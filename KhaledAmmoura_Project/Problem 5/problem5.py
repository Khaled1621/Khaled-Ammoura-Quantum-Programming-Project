# All the imports
import pennylane as qml
import numpy as np

# Initialization
num_qubits =int(input("Enter the desired number of qubits: "))

# Create the device
dev = qml.device("default.qubit", wires=num_qubits)

# Create the oracle
def deutsch_oracle(f):
    def oracle():
        for i in range(num_qubits - 1):
            if f(i): # If f(i)==1
                qml.CNOT(wires=[i, num_qubits - 1])
    return oracle

# Create the circuit
@qml.qnode(dev)
def deutsch_jozsa_circuit(f):
    # Apply Hadamard gates to the first n-1 qubits
    for i in range(num_qubits - 1):
        qml.Hadamard(wires=i)
    # Apply X gate to the last qubit
    qml.PauliX(wires=num_qubits - 1)
    qml.Hadamard(wires=num_qubits - 1)

    # Apply the oracle
    oracle = deutsch_oracle(f)
    oracle()

    # Apply Hadamard to the first n-1 qubits again
    for i in range(num_qubits - 1):
        qml.Hadamard(wires=i)

    return [qml.expval(qml.PauliZ(i)) for i in range(num_qubits - 1)]

# Drawing function
def draw_circuit(circuit, f):
    return qml.draw(circuit)(f)

# Constant function f(x) = 0
constant_f = lambda x: 0  # Function is constant
result_constant = deutsch_jozsa_circuit(constant_f)
drawer1 = draw_circuit(deutsch_jozsa_circuit, constant_f)
print(drawer1)
print("Measurement result for constant function f(x) = 0:", [float(val) for val in result_constant])

# Balanced function f(x) = x
balanced_f = lambda x: x  # Function is balanced
result_balanced = deutsch_jozsa_circuit(balanced_f)
drawer2 = draw_circuit(deutsch_jozsa_circuit, balanced_f)
print(drawer2)
print("Measurement result for balanced function f(x) = x:", [float(val) for val in result_balanced])

# To identify which qubit it was exactly
def interpret_expval(expvals):
    return 0 if all(e > 0 for e in expvals) else 1

constant_result = interpret_expval(result_constant)
balanced_result = interpret_expval(result_balanced)

print(f"Result for constant function: {constant_result} (0 = constant)")
print(f"Result for balanced function: {balanced_result} (1 = balanced)")