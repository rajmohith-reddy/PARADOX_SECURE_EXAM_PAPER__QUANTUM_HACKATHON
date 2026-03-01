# BB84 Quantum Key Distribution – IBM Quantum Composer Implementation
Amrita QuantumLeap Bootcamp 2026  
Theme: Quantum Cryptography  
---
## Overview
This repository contains the IBM Quantum Composer implementation of the BB84 Quantum Key Distribution protocol.
The goal of this implementation is to visually demonstrate how quantum mechanics enables secure key distribution and how eavesdropping introduces detectable disturbances in the quantum state.
This circuit-based implementation complements our full Python simulation and focuses specifically on visualizing:
- Alice encoding
- Eve interception (optional)
- Bob basis selection
- Measurement outcomes
- Bloch sphere state evolution
---
## Why IBM Quantum Composer?
While our main simulation is built using Qiskit, we used IBM Quantum Composer to:
- Visually construct the BB84 protocol
- Demonstrate state evolution on the Bloch sphere
- Show how basis changes affect quantum states
- Illustrate how measurement collapses the qubit state
- Present a clean, structured quantum circuit for the hackathon
This helps clearly explain the physics behind quantum key distribution.
---
## Protocol Representation
The circuit follows these stages:
1. **Alice Encoding**
   - Encodes classical bits using either Z or X basis.
   - Uses X gate for bit encoding.
   - Uses H gate for X-basis preparation.
2. **Eve Interception (Optional)**
   - Simulates intercept-resend attack.
   - Applies basis transformation.
   - Measurement collapses the quantum state.
3. **Bob Basis Selection**
   - Applies H gate if measuring in X basis.
   - Measures in computational basis.
4. **Measurement**
   - Final classical output.
   - Used to compute QBER in simulation layer.
---
## Bloch Sphere Demonstration
We used a single-qubit circuit to visualize state evolution.
Key observations:
- Superposition states appear on the equator of the Bloch sphere.
- Measuring in the wrong basis collapses the state to a pole.
- This collapse introduces disturbance.
- The disturbance leads to an increased Quantum Bit Error Rate (QBER).
This physical disturbance is what makes BB84 secure.
---
## What This Demonstrates
- Security based on quantum physics.
- No-cloning theorem in action.
- Measurement disturbance principle.
- Difference between clean channel and intercepted channel.
When Eve measures in the wrong basis, the Bloch sphere visibly collapses to a different state, showing how interception affects the qubit.
---
## Tools Used
- IBM Quantum Composer
- OpenQASM 2.0
- IBM Quantum Simulator
- Bloch Sphere / Q-sphere visualization
---
## How to Use
1. Open IBM Quantum Composer:
   https://quantum-computing.ibm.com
2. Switch to Code Editor mode.
3. Paste the provided OpenQASM code.
4. Click “Set up and run”.
5. Observe:
   - Circuit structure
   - Measurement histogram
   - Bloch sphere visualization
---
##Reference
Bennett, C. H., & Brassard, G. (1984).  
Quantum cryptography: Public key distribution and coin tossing.
---
“Quantum security is not based on computational difficulty — it is based on the fundamental laws of physics.”
