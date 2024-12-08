# All the imports
import pennylane as qml
import numpy as np

# Create the devices
dev1 = qml.device("default.qubit", wires=1)
dev2 = qml.device("default.qubit", wires=1)

# Create the circuit function, which takes
# Two angles: theta1 (θ_1) and theta2 (θ_2)
# Two functions: func1 and func2, where they can be either RX or RY
def circuit(theta1, theta2, func1, func2):
    func1(theta1, wires=0)
    func2(theta2, wires=0)
    return qml.expval(qml.PauliX(wires=0)), qml.probs(wires=0), qml.expval(qml.PauliZ(wires=0))

# Define the QNodes
@qml.qnode(dev1)
def circuit1(theta1, theta2):
    return circuit(theta1, theta2, qml.RX, qml.RY)

@qml.qnode(dev2)
def circuit2(theta1, theta2):
    return circuit(theta1, theta2, qml.RY, qml.RX)

# Drawing function
def draw_circuit(circuit, theta1, theta2):
    return qml.draw(circuit)(theta1, theta2)

# Initializations
theta1 = 5 * np.pi / 8
theta2 = np.pi / 5


# Compute results for both circuits
result1 = circuit1(theta1, theta2)
result2 = circuit2(theta2, theta1)

# Extract the results
expval1_x, probs1, expval1_z = result1
expval2_x, probs2, expval2_z = result2

# Draw the circuits and print the results
drawer1 = draw_circuit(circuit1, theta1, theta2)
print("Circuit 1: ",drawer1)
print(f"Circuit 1 - Expectation Value of Pauli-X: {expval1_x:.4f}")
print(f"Circuit 1 - Expectation Value of Pauli-Z: {expval1_z:.4f}")
print(f"Circuit 1 - Probability |0>: {probs1[0]:.4f}, Probability |1>: {probs1[1]:.4f}")

drawer2 = draw_circuit(circuit2, theta1, theta2)
print("Circuit 2: ",drawer2)
print(f"Circuit 2 - Expectation Value of Pauli-X: {expval2_x:.4f}")
print(f"Circuit 2 - Expectation Value of Pauli-Z: {expval2_z:.4f}")
print(f"Circuit 2 - Probability |0>: {probs2[0]:.4f}, Probability |1>: {probs2[1]:.4f}")

#To check the expected value:
#Let the final state of the |ψ>
#Then, to get the expectation value of the Pauli-X gate, we need to calculate:<ψ|X|ψ>

# Calculate the absolute difference
absolute_difference_x = np.abs(expval1_x - expval2_x)
print(f"Absolute Difference of Pauli-X: {absolute_difference_x:.4f}")

absolute_difference_z = np.abs(expval1_z - expval2_z)
print(f"Absolute Difference of Paulit-Z: {absolute_difference_z:.4f}")