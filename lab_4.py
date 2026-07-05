import numpy as np
import math

from qiskit import *
from qiskit_aer import AerSimulator
from qiskit.circuit import Gate

# All 2+1 oracles should read input from q1 and q0,
# and store the result on q2


def zero_oracle() -> Gate:
    # Creates 2+1 bit oracle that always returns 0

    qc = QuantumCircuit(3)
    # your implementation here
    # nothing needed here already all 0s
    return qc.to_gate(label="Zero Oracle")


def one_oracle() -> Gate:
    # Creates 2+1 bit oracle that always returns 1
    qc = QuantumCircuit(3)
    # your implementation here
    qc.x(2)
    return qc.to_gate(label="One Oracle")


def AND_oracle() -> Gate:
    # Creates 2+1 bit oracle that returns q0 & q1
    qc = QuantumCircuit(3)
    # your implementation here
    # toffoli: 00 -> 0, 01 -> 0, 10 -> 0, 11 -> 1
    qc.ccx(0,1,2)
    return qc.to_gate(label="AND Oracle")

def OR_oracle() -> Gate:
    # Creates 2+1 bit oracle that returns q0 | q1
    qc = QuantumCircuit(3)
    # your implementation here
    # using discrete math: !q2 = !(q0 OR q1) -> !q0 AND !q1
    #!q0:
    qc.x(0)
    #!q1
    qc.x(1)
    qc.ccx(0,1,2)
    #since it is !q2 need to reverse it
    qc.x(2)
    # print("hello")
    # print(qc)
    # undo
    qc.x(0)
    qc.x(1)
    return qc.to_gate(label="OR Oracle")


def XOR_oracle() -> Gate:
    # Creates 2+1 bit oracle that returns q0 ^ q1
    qc = QuantumCircuit(3)
    # your implementation here
    # Cnot gate: if control is 0 nothing, if control is 1 flip target
    # Since we need to flip flop, 0 -> 2: 000 -> 000, 001 -> 101, 010 -> 010, 011 -> 111
    # 1 -> 2 000 -> 000, 101 -> 101, 010 -> 110, 111 -> 011
    qc.cx(0, 2)
    qc.cx(1, 2)
    return qc.to_gate(label="XOR Oracle")


def XNOR_oracle() -> Gate:
    # Creates 2+1 bit oracle that returns q0 ~^ q1
    qc = QuantumCircuit(3)
    # your implementation here
    # can be written as ~ (q0 ^ q1)
    # XOR
    qc.cx(0, 2)
    qc.cx(1, 2)
    # ~
    qc.x(2)
    return qc.to_gate(label="XNOR Oracle")


def DJ_generator(oracle: Gate) -> QuantumCircuit:
    # Generates circuit to apply DJ algorithm on provided
    # 2+1 oracle (does not include measurement)

    qc = QuantumCircuit(3, 2)  
    # h gate on each qubit excluding the target qubit
    n = oracle.num_qubits
    qc.h(range(n-2))
    # qubit target starts at |1> and h gate applied 
    qc.x(n-1)
    qc.h(n-1)
    # use the append method to add the gate input to the circuit
    qc.append(oracle, range(3))
    # both qubits excluding target get h gate again
    qc.h(range(n-2))
    return qc


def is_balanced(oracle: Gate) -> bool:
    # Requires that oracle is either balanced or constant
    # Returns true if an oracle is balanced, false if constant
    # Operates by performing measurement on DJ circuit
    # generate the circuit with the gate input: this is just run_DJ
    qc = DJ_generator(oracle)
    n = oracle.num_qubits
    # measure the two qubits that are inputs and not target
    qc.measure(range(n-1), range(n-1))
    # simulate 1024 times (from run_DJ)
    sim = AerSimulator()
    qc = transpile(qc, sim)
    counts = sim.run(qc, shots=1024).result().get_counts()
    # this is new: need to check if the 0s string is in the counts
    # if it is then constant otherwise balanced
    string = "0"*(n-1)
    # print(string)
    if string in counts:
        return False
    else:
        return True
    pass
