# HumanEffortCoin (HEC) - Proof-of-Labor Economic Oracle

![Status](https://img.shields.io/badge/status-demo-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Python](https://img.shields.io/badge/python-3.9%2B-blue)
![React](https://img.shields.io/badge/react-18-61dafb)
![GitHub stars](https://img.shields.io/github/stars/sohamds1/human-effort-coin?style=social)
![GitHub forks](https://img.shields.io/github/forks/sohamds1/human-effort-coin?style=social)

A decentralized economic protocol where **1 EffortCoin (EC) = 1 Verified Hour of Human Labor**. HEC introduces Proof-of-Labor (PoL) as a novel consensus mechanism, minting currency based on verified, useful human time expenditure.

---

## 📑 Table of Contents

1. [Overview](#-overview)
2. [Core Concept](#-core-concept)
3. [Architecture Deep Dive](#-architecture-deep-dive)
4. [Installation & Setup](#-installation--setup)
5. [Project Structure](#-project-structure)
6. [Backend Explained](#-backend-explained)
7. [Frontend Explained](#-frontend-explained)
8. [Customization Guide](#-customization-guide)
9. [API Documentation](#-api-documentation)
10. [Database Schema](#-database-schema)
11. [Troubleshooting](#-troubleshooting)
12. [Contributing](#-contributing)
13. [License](#-license)

---

## 🎯 Overview

HumanEffortCoin is an **autonomous economic simulation** demonstrating how a currency can be backed by verified human labor instead of traditional commodities or fiat guarantees.

### What Makes HEC Unique?

- **Labor-Backed Currency**: Unlike Bitcoin (computational proof-of-work) or traditional fiat, HEC is backed by verified human time
- **AI Verification**: Simulated AI agent validates labor submissions (ready for real AI integration)
- **Real-time Economics**: Watch supply, demand, and GDP evolve autonomously
- **Zero Blockchain Dependency**: Currently runs on SQLite (easily upgradeable to blockchain)
- **Open Source**: Fork, customize, and build your own economic system

---

## 💡 Core Concept

### The Economic Formula

```
Tokens Minted = Hours_Logged × Skill_Multiplier × Reputation_Score
```

**Example:**
- Worker submits 2.5 hours of coding
- Skill multiplier for coding: 1.2x
- Worker reputation: 0.95 (good standing)
- **Tokens minted**: 2.5 × 1.2 × 0.95 = **2.85 EC**

---

## 🏗️ Architecture Deep Dive

### System Components

```
┌─────────────────────────────────────────────────────────┐
│                    HEC ECOSYSTEM                        │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  ┌─────────────┐    ┌─────────────┐    ┌───────────┐  │
│  │   Frontend  │───▶│  REST API   │───▶│  Database │  │
│  │   (React)   │    │  (FastAPI)  │    │  (SQLite) │  │
│  └─────────────┘    └─────────────┘    └───────────┘  │
│         │                   │                   │      │
│         │                   ▼                   │      │
│         │           ┌─────────────┐            │      │
│         └──────────▶│  Genesis    │────────────┘      │
│                     │  Driver     │                    │
│                     │ (Simulator) │                    │
│                     └─────────────┘                    │
│                            │                           │
│                            ▼                           │
│                     ┌─────────────┐                    │
│                     │ Mock Agent  │                    │
│                     │  (AI Sim)   │                    │
│                     └─────────────┘                    │
└─────────────────────────────────────────────────────────┘
```

---

## 🚀 Installation & Setup

### Prerequisites

| Software | Version | Purpose |
|----------|---------|---------|
| **Python** | 3.9+ | Backend API & Simulation |
| **Node.js** | 16+ | Frontend build & dev server |
| **npm** | 8+ | Package management |

### Step-by-Step Installation

#### 1. Clone the Repository

```bash
git clone https://github.com/sohamds1/human-effort-coin.git
cd human-effort-coin
```

#### 2. Install Python Dependencies

```bash
pip install fastapi uvicorn sqlalchemy
```

#### 3. Install Frontend Dependencies

```bash
cd hec-dashboard
npm install
cd ..
```

### Running the System

You need **3 terminal windows** running simultaneously:

#### Terminal 1: API Server

```bash
cd hec-core
python -m uvicorn api.main:app --port 8000
```

#### Terminal 2: Simulation Driver

```bash
python hec-core/genesis_driver.py
```

#### Terminal 3: Dashboard

```bash
cd hec-dashboard
npm run dev
```

#### Access the Dashboard

Open your browser to: **http://localhost:5173**

---

## 📁 Project Structure

```
human-effort-coin/
│
├── hec-core/                       # Backend (Python)
│   ├── api/                        # REST API
│   │   ├── main.py                 # FastAPI app entry point
│   │   └── routes.py               # API endpoint definitions
│   ├── database/                   # Data layer
│   │   └── models.py               # SQLAlchemy ORM models
│   ├── agent/                      # Mock AI agent
│   └── genesis_driver.py           # Simulation engine
│
├── hec-dashboard/                  # Frontend (React)
│   ├── src/
│   │   ├── App.jsx                 # Main React component
│   │   └── index.css               # Global styles
│   └── package.json
│
├── .gitignore                      # Git ignore rules
├── README.md                       # This file
├── hec_protocol.md                 # Technical specification
├── start_hec.bat                   # Windows startup script
└── hec_world_v3.db                 # SQLite database (gitignored)
```

---

## 🔧 Backend Explained

### api/main.py - FastAPI Application

The backend serves as the gateway for the frontend and simulation driver. It uses FastAPI for high performance and easy API definition.

### database/models.py - Database Schema

We use SQLAlchemy with SQLite for a lightweight, portable database. The schema includes Users, Tasks, TaskSubmissions, and SystemConfig.

### genesis_driver.py - Simulation Engine

This script simulates the "world" by generating random users, creating tasks, and simulating the AI verification process. It's the engine that makes the dashboard come alive.

---

## 🎨 Frontend Explained

The frontend is built with React and Vite. It uses a **Skeuomorphic Minimalism** design language with dark mode, gradients, and depth effects. It polls the API every 2 seconds to provide a real-time experience.

---

## 🤝 Contributing

We welcome contributions! Please fork the repository and submit a pull request.

---

## 📜 License

MIT License - See LICENSE file for details.
