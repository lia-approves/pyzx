# PyZX - Python library for quantum circuit rewriting
#        and optimisation using the ZX-calculus
# Copyright (C) 2018 - Aleks Kissinger and John van de Wetering

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


import math
from fractions import Fraction

from . import Circuit
from .gates import qasm_gate_table, ZPhase, XPhase
from .qasmparser import QASMParser

class qiskitQASMParser(QASMParser):
    """Class for parsing QASM source files into circuit descriptions."""
    def qiskitparse(self, s, strict=True):
        lines = s.splitlines()
        r = []
        #strip comments
        for s in lines:
            if s.find("//")!=-1:
                t = s[0:s.find("//")].strip()
            else: t = s.strip()
            if t: r.append(t)

        if r[0].startswith("OPENQASM"):
            r.pop(0)
        elif strict:
            raise TypeError("File does not start with OPENQASM descriptor")

        if r[0].startswith('include "qelib1.inc";'):
            r.pop(0)
        elif strict:
            raise TypeError("File is not importing standard library")

        data = "\n".join(r)
        # Strip the custom command definitions from the normal commands
        while True:
            i = data.find("gate ")
            if i == -1: break
            j = data.find("}", i)
            self.parse_custom_gate(data[i:j+1])
            data = data[:i] + data[j+1:]
        #parse the regular commands
        commands = [s.strip() for s in data.split(";") if s.strip()]
        circuit_list = []
        counter = 0
        whichpyzx = []
        gates = []
        for c in commands:
            pc = (self.parse_command_wrapper(c, self.registers))
            if pc is None:
               if gates:
                   circ = Circuit(self.qubit_count)
                   circ.gates = self.gates
                   circuit_list.append(circ)
               ##add nonpyzx circuit to circuitlist, update whichpyzx and counter
            else:
                self.gates.extend(pc)
        circ = Circuit(self.qubit_count)
        circ.gates = self.gates
        self.circuit = circ
        return self.circuit

    def parse_command_wrapper(self, c, registers):
        try:
            parse_command(self, c, registers)
        except:
            return None
        return gates
