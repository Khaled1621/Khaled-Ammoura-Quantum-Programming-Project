# All the imports
import pennylane as qml
import numpy as np

# Device
dev = qml.device("default.qubit", wires=2)

# Create the oracle
def deutsch_oracle(f):
    def oracle():
        if f(0) == f(1):
            # Apply Identity Gate --> Do nothing
            pass
        else:
            # Apply CNOT gate to get the negation of the applied function on the qubit
            qml.CNOT(wires=[0, 1])
    return oracle

@qml.qnode(dev)
def deutsch_circuit(f):
    # Apply Hadamard to the first qubit. Apply Pauli-X then Hadamard to the second qubit
    qml.Hadamard(wires=0)
    qml.PauliX(wires=1)
    qml.Hadamard(wires=1)

    # Apply the oracle
    oracle = deutsch_oracle(f)
    oracle()

    # Apply Hadamard to the first qubit again. To get it back to the computational bases (either 0 or 1)
    qml.Hadamard(wires=0)

    # Measure the expectation value of Pauli-Z on the first qubit
    return qml.expval(qml.PauliZ(0))

# Drawing function
def draw_circuit(circuit, f):
    return qml.draw(circuit)(f)

# Constant function f(x) = 0
constant_f = lambda x: 0  # Function is constant
result_constant = deutsch_circuit(constant_f)
drawer1 = draw_circuit(deutsch_circuit, constant_f)
print(drawer1)
print("Measurement result for constant function f(x) = 0:", result_constant)

# Balanced function f(x) = x
balanced_f = lambda x: x  # Function is balanced
result_balanced = deutsch_circuit(balanced_f)
drawer2 = draw_circuit(deutsch_circuit, balanced_f)
print(drawer2)
print("Measurement result for balanced function f(x) = x:", result_balanced)

# To identify which qubit it was exactly
def interpret_expval(expval):
    return 0 if expval > 0 else 1

constant_result = interpret_expval(result_constant)
balanced_result = interpret_expval(result_balanced)

print(f"Result for constant function: {constant_result} (0 = constant)")
print(f"Result for balanced function: {balanced_result} (1 = balanced)")