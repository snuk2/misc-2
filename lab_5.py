import numpy as np
import math
from typing import List, Dict

from qiskit import *
from qiskit.circuit.library.standard_gates import MCXGate

def diffuser(n: int) -> QuantumCircuit:
    """Returns QuantumCircuit that rotates the state around |s>
    Args:
        n: How many qubits the diffuser should process"""
    qc = QuantumCircuit(n)

    # Map |s> -> |00..0> ->|11..1> 
    # this is the h gate for all the qubits
    qc.h(range(n))
    
    # Rotate around |0>
    # this is the x gate for all the qubits 
    qc.x(range(n))
    # |11..1> -> |00..0> -> |s>
    # implement the multi-qubit controlled Z gste

    if n > 1:
        # last qubit in |+> state
        qc.h(n - 1) 
        # Multi-qubit controlled-Z from lab 5 spec
        num_ctrl_bits = n - 1
        # print(n-1)
        # get a binary number of n - 1 1s as the control state
        mcx_state = (1 << num_ctrl_bits) - 1
        # print(mcx_state)
        gate = MCXGate(num_ctrl_bits, ctrl_state=mcx_state)
        qc.append(gate, range(n))
        # print(bin((1 << n) - 1))
        # undo last qubit in |+> state
        qc.h(n - 1)  
    else:
        # if only one qubit circut then it is a z gate instead of controlled 
        qc.z(0)

    # undo the x gate
    qc.x(range(n))

    # do the h gate again
    qc.h(range(n))
    
    # return the circuit
    return qc

def grover() -> QuantumCircuit:
    """Returns a Grover circuit to solve the below mystery_oracle
       Make sure to NOT add measruments here, as the tests already do so"""

    # mystery oracle has 6 qubits 
    qc = QuantumCircuit(6, 3)

    # put the first three qubits into superposition
    qc.h(0)
    qc.h(1)
    qc.h(2)

    # make the oracle with mystery_oracle and
    # apply the oracle to the current circuit with the superposition on three qubits
    oracle = mystery_oracle()
    qc.append(oracle, range(6))

    # apply the diffuser on only the first three qubits where the input is provided 
    qc.append(diffuser(3), range(3))

    # return the quantum circuit
    return qc
    pass 

# DO NOT MODIFY THIS FUNCTION
def mystery_oracle():
    """Returns QuantumCircuit implementing some 3->1 bit function
       Input are provided in bits 0-2 and the result is placed on
       bit 5. Bits 3-4 are used as temporary "ancilla bits"
    """
    oracle = QuantumCircuit(6)
    
    # t1
    oracle.cx(0,3)
    oracle.cx(1,3)

    # t2
    oracle.x({0,2})
    oracle.cx(0,4)
    oracle.cx(2,4)
    oracle.x({0,2})

    # o
    gate = MCXGate(3, ctrl_state=0b111)
    oracle.append(gate,{5,4,3,1})

    # uncompute t2
    oracle.x({0,2})
    oracle.cx(2,4)
    oracle.cx(0,4)
    oracle.x({0,2})

    # uncompute t1
    oracle.cx(1,3)
    oracle.cx(0,3)


    return oracle