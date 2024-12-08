# All the imports
import pennylane as qml
import numpy as np

# Initialization
num_qubits =int(input("Enter the desired number of qubits (minimum 2): "))
if num_qubits < 2:
    raise ValueError("Number of qubits must be at least 2.")

# Create the device
dev = qml.device("default.qubit", wires=num_qubits)

# Define oracles
def constant_oracle():
    pass

def balanced_oracle():
    qml.CNOT(wires=[0, num_qubits - 1])  # Flip ancillary if the first qubit is 1

# Deutsch-Jozsa circuit
@qml.qnode(dev)
def deutsch_jozsa_circuit(oracle):
    for i in range(num_qubits - 1):
        qml.Hadamard(wires=i)
    qml.PauliX(wires=num_qubits - 1)
    qml.Hadamard(wires=num_qubits - 1)
    oracle()
    for i in range(num_qubits - 1):
        qml.Hadamard(wires=i)
    return [qml.expval(qml.PauliZ(i)) for i in range(num_qubits - 1)]

# Drawing function
def draw_circuit(circuit, f):
    return qml.draw(circuit)(f)

# Test constant function
result_constant = deutsch_jozsa_circuit(constant_oracle)
clean_result_constant = [float(r) for r in result_constant]
drawer1 = draw_circuit(deutsch_jozsa_circuit, constant_oracle)
print(drawer1)
print("Measurement results for constant function:", clean_result_constant)

# Test balanced function
result_balanced = deutsch_jozsa_circuit(balanced_oracle)
clean_result_balanced = [float(r) for r in result_balanced]
drawer2 = draw_circuit(deutsch_jozsa_circuit, balanced_oracle)
print(drawer2)
print("Measurement results for balanced function:", clean_result_balanced)

# Interpretation
def interpret_results(results):
    return "constant" if all(np.isclose(r, 1) for r in results) else "balanced"

constant_result = interpret_results(result_constant)
balanced_result = interpret_results(result_balanced)

print(f"Result for constant function: {constant_result} (0 = constant)")
print(f"Result for balanced function: {balanced_result} (1 = balanced)")