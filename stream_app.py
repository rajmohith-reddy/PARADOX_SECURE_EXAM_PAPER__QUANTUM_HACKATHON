import streamlit as st
st.set_page_config(page_title="Quantum Exam Security", layout="wide")

import numpy as np
import matplotlib.pyplot as plt
from qiskit import QuantumCircuit, transpile
from qiskit_aer.noise import NoiseModel, depolarizing_error
from qiskit_aer import Aer
import random


# ---------------- Classical RSA Simulation ---------------

def rsa_simulation(intercept=False):
    symmetric_key = random.randint(1000, 9999)
    ciphertext = symmetric_key * 7 + 13

    attacker_copy = None
    if intercept:
        attacker_copy = ciphertext

    decrypted_key = (ciphertext - 13) // 7
    return symmetric_key, ciphertext, decrypted_key, attacker_copy


# ---------------------- BB84 CORE ------------------------

def generate_bits(n):
    return np.random.randint(2, size=n)

def generate_bases(n):
    return np.random.randint(2, size=n)

def eve_intercept(bits, bases):
    eve_bases = generate_bases(len(bits))
    corrupted = []
    for i in range(len(bits)):
        if eve_bases[i] == bases[i]:
            corrupted.append(bits[i])
        else:
            corrupted.append(np.random.randint(2))
    return corrupted

def create_noise_model(prob):
    noise_model = NoiseModel()
    error = depolarizing_error(prob, 1)
    noise_model.add_all_qubit_quantum_error(error, ['x', 'h'])
    return noise_model

def encode_qubits(bits, bases):
    circuits = []
    for i in range(len(bits)):
        qc = QuantumCircuit(1, 1)
        if bits[i] == 1:
            qc.x(0)
        if bases[i] == 1:
            qc.h(0)
        circuits.append(qc)
    return circuits

def measure_qubits(circuits, bob_bases, noise_model=None):
    simulator = Aer.get_backend('aer_simulator')
    measured = []
    for i in range(len(circuits)):
        qc = circuits[i].copy()
        if bob_bases[i] == 1:
            qc.h(0)
        qc.measure(0, 0)
        compiled = transpile(qc, simulator)

        if noise_model:
            result = simulator.run(compiled, noise_model=noise_model, shots=1).result()
        else:
            result = simulator.run(compiled, shots=1).result()

        counts = result.get_counts()
        measured.append(int(list(counts.keys())[0]))
    return measured

def sift_key(alice_bits, alice_bases, bob_bits, bob_bases):
    key_a, key_b = [], []
    for i in range(len(alice_bits)):
        if alice_bases[i] == bob_bases[i]:
            key_a.append(alice_bits[i])
            key_b.append(bob_bits[i])
    return key_a, key_b

def calculate_error(a, b):
    return sum(x != y for x, y in zip(a, b)) / len(a)

def run_bb84(n=100, eve=False, noise_prob=0):
    alice_bits = generate_bits(n)
    alice_bases = generate_bases(n)
    bob_bases = generate_bases(n)

    if eve:
        transmitted = eve_intercept(alice_bits, alice_bases)
    else:
        transmitted = alice_bits

    circuits = encode_qubits(transmitted, alice_bases)
    noise_model = create_noise_model(noise_prob) if noise_prob > 0 else None
    bob_bits = measure_qubits(circuits, bob_bases, noise_model)

    key_a, key_b = sift_key(alice_bits, alice_bases, bob_bits, bob_bases)
    return calculate_error(key_a, key_b)

# ------------------------- UI ----------------------------

st.title("🔐 Quantum-Optimized Exam Paper Security")
st.markdown("### Classical RSA vs Quantum BB84 Comparison")

st.markdown("---")

st.markdown("## 🔓 Classical RSA Key Exchange")

rsa_attack = st.checkbox("Simulate Interception (RSA)")

if st.button("Run RSA Simulation"):

    original, cipher, decrypted, attacker = rsa_simulation(rsa_attack)

    st.subheader("Key Exchange Flow")

    col1, col2, col3 = st.columns(3)

    col1.metric("Original Symmetric Key", original)
    col2.metric("Encrypted Ciphertext", cipher)
    col3.metric("Decrypted Key", decrypted)

    st.markdown("---")

    # Integrity Check
    if original == decrypted:
        st.success("Integrity Check: PASSED (Keys Match)")
    else:
        st.error("Integrity Check: FAILED")

    if rsa_attack:
        st.warning("👤 Interception Occurred During Transmission")
        st.info("⚠ System Status: No Detection Mechanism Triggered")

    else:
        st.info("No Interception Simulated")

    # Visual Comparison Graph
    fig, ax = plt.subplots()
    ax.bar(
        ["Original Key", "Decrypted Key"],
        [original, decrypted],
        color=["green", "green"]
    )
    ax.set_title("RSA Transmission Integrity (No Disturbance Detection)")
    st.pyplot(fig)

#------------BB84 SECTION ----------------

st.markdown("## 🔐 Proposed Quantum BB84 System")

col1, col2 = st.columns(2)

with col1:
    n = st.slider("Number of Qubits", 50, 200, 100)
    noise = st.slider("Noise Probability", 0.0, 0.3, 0.15)
    eve_attack = st.checkbox("Enable Eve (Quantum Eavesdropper)")
    run_quantum = st.button("Run BB84 Simulation")

with col2:
    st.info("""
    BB84 generates a secret key using quantum states.
    Any interception introduces measurable disturbance.
    Clean channel → ~0% error
    Eavesdropping → ~25% error
    """)
if run_quantum:

    st.markdown("---")
    st.subheader("Quantum Security Analysis")

    # Always compute clean channel (no noise, no Eve)
    clean_error = run_bb84(n=n, eve=False, noise_prob=0)

    # Noise-only scenario
    noise_error = run_bb84(n=n, eve=False, noise_prob=noise)

    # Eve scenario (only if enabled)
    if eve_attack:
        eve_error = run_bb84(n=n, eve=True, noise_prob=noise)
    else:
        eve_error = None

    # Display metrics
    colA, colB, colC = st.columns(3)
    colA.metric("Clean Error", f"{clean_error:.4f}")
    colB.metric("Noise Error", f"{noise_error:.4f}")

    if eve_attack:
        colC.metric("Eavesdropping Error", f"{eve_error:.4f}")

    threshold = 0.15

    # Detection Logic
    if eve_attack and eve_error > threshold:
        st.error("⚠ Eavesdropping Detected — Abort Key Exchange")
    elif noise_error > threshold:
        st.warning("⚠ High Channel Noise Detected")
    else:
        st.success("Secure Quantum Key Exchange")

    # Plot full comparison graph
    fig, ax = plt.subplots()

    labels = ["Clean", "Noise"]
    values = [clean_error, noise_error]
    colors = ["green", "orange"]

    if eve_attack:
        labels.append("Eve")
        values.append(eve_error)
        colors.append("red")

    ax.bar(labels, values, color=colors)
    ax.set_ylabel("Error Rate")
    ax.set_title("BB84 Disturbance Comparison")

    st.pyplot(fig)

st.markdown("---")
st.caption("Quantum Cryptography Hackathon Project | RSA vs BB84 Comparison")
