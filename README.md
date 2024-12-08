
# Quantum Programming Project - README

**Course**: EECE 435 - Introduction to Quantum Computing  
**Student**: Khaled Ammoura  
**Term**: Fall 2024-25  
**Due Date**: December 8, 2024  

---

## Overview

This repository contains the problem set and the corresponding solutions for the **Quantum Programming Project** assigned in EECE 435. The project involves implementing and analyzing various quantum algorithms using PennyLane, including investigations into quantum gates, GHZ state preparation, Deutsch’s and Deutsch-Jozsa algorithms, and optimizing quantum circuits.

---

## File Structure

1. **`Quantum Programming Project Description.pdf`**  
   - This document contains the detailed problem set, including instructions, tasks, and guidelines for the following exercises:
     - **Problem 1**: Order of Quantum Gates  
     - **Problem 2**: GHZ State Creation and Optimization  
     - **Problem 3**: Counting SWAP Gates for a CNOT Gate  
     - **Problem 4**: Deutsch’s Algorithm Implementation  
     - **Problem 5**: Deutsch-Jozsa Algorithm Implementation  
     - **Problem 6 (Bonus)**: Quantum Superdense Coding Using Bell Pairs  

2. **`Quantum Programming Project.pdf`**  
   - This document contains the detailed solutions and code implementations for the problems described in the problem set. It includes:
     - Quantum circuit diagrams  
     - Calculations of expectation values and probability distributions  
     - Explanations of results and answers to conceptual questions  

3. **`KhaledAmmoura_Project`**  
   - This file contains all the code implementations for the quantum programming project. The file archive includes:
     - Python scripts for each problem  
     - Sample outputs and verification code  

---

## Contents Overview

### Problem Summaries

1. **Problem 1: Order of Quantum Gates**  
   Investigates how the order of applying RX and RY gates affects measurement outcomes in the Pauli-X and Pauli-Z bases.

2. **Problem 2: GHZ State Creation and Optimization**  
   Implements quantum circuits to generate 3-qubit and 5-qubit GHZ states and compares circuit depth and gate count.

3. **Problem 3: Counting SWAP Gates**  
   Calculates the minimum number of SWAP gates needed to perform a CNOT operation on a hardware-limited architecture.

4. **Problem 4: Deutsch’s Algorithm**  
   Implements Deutsch’s algorithm to determine whether a function is constant or balanced with a single query.

5. **Problem 5: Deutsch-Jozsa Algorithm**  
   Extends Deutsch’s algorithm to n-bit functions, identifying if a function is constant or balanced.

6. **Bonus (Problem 6): Superdense Coding**  
   Implements the superdense coding protocol to transmit two classical bits using a single qubit and Bell states.

---

## Libraries Needed

To run the Quantum Programming Project, the following libraries are required:

1. **PennyLane**  
   - Quantum computing library for building and optimizing quantum circuits.  
   - **Installation**:  
     ```bash
     pip install pennylane
     ```

2. **NumPy**  
   - For numerical operations and matrix manipulations.  
   - **Installation**:  
     ```bash
     pip install numpy
     ```

3. **Matplotlib** (Optional)  
   - For visualizing quantum circuits and results.  
   - **Installation**:  
     ```bash
     pip install matplotlib
     ```

### Example `requirements.txt`

If you prefer to install all libraries at once, use the following `requirements.txt`:

```plaintext
pennylane
numpy
matplotlib
```

**Install Libraries Using `requirements.txt`**:  

```bash
pip install -r requirements.txt
```

### Verify Installation

To verify that the libraries are installed correctly, run:

```python
import pennylane as qml
import numpy as np
import matplotlib.pyplot as plt

print("Libraries installed successfully!")
```
