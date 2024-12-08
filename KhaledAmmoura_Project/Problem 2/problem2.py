# All the imports
import pennylane as qml
import numpy as np

for num_qubits in [3,5]:

    # Create the devices
    dev = qml.device("default.qubit", wires=num_qubits)

    # Create the circuit
    @qml.qnode(dev)
    def circuit(num_qubits):
        qml.Hadamard(wires=0)
        for i in range(1,num_qubits):
            qml.CNOT(wires=[i-1,i])
        return qml.state(), qml.probs(wires=range(num_qubits))

    # Drawing function
    def draw_circuit(circuit, num_qubits):
        return qml.draw(circuit)(num_qubits)

    drawer = draw_circuit(circuit, num_qubits)

    # Test
    states, probabilities = circuit(num_qubits)

    # Fidelity measurement (optional)
    # Target GHZ state for comparison
    GHZ = np.zeros(2**num_qubits)
    GHZ[0] = 1 / np.sqrt(2)  # Coefficient for |00000>
    GHZ[-1] = 1 / np.sqrt(2)  # Coefficient for |11111>
    fidelity = np.abs(np.dot(np.conj(GHZ), states))**2

    print("Generated Quantum Circuits:\n", drawer)
    print("Generated GHZ State Vector:\n", states)
    print("Fidelity with Target GHZ State:", fidelity)
    if num_qubits ==3:
        print("Measurement Probabilities (|000>, ..., |111>):", probabilities)
    else:
        print("Measurement Probabilities (|00000>, ..., |11111>):", probabilities)

num_qubits = 5
# Effiient Way
# Create the devices
dev = qml.device("default.qubit", wires=num_qubits)

# Create the circuit
@qml.qnode(dev)
def circuit(num_qubits):
    # Step 1: Apply Hadamard to the first qubit
    qml.Hadamard(wires=0)
    
    # Step 2: Apply parallel CNOT gates (binary tree structure)
    # Round 1
    qml.CNOT(wires=[0, 1])
    qml.CNOT(wires=[2, 3])
    
    # Round 2
    qml.CNOT(wires=[1, 2])
    
    # Round 3
    qml.CNOT(wires=[3, 4])
    
    # Return the quantum state and probabilities
    return qml.state(), qml.probs(wires=range(num_qubits))

# Drawing function
def draw_circuit(circuit, num_qubits):
    return qml.draw(circuit)(num_qubits)

drawer = draw_circuit(circuit, num_qubits)

# Test
states, probabilities = circuit(num_qubits)

# Fidelity measurement (optional)
# Target GHZ state for comparison
GHZ = np.zeros(2**num_qubits)
GHZ[0] = 1 / np.sqrt(2)  # Coefficient for |00000>
GHZ[-1] = 1 / np.sqrt(2)  # Coefficient for |11111>
fidelity = np.abs(np.dot(np.conj(GHZ), states))**2

print("Generated Quantum Circuits:\n", drawer)
print("Generated GHZ State Vector:\n", states)
print("Fidelity with Target GHZ State:", fidelity)
if num_qubits ==3:
    print("Measurement Probabilities (|000>, ..., |111>):", probabilities)
else:
    print("Measurement Probabilities (|00000>, ..., |11111>):", probabilities)