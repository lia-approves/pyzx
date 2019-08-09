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

class QiskitQASMParser(QASMParser):
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
        circuit_list = [] #list of circuits (some qiskit qasm, some pyzx circuits)
        whichpyzx = [] #which indexed circuits in circuit_list are pyzx circuits
        self.gates = [] #current list of gates

        for k in range(len(commands)):
            c = commands[k]
            pc = self.parse_command(c, self.registers)
            if pc is None:
                if self.gates:
                    circ = Circuit(self.qubit_count)
                    circ.gates = self.gates
                    whichpyzx.append(len(circuit_list))
                    circuit_list.append(circ)
                    self.gates = []
                circuit_list.append(c)
            else:
                self.gates.extend(pc)
                if k == len(commands) - 1:
                    circ = Circuit(self.qubit_count)
                    circ.gates = self.gates
                    whichpyzx.append(len(circuit_list))
                    circuit_list.append(circ)
                    self.gates = []
        return circuit_list, whichpyzx

    def parse_command(self, c, registers):
        try:
            pc = super().parse_command(c, registers)
        except TypeError:
            return None
        return pc
