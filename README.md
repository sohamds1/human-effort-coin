# HumanEffortCoin (HEC) - The Proof-of-Labor Protocol

![Status](https://img.shields.io/badge/status-experimental-orange)
![License](https://img.shields.io/badge/license-MIT-green)
![Concept](https://img.shields.io/badge/concept-proof--of--labor-blue)

> **"What if money wasn't backed by gold, government decrees, or wasted electricity—but by the sweat of your brow?"**

HumanEffortCoin (HEC) is an experimental economic protocol and simulation that explores a radical question: **Can we tokenize human time itself?**

This repository contains a fully functional **Economic Oracle & Simulation** that demonstrates this concept in action. It is not just code; it is a provocation.

---

## 📑 Table of Contents

1. [🧠 The Philosophy: Proof-of-Labor](#-the-philosophy-proof-of-labor)
2. [⚠️ The Dystopian Reality & Risks](#-the-dystopian-reality--risks)
3. [🏗️ How This Project Implements It](#-how-this-project-implements-it)
4. [🚀 Quick Start Simulation](#-quick-start-simulation)
5. [🛠️ Technical Architecture](#-technical-architecture)
6. [🔮 Future Workarounds (ZK-Proofs)](#-future-workarounds-zk-proofs)

---

## 🧠 The Philosophy: Proof-of-Labor

### The Problem with Current Money
*   **Fiat Currency**: Backed by government trust, prone to inflation.
*   **Gold**: Backed by scarcity, hard to transport/divide.
*   **Bitcoin (Proof-of-Work)**: Backed by *computational* energy expenditure. It proves you wasted electricity to solve a puzzle.
*   **Ethereum (Proof-of-Stake)**: Backed by capital. Money makes more money.

### The HEC Solution
HEC proposes **Proof-of-Labor (PoL)**. The fundamental unit of value is the **Verified Human Hour**.

If a currency is backed by human time—the one resource that is finite for every human regardless of status—it creates an intrinsically egalitarian economy. 1 Hour of a CEO's time = 1 Hour of a Janitor's time (in the purest sense of time scarcity).

**The Formula:**
```
Minted HEC = (Time_Spent) × (Skill_Complexity_Multiplier) × (Quality_Score)
```

In this system, you don't "mine" coins with a GPU. You "mine" coins by **doing things**: planting trees, writing code, cleaning streets, or learning a new language.

---

## ⚠️ The Dystopian Reality & Risks

While the ideal is noble, implementing this in the real world faces terrifying challenges. This project serves as a simulation to study these failure points.

### 1. The Oracle Problem (The "Black Mirror" Factor)
**The Challenge:** How does a digital blockchain know you *actually* cleaned the street?
**The Failure Mode:** It requires total surveillance. To verify labor, the system needs GPS data, heart rate monitors, camera feeds, and constant telemetry.
**The Risk:** This creates a "panopticon" economy where privacy is traded for income.

### 2. The "Gamification" of Existence
**The Challenge:** If every action has a monetary value, intrinsic motivation dies.
**The Failure Mode:** People stop doing good deeds because "it's the right thing to do" and start doing them only "if the bounty is high enough."
**The Risk:** A hyper-capitalist nightmare where a mother asks for payment to care for her child because it's "Care Labor."

### 3. AI Bias in Verification
**The Challenge:** The "Verifier" is an AI Agent (as simulated in this project).
**The Failure Mode:** If the AI is trained on biased data, it might reject the labor of certain demographics or fail to recognize non-standard forms of work.
**The Risk:** Systemic economic exclusion hard-coded into the currency itself.

---

## 🏗️ How This Project Implements It

This codebase is a **Simulation of the Protocol**. It does not solve the Oracle Problem but assumes a "Perfect Oracle" to study the economic effects.

### 1. The "World Engine" (`hec-core/genesis_driver.py`)
This script acts as the **God Mode**. It:
*   Generates synthetic users (Workers).
*   Simulates them performing tasks (e.g., "Gardening", "Coding").
*   Generates "Evidence" (Mock GPS logs, image hashes).

### 2. The "Overseer" (`hec-core/agent/blockchain.py`)
This is the **AI Oracle**. It:
*   Receives the evidence.
*   "Verifies" it (in this sim, it checks probability and metadata).
*   Decides whether to Mint or Reject.

### 3. The "Ledger" (SQLite Database)
Unlike a blockchain, we use a simple SQL database for this prototype to track:
*   `Users`: The workers.
*   `TaskSubmissions`: The labor performed.
*   `SystemConfig`: The global economic parameters.

### 4. The "Interface" (React Dashboard)
The frontend visualizes this invisible economy, showing the flow of human effort turning into digital value.

---

## 🚀 Quick Start Simulation

Want to watch this economy run on your machine?

### Prerequisites
*   Python 3.9+
*   Node.js 16+

### 1. Clone & Install
```bash
git clone https://github.com/sohamds1/human-effort-coin.git
cd human-effort-coin

# Backend
pip install fastapi uvicorn sqlalchemy

# Frontend
cd hec-dashboard
npm install
```

### 2. Run the "Trinity"
Open **3 Terminal Windows**:

**Terminal 1 (The API):**
```bash
cd hec-core
python -m uvicorn api.main:app --port 8000 --reload
```

**Terminal 2 (The Simulation):**
```bash
# Windows
$env:PYTHONIOENCODING='utf-8'
python hec-core/genesis_driver.py
```

**Terminal 3 (The Dashboard):**
```bash
cd hec-dashboard
npm run dev
```

Visit **http://localhost:5173** to watch the economy evolve.

---

## 🔮 Future Workarounds (ZK-Proofs)

How do we solve the Dystopian Surveillance problem?

The theoretical solution (not implemented here) is **Zero-Knowledge Proofs (ZKPs)**.
*   **Concept:** A user proves they did the work *without* revealing the raw data.
*   **Example:** Your phone proves you walked 5 miles using accelerometer data, but *does not* reveal your GPS location history to the network.
*   **Hardware Oracles:** Trusted Enclave hardware (like Apple's Secure Enclave) signs the data locally. The network trusts the signature, not the raw video feed.

This project is the first step: **Proving the Economy works.**
The next step is **Proving the Privacy works.**

---

## 📜 License

MIT License. Fork it. Fix it. Break it.
