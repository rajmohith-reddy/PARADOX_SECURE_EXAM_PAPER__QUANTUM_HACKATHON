# PARADOX_SECURE_EXAM_PAPER__QUANTUM_HACKATHON

# Quantum-Optimized Exam Paper Security Using BB84

Amrita QuantumLeap Bootcamp 2026  
Theme: Quantum Cryptography  
---
##Why We Built This
In most academic institutions, exam papers are transmitted digitally before exams.  
Today, this transmission typically relies on:
- RSA (for key exchange)
- AES (for encryption)
- HTTPS / VPN-based secure transfer
These systems are secure *for now*, but they depend on mathematical hardness assumptions.  
With the rise of quantum computing, algorithms like **Shor’s algorithm** threaten RSA-based systems.
This made us think:
>> What if someone intercepts an exam paper key?  
>> How would the system even know?
# Current classical systems do not have built-in intrusion detection at the key distribution level.
- So instead of replacing classical security, we decided to **strengthen it using quantum-aware key distribution.**
---
##Our Idea
We implemented the **BB84 Quantum Key Distribution protocol**, originally proposed by Bennett and Brassard (1984).
The goal is simple:
1. Use quantum mechanics to securely generate a shared key.
2. Detect any interception attempt using Quantum Bit Error Rate (QBER).
3. Use the generated quantum-safe key for AES encryption of exam papers.
This creates a hybrid security model:
- Quantum-based key generation  
- Classical AES encryption for file security  
---
##How It Works
1. Alice (Exam Authority) generates random bits.
2. She encodes them using random quantum bases (Z or X).
3. Qubits are transmitted through a simulated channel.
4. Bob (University Server) measures them using random bases.
5. Matching bases are kept (key sifting).
6. QBER is calculated.
If:
- QBER is low → secure communication
- QBER is high → intrusion detected
We also simulate:
- Intercept-resend attack (Eve)
- Depolarizing quantum noise
---
##Tools Used
- Python
- Qiskit
- Qiskit Aer Simulator
- NumPy
- Matplotlib
- IBM Quantum Composer (for circuit visualization)
---
##What We Observed
| Scenario          | QBER       |
|-------------------|------------|
| Clean Channel     | ~0.01      |
| With Eavesdropper | ~0.25      |
| Noise (5%)        | ~0.05–0.10 |

---

Key Insight:
- Eavesdropping introduces ~25% error due to measurement disturbance.
- Noise increases error gradually.
- A threshold can distinguish attack from natural noise.
This gives us **built-in intrusion detection**, which classical systems lack.
---
##Why This Matters
Classical systems:
- Secure today
- Vulnerable to future quantum attacks
- No intrinsic eavesdropping detection
Quantum BB84:
- Security based on physics, not math assumptions
- Measurement collapse reveals interception
- No-cloning theorem prevents copying qubits
This makes the system future-ready.
---
Hybrid Model
Quantum Key Distribution (BB84)  
            ⬇  
    Generated Secure Key  
            ⬇  
  AES Encryption of Exam Paper  
            ⬇  
      Secure Transmission  
Here, We are not replacing AES or classical encryption.  
We are strengthening the key generation layer.
---
## Future Improvements
- Test on real IBM Quantum hardware
- Add privacy amplification
- Integrate quantum error correction
- Extend to full campus communication system
- Compare with post-quantum cryptographic methods
---
## Installation

Clone the repository:
```
git clone https://github.com/your-username/quantum-exam-security-bb84.git
cd quantum-exam-security-bb84
```
Create virtual environment:
```
python3 -m venv venv
source venv/bin/activate
```
Install dependencies:
```
pip install -r requirements.txt
```
Run:
```
python quantum_exam_security.py
```
## Reference
Bennett, C. H., & Brassard, G. (1984).
Quantum cryptography: Public key distribution and coin tossing.

## “Combining physics-based security with practical encryption strengthens institutional data protection.”
---
