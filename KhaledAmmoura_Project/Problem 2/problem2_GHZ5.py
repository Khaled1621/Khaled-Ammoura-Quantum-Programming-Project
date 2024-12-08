# All the imports
import pennylane as qml
import numpy as np

# Initialization
num_qubits = 5

# Create the device
dev = qml.device("default.qubit", wires=num_qubits)

# Create the Circuit
@qml.qnode(dev)
def circuit():
    qml.Hadamard(wires=0)
    qml.CNOT(wires=[0,4])
    qml.CNOT(wires=[0,2])
    qml.CNOT(wires=[0,1])
    qml.CNOT(wires=[2,3])
    return qml.state(), qml.probs(wires=[0,1,2,3,4])
@qml.qnode(dev)
def expval_circuit():
    qml.Hadamard(wires=0)
    qml.CNOT(wires=[0,4])
    qml.CNOT(wires=[0,2])
    qml.CNOT(wires=[0,1])
    qml.CNOT(wires=[2,3])
    return [qml.expval(qml.PauliZ(wires=i)) for i in range(num_qubits)]

# Drawing function
def draw_circuit(circuit):
    return qml.draw(circuit)()
drawer = draw_circuit(circuit)
drawer2 = draw_circuit(expval_circuit)

# Test
states, probabilities = circuit()
exp_vals = expval_circuit()

# Create the target state 
GHZ_target = np.zeros(2**num_qubits)
GHZ_target[0] = 1 / np.sqrt(2)  # Coefficient for |00000>
GHZ_target[-1] = 1 / np.sqrt(2)  # Coefficient for |11111>
fidelity = np.abs(np.dot(np.conj(GHZ_target), states))**2

print("Generated Quantum Circuits:\n", drawer)
print("Generated Quantum Circuits of the Exp Val:\n", drawer2)
print("Generated GHZ State Vector:\n", states)
print("Fidelity with Target GHZ State:", fidelity)
exp_vals_clean = [float(val) for val in exp_vals]
print(f"Expectation Values: {exp_vals_clean}")
print("Measurement Probabilities (|00000>, ..., |11111>):", probabilities)