import numpy as np
import random
from typing import Optional

class LQ3K:
    """Create a new circuit with the specified number of qubits and no gates.

    Circuit supports limited measuring capabilities: all qubits are automatically measured
    at the end of the circuit when running "simulate_run"  
    
    Args:
        num_qubits: total number of quantum bits in the circuit (can't be modified after
        initialization)

        Example:
            qc = LQ3K(2)
            qc.h(0)
            qc.cx(0, 1)
            qc.simulate_run([1,0,0,0]) # returns 0 (0b00) ~50% of time, and 3 (0b11) ~50% of time
            

    """
    #gates for ref
    #from online: use dtype=complex to initialize a complex array
    #X = [[0, 1], [1, 0]] 
    #Y = [[0, -1j], [1j, 0]]
    #Z= [[1, 0], [0, -1]] 
    #H = (1 / np.sqrt(2)) * [[1, 1], [1, -1]]
    #S = [[1, 0], [0, 1j]]
    #S Dagger = [[1, 0], [0, -1j]] 
    #T = [[1, 0], [0, np.exp(1j * np.pi / 4)]]
    #T Dagger = [[1, 0], [0, np.exp(-1j * np.pi / 4)]]
    #swap = [[1, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 1]]  
    #CX = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]]

    class InvalidStateVector(Exception):
        """Not a valid state vector"""


    def __init__(self, num_qubits: int) -> None:
        self.num_qubits = num_qubits
        self.unitary = np.eye(2**num_qubits, dtype=complex)
        pass

    def swap(self, idx_1: int, idx_2: int) -> None:
        """Applies SWAP gate, switching the state of the two specified qubits
        A qubit CANNOT be swapped with itself"""
        # check the two indices 
        if idx_1 == idx_2 or idx_1 < 0 or idx_2 < 0 or idx_1 >= self.num_qubits or idx_2 >= self.num_qubits:
            raise IndexError("qubits not equal indices")
        # swap gate can be comprised of 3 cx gates
        LQ3K.cx(self,idx_1, idx_2)
        LQ3K.cx(self,idx_2, idx_1)
        LQ3K.cx(self,idx_1, idx_2)
        # swap_matrix = np.eye(2**self.num_qubits, dtype=complex)

        # for i in range(2**self.num_qubits):
        #     swapped_index = (i ^ (1 << idx_1)) if ((i >> idx_1) & 1) != ((i >> idx_2) & 1) else i ^ (1 << idx_2)
        #     swap_matrix[i, i] = 0
        #     swap_matrix[i, swapped_index] = 1
        
        # self.unitary = swap_matrix @ self.unitary

        pass

    def cx(self, control_qubit: int, target_qubit: int) -> None:
        """Applies CX, also known as controlled-NOT gate, to the specified qubits"""
        # check the two indices
        if control_qubit == target_qubit or control_qubit < 0 or target_qubit < 0 or control_qubit >= self.num_qubits or target_qubit >= self.num_qubits:
            raise IndexError("qubits not equal indices")
        
        cx_matrix = np.eye(2**self.num_qubits, dtype=complex)
        for i in range(2**self.num_qubits):
            # check if the binary value at that index (the control_qubit) is 1 otherwise don't do anything
            if (i >> control_qubit) & 1:
                # get a single binary value and the index (online)
                flipped_index = i ^ (1 << target_qubit)
                cx_matrix[i, i] = 0
                cx_matrix[i, flipped_index] = 1
        
        self.unitary = cx_matrix @ self.unitary

        pass

    def x(self, qubit_idx: int) -> None:
        """Applies X gate to the specified qubit"""
        """Applies X gate to the specified qubit"""
        if qubit_idx < 0 or qubit_idx >= self.num_qubits:
            raise IndexError(f"qubits not equal")
            
        identity = np.eye(2, dtype=complex)
        X_gate = np.array([[0, 1], [1, 0]], dtype=complex)
        new_unitary = np.eye(1, dtype=complex)
        
        for i in range(self.num_qubits):
            if i == qubit_idx:
                # for all others order should be gate, unitary
                new_unitary = np.kron(X_gate, new_unitary)  
            else:
                new_unitary = np.kron(identity, new_unitary)  

        self.unitary = new_unitary @ self.unitary   
        pass

    def y(self, qubit_idx: int) -> None:
        """Applies Y gate to the specified qubit"""
        if qubit_idx < 0 or qubit_idx >= self.num_qubits:
            raise IndexError(f"qubits not equal")
            
        identity = np.eye(2, dtype=complex)
        Y_gate = np.array([[0, -1j], [1j, 0]], dtype=complex)
        new_unitary = np.eye(1, dtype=complex)
        
        for i in range(self.num_qubits):
            if i == qubit_idx:
                new_unitary = np.kron(Y_gate, new_unitary)  
            else:
                new_unitary = np.kron(identity, new_unitary)  

        self.unitary = new_unitary @ self.unitary   
        pass

    def z(self, qubit_idx: int) -> None:
        """Applies Z gate to the specified qubit"""
        if qubit_idx < 0 or qubit_idx >= self.num_qubits:
            raise IndexError(f"qubits not equal")
            
        identity = np.eye(2, dtype=complex)
        Z_gate = np.array([[1, 0], [0, -1]], dtype=complex)
        new_unitary = np.eye(1, dtype=complex)
        
        for i in range(self.num_qubits):
            if i == qubit_idx:
                new_unitary = np.kron(Z_gate, new_unitary)  
            else:
                new_unitary = np.kron(identity, new_unitary)  

        self.unitary = new_unitary @ self.unitary   
        pass

    def h(self, qubit_idx: int) -> None:
        """Applies Hadamard gate to the specified qubit"""
        if qubit_idx < 0 or qubit_idx >= self.num_qubits:
            raise IndexError(f"qubits not equal")
            
        identity = np.eye(2, dtype=complex)
        H_gate = (1 / np.sqrt(2)) * np.array([[1, 1], [1, -1]], dtype=complex)
        new_unitary = np.eye(1, dtype=complex)
        
        for i in range(self.num_qubits):
            if i == qubit_idx:
                new_unitary = np.kron(H_gate, new_unitary)  
            else:
                new_unitary = np.kron(identity, new_unitary)  
        self.unitary = new_unitary @ self.unitary 
        pass

    def s(self, qubit_idx: int) -> None:
        """Applies S gate to the specified qubit"""
        if qubit_idx < 0 or qubit_idx >= self.num_qubits:
            raise IndexError(f"qubits not equal")
            
        identity = np.eye(2, dtype=complex)
        S_gate = np.array([[1, 0], [0, 1j]], dtype=complex)
        new_unitary = np.eye(1, dtype=complex)
        
        for i in range(self.num_qubits):
            if i == qubit_idx:
                new_unitary = np.kron(S_gate, new_unitary)  
            else:
                new_unitary = np.kron(identity, new_unitary)  
        self.unitary = new_unitary @ self.unitary 
        pass

    def sdg(self, qubit_idx: int) -> None:
        """Applies S dag gate (complex conjugate of S) to the specified qubit"""
        if qubit_idx < 0 or qubit_idx >= self.num_qubits:
            raise IndexError(f"qubits not equal")
            
        identity = np.eye(2, dtype=complex)
        Sdg_gate = np.array([[1, 0], [0, -1j]], dtype=complex)
        new_unitary = np.eye(1, dtype=complex)
        
        for i in range(self.num_qubits):
            if i == qubit_idx:
                new_unitary = np.kron(Sdg_gate, new_unitary)  
            else:
                new_unitary = np.kron(identity, new_unitary)  
        self.unitary = new_unitary @ self.unitary 
        pass

    def t(self, qubit_idx: int) -> None:
        """Applies T gate to the specified qubit"""
        if qubit_idx < 0 or qubit_idx >= self.num_qubits:
            raise IndexError(f"qubits not equal")
            
        identity = np.eye(2, dtype=complex)
        T_gate = np.array([[1, 0], [0, np.exp(1j * np.pi / 4)]], dtype=complex)
        new_unitary = np.eye(1, dtype=complex)
        
        for i in range(self.num_qubits):
            if i == qubit_idx:
                new_unitary = np.kron(T_gate, new_unitary)  
            else:
                new_unitary = np.kron(identity, new_unitary)  
        self.unitary = new_unitary @ self.unitary 
        pass

    def tdg(self, qubit_idx: int) -> None:
        """Applies T dag gate (complex conjugate of T) to the specified qubit"""
        if qubit_idx < 0 or qubit_idx >= self.num_qubits:
            raise IndexError(f"qubits not equal")
            
        identity = np.eye(2, dtype=complex)
        Tdg_gate = np.array([[1, 0], [0, np.exp(-1j * np.pi / 4)]], dtype=complex)
        new_unitary = np.eye(1, dtype=complex)
        
        for i in range(self.num_qubits):
            if i == qubit_idx:
                new_unitary = np.kron(Tdg_gate, new_unitary)  
            else:
                new_unitary = np.kron(identity, new_unitary)  
        self.unitary = new_unitary @ self.unitary 
        pass


    def simulate_run(self, initial_state: Optional[np.ndarray] = None) -> int:
        """Evolves state vector after initial_state is passed through circuit,
        and then simulates a probabilistic measurement of all qubits, returning
        result in decimal. Probabilities are determined by final state vector

        If no initial state is passed in, default state of |0> should be used

        Example:
            qc = LQ3K(2)
            qc.h(0)
            qc.cx(0, 1)
            qc.simulate_run() # returns 0 (0b00) ~50% of time, and 3 (0b11) ~50% of time
        
        Returns: Integer representation of measured bits
        Raises:
            InvalidStateVector: When initial_state is not unit length."""
        if initial_state is None:
            initial_state = np.zeros(2**self.num_qubits, dtype=complex)
            initial_state[0] = 1  

        if not np.allclose(np.linalg.norm(initial_state), 1):
            raise self.InvalidStateVector("Not normalized ")
        
        final_state = self.unitary @ initial_state
        # print(final_state)
        # print(self.unitary)
        probabilities = np.abs(final_state)**2
        outcomes = list(range(2**self.num_qubits))
        return random.choices(outcomes, probabilities)[0]
        pass
