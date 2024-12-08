# All the imports
import pennylane as qml
import numpy as np

# Initialization
num_qubits =int(input("Enter the desired number of qubits (minimum 2): "))
if num_qubits < 2:
    raise ValueError("Number of qubits must be at least 2.")

# Create the device
dev = qml.device("default.qubit", wires=num_qubits)

# Create the oracle
def deutsch_oracle(f):
    def oracle():
        for i in range(num_qubits - 1):
            if f(i) == 1:
                qml.CNOT(wires=[i, num_qubits - 1])
    return oracle

# Create the circuit
@qml.qnode(dev)
def deutsch_jozsa_circuit(f):
    for i in range(num_qubits-1):
        qml.Hadamard(wires=i)
    qml.PauliX(wires=num_qubits-1)
    qml.Hadamard(wires=num_qubits-1)

    # Apply the oracle
    oracle = deutsch_oracle(f)
    oracle()
    
    # Apply Hadamard to the first qubit again. To get it back to the computational bases (either 0 or 1)
    for i in range(num_qubits-1):
        qml.Hadamard(wires=i)
    
    # Measure all qubits except the last
    return [qml.expval(qml.PauliZ(i)) for i in range(num_qubits - 1)]

# Drawing function
def draw_circuit(circuit, f):
    return qml.draw(circuit)(f)

# Constant function f(x) = 0
constant_f = lambda x: 0  # Function is constant
result_constant = deutsch_jozsa_circuit(constant_f)
clean_result_constant = [float(r) for r in result_constant]
drawer1 = draw_circuit(deutsch_jozsa_circuit, constant_f)
print(drawer1)
print("Measurement results for constant function:", clean_result_constant)

# Balanced function f(x) = x % 2
balanced_f = lambda x: x % 2  # Function is balanced
result_balanced = deutsch_jozsa_circuit(balanced_f)
clean_result_balanced = [float(r) for r in result_balanced]
drawer2 = draw_circuit(deutsch_jozsa_circuit, balanced_f)
print(drawer2)
print("Measurement results for balanced function:", clean_result_balanced)

# Interpretation of results
def interpret_results(results):
    # If all measurements are close to 1, the function is constant
    # If any measurement is not close to 1, the function is balanced
    return "constant" if all(np.isclose(r, 1) for r in results) else "balanced"

constant_result = interpret_results(result_constant)
balanced_result = interpret_results(result_balanced)

print(f"Result for constant function: {constant_result} (0 = constant)")
print(f"Result for balanced function: {balanced_result} (1 = balanced)")