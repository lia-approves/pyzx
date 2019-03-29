// Initial wiring: [5, 14, 2, 9, 0, 10, 6, 3, 11, 18, 4, 17, 7, 8, 19, 12, 1, 16, 13, 15]
// Resulting wiring: [5, 14, 2, 9, 0, 10, 6, 3, 11, 18, 4, 17, 7, 8, 19, 12, 1, 16, 13, 15]
OPENQASM 2.0;
include "qelib1.inc";
qreg q[20];
cx q[5], q[3];
cx q[3], q[2];
cx q[6], q[4];
cx q[7], q[6];
cx q[6], q[4];
cx q[7], q[1];
cx q[7], q[6];
cx q[8], q[1];
cx q[9], q[8];
cx q[8], q[1];
cx q[11], q[8];
cx q[8], q[7];
cx q[7], q[6];
cx q[11], q[10];
cx q[8], q[7];
cx q[12], q[11];
cx q[11], q[8];
cx q[12], q[11];
cx q[13], q[7];
cx q[7], q[1];
cx q[14], q[13];
cx q[13], q[12];
cx q[12], q[11];
cx q[12], q[7];
cx q[11], q[8];
cx q[7], q[2];
cx q[12], q[11];
cx q[12], q[7];
cx q[14], q[13];
cx q[15], q[14];
cx q[16], q[13];
cx q[13], q[6];
cx q[6], q[4];
cx q[13], q[6];
cx q[16], q[13];
cx q[17], q[12];
cx q[12], q[6];
cx q[17], q[11];
cx q[6], q[3];
cx q[11], q[10];
cx q[3], q[2];
cx q[17], q[16];
cx q[6], q[3];
cx q[17], q[12];
cx q[17], q[11];
cx q[18], q[11];
cx q[8], q[9];
cx q[7], q[13];
cx q[7], q[8];
cx q[13], q[14];
cx q[7], q[12];
cx q[8], q[11];
cx q[5], q[6];
cx q[5], q[14];
cx q[6], q[12];
cx q[3], q[6];
cx q[6], q[12];
cx q[12], q[18];
cx q[1], q[7];