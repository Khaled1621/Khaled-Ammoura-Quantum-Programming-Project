# All the imports
import pennylane as qml
import numpy as np

# Initialization
num_qubits = 5  # 5 qubits for the GHZ state

# Create the device
dev = qml.device("default.qubit", wires=num_qubits)

# Optimized circuit for the GHZ state
@qml.qnode(dev)
def optimized_five_qubit_ghz():
    # Step 1: Apply Hadamard to the first qubit
    qml.Hadamard(wires=0)
    
    # Step 2: Apply a multi-controlled Z gate with qubits 1-4 as controls and qubit 0 as target
    control_wires = [1, 2, 3, 4]
    target_wire = 0
    qml.MultiControlledX(wires=control_wires + [target_wire], control_values='1'*4)
    
    # Return the quantum state
    return qml.state()

# Target GHZ state for comparison
ghz_target_5 = np.zeros(2**num_qubits, dtype=complex)  # 32 elements for 5 qubits
ghz_target_5[0] = 1 / np.sqrt(2)  # Amplitude for |00000>
ghz_target_5[-1] = 1 / np.sqrt(2)  # Amplitude for |11111>

# Generate the GHZ state
state = optimized_five_qubit_ghz()
def draw_circuit(circuit):
    return qml.draw(circuit)()

drawer = draw_circuit(optimized_five_qubit_ghz)
print(drawer)
# Print the state vector
print("\nGenerated 5-Qubit GHZ State Vector:\n", state)

# Calculate Fidelity
fidelity = np.abs(np.dot(np.conj(ghz_target_5), state))**2
print("\nFidelity with Target GHZ State:", fidelity)
