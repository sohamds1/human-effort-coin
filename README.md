# HumanEffortCoin (HEC) - Proof-of-Labor Economic Oracle

![Status](https://img.shields.io/badge/status-demo-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Python](https://img.shields.io/badge/python-3.9%2B-blue)
![React](https://img.shields.io/badge/react-18-61dafb)
![GitHub stars](https://img.shields.io/github/stars/sohamds1/human-effort-coin?style=social)
![GitHub forks](https://img.shields.io/github/forks/sohamds1/human-effort-coin?style=social)
![Python](https://img.shields.io/badge/python-3.9%2B-blue)
![React](https://img.shields.io/badge/react-18-61dafb)

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
11. [Deployment](#-deployment)
12. [Troubleshooting](#-troubleshooting)
13. [Contributing](#-contributing)
14. [License](#-license)

---

## 🎯 Overview

HumanEffortCoin is an **autonomous economic simulation** demonstrating how a currency can be backed by verified human labor instead of traditional commodities or fiat guarantees.

### What Makes HEC Unique?

- **Labor-Backed Currency**: Unlike Bitcoin (computational proof-of-work) or traditional fiat, HEC is backed by verified human time
- **AI Verification**: Simulated AI agent validates labor submissions (ready for real AI integration)
- **Real-time Economics**: Watch supply, demand, and GDP evolve autonomously
- **Zero Blockchain Dependency**: Currently runs on SQLite (easily upgradeable to blockchain)
- **Open Source**: Fork, customize, and build your own economic system

### Use Cases

- **Economic Research**: Study labor-backed currency models
- **Educational Tool**: Teach economic concepts with live simulations
- **Proof of Concept**: Demonstrate autonomous agent-based economics
- **Hackathon Project**: Ready-to-deploy full-stack application
- **Portfolio Piece**: Showcase full-stack + AI + economics expertise

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

### Verification Pipeline

```
1. Worker Submits Task
   ↓
2. Metadata Audit (GPS, time, type)
   ↓
3. AI Vision Analysis (proof media)
   ↓
4. Fraud Detection (duplicate check)
   ↓
5. Agent Verdict (APPROVE/REJECT)
   ↓
6. Token Minting or Reputation Penalty
```

### Anti-Fraud Mechanisms

| Mechanism | Purpose | Implementation |
|-----------|---------|----------------|
| **Max Daily Mint** | Prevent grinding | 12 EC per user per day |
| **Reputation System** | Penalize bad actors | Score decreases on rejection |
| **Fraud Vectoring** | Detect duplicates | Content-based similarity |
| **Circuit Breaker** | Prevent inflation attacks | Freeze at 2000 EC/hour |
| **Transaction Burn** | Deflationary pressure | 2% burn on all transactions |

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

### Data Flow Example

1. **User Registration**: `genesis_driver.py` creates a new user with wallet address
2. **Task Submission**: User submits task (type, hours, GPS, media URL)
3. **Agent Verification**: Mock AI agent scores the submission (0-1)
4. **Database Update**: Task stored with verdict
5. **Token Minting**: If approved, user balance increases
6. **Dashboard Update**: Frontend polls API every 2s and displays new data

---

## 🚀 Installation & Setup

### Prerequisites

| Software | Version | Purpose |
|----------|---------|---------|
| **Python** | 3.9+ | Backend API & Simulation |
| **Node.js** | 16+ | Frontend build & dev server |
| **npm** | 8+ | Package management |
| **Git** | Any | Version control (optional) |

### Step-by-Step Installation

#### 1. Clone or Download

```bash
# Option A: Clone with Git
git clone https://github.com/YOUR_USERNAME/human-effort-coin.git
cd human-effort-coin

# Option B: Download ZIP
# Extract to preferred location
cd path/to/human-effort-coin
```

#### 2. Install Python Dependencies

```bash
# Install required packages
pip install fastapi uvicorn sqlalchemy

# Verify installation
python -c "import fastapi; import uvicorn; import sqlalchemy; print('✓ All packages installed')"
```

#### 3. Install Frontend Dependencies

```bash
cd hec-dashboard
npm install

# Expected output: "added XXX packages"
```

#### 4. Verify Installation

```bash
# Check Python version
python --version  # Should be 3.9+

# Check Node version
node --version    # Should be 16+

# Check npm version
npm --version     # Should be 8+
```

### Running the System

You need **3 terminal windows** running simultaneously:

#### Terminal 1: API Server

```bash
cd hec-core
python -m uvicorn api.main:app --port 8000

# Expected output:
# INFO:     Uvicorn running on http://127.0.0.1:8000
# INFO:     Application startup complete.
```

**What it does:** Serves REST API endpoints for the dashboard

#### Terminal 2: Simulation Driver

```bash
# From project root
python hec-core/genesis_driver.py

# Expected output:
# Initializing HEC Autonomous Ecosystem...
# ✅ Database Mounted.
# ✅ Engine Online.
# === SYSTEM FULLY OPERATIONAL ===
```

**What it does:** Generates users, submits tasks, simulates economy

#### Terminal 3: Dashboard

```bash
cd hec-dashboard
npm run dev

# Expected output:
# VITE vX.X.X  ready in XXX ms
# ➜  Local:   http://localhost:5173/
```

**What it does:** Serves the React frontend

#### Access the Dashboard

Open your browser to: **http://localhost:5173**

You should see:
- Real-time stats (updating every 2 seconds)
- Live transaction feed
- Start/Stop control button

---

## 📁 Project Structure

```
human-effort-coin/
│
├── hec-core/                       # Backend (Python)
│   ├── api/                        # REST API
│   │   ├── __init__.py
│   │   ├── main.py                 # FastAPI app entry point
│   │   └── routes.py               # API endpoint definitions
│   │
│   ├── database/                   # Data layer
│   │   ├── __init__.py
│   │   └── models.py               # SQLAlchemy ORM models
│   │
│   ├── agent/                      # Mock AI agent
│   │   ├── __init__.py
│   │   └── blockchain.py           # Mock ledger/blockchain
│   │
│   └── genesis_driver.py           # Simulation engine
│
├── hec-dashboard/                  # Frontend (React)
│   ├── node_modules/               # NPM dependencies (gitignored)
│   ├── public/                     # Static assets
│   ├── src/
│   │   ├── App.jsx                 # Main React component
│   │   ├── App.css                 # Component styles (empty)
│   │   ├── index.css               # Global styles
│   │   └── main.jsx                # React entry point
│   │
│   ├── index.html                  # HTML template
│   ├── package.json                # NPM dependencies
│   ├── vite.config.js              # Vite configuration
│   └── vercel.json                 # Vercel deployment config
│
├── .gitignore                      # Git ignore rules
├── README.md                       # This file
├── DEPLOYMENT.md                   # Deployment guide
├── hec_protocol.md                 # Technical specification
├── start_hec.bat                   # Windows startup script
└── hec_world_v3.db                 # SQLite database (gitignored)
```

---

## 🔧 Backend Explained

### api/main.py - FastAPI Application

```python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api import routes

app = FastAPI(title="HEC Overseer Node API", version="1.0.0")

# CORS Configuration - allows frontend to connect
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify exact origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Database initialization
@app.on_event("startup")
def startup():
    from database.models import init_db
    init_db()  # Creates tables if they don't exist

# Register API routes
app.include_router(routes.router)

# Root endpoint
@app.get("/")
def root():
    return {"status": "HEC Overseer Node Online"}
```

**Customization Ideas:**
- Add authentication middleware
- Implement rate limiting
- Add logging/monitoring
- Switch to PostgreSQL

### api/routes.py - API Endpoints

| Endpoint | Method | Purpose | Request | Response |
|----------|--------|---------|---------|----------|
| `/` | GET | Health check | None | `{"status": "..."}` |
| `/stats` | GET | Economy stats | None | `{total_users, total_minted, total_tasks}` |
| `/feed` | GET | Recent tasks | `?limit=10` | Array of task objects |
| `/user/{wallet}` | GET | User profile | Wallet address | User object |
| `/submit_task` | POST | Submit new task | Task JSON | `{status, submission_id}` |
| `/simulation/start` | POST | Start simulation | None | `{status}` |
| `/simulation/stop` | POST | Stop simulation | None | `{status}` |
| `/simulation/status` | GET | Check if active | None | `{active: bool}` |

**Example Request:**

```bash
curl -X POST http://localhost:8000/submit_task \
  -H "Content-Type: application/json" \
  -d '{
    "worker_id": "0x123...",
    "task_type": "CODING",
    "hours": 3.5,
    "description": "Built authentication system"
  }'
```

### database/models.py - Database Schema

```python
# User Model
class User(Base):
    __tablename__ = "users"
    wallet_address = Column(String, primary_key=True)
    total_minted = Column(Float, default=0.0)
    reputation_score = Column(Float, default=1.0)
    skills = Column(JSON)  # {"CODING": 1.2, "GARDENING": 1.0}
    created_at = Column(DateTime)

# Task Model
class Task(Base):
    __tablename__ = "tasks"
    task_id = Column(String, primary_key=True)
    type = Column(String)  # CODING, GARDENING, CONSTRUCTION
    duration_hours = Column(Float)
    geo_fence = Column(JSON)  # {"lat": 37.7749, "lon": -122.4194}
    
# TaskSubmission Model
class TaskSubmission(Base):
    __tablename__ = "task_submissions"
    submission_id = Column(String, primary_key=True)
    worker_id = Column(String, ForeignKey("users.wallet_address"))
    task_id = Column(String, ForeignKey("tasks.task_id"))
    agent_verdict = Column(String)  # APPROVED, REJECTED
    time_start = Column(DateTime)
    time_end = Column(DateTime)
```

### genesis_driver.py - Simulation Engine

**What it does:**
1. Creates random users with wallet addresses
2. Generates tasks (GARDENING, CODING, CONSTRUCTION)
3. Simulates agent verification (random score 0.5-1.0)
4. Mints tokens for approved tasks
5. Penalizes reputation for rejected tasks

**Key Variables to Customize:**

```python
SYSTEM_TICK_RATE = 3  # Seconds between cycles (lower = faster simulation)

TASK_TYPES = [
    ("GARDENING", 1.0),     # (type, skill_multiplier)
    ("CODING", 1.2),
    ("CONSTRUCTION", 1.5)
]

APPROVAL_THRESHOLD = 0.7  # AI score needed to approve (0.0-1.0)

USER_GENERATION_RATE = 0.3  # Probability of new user per cycle
```

---

## 🎨 Frontend Explained

### App.jsx - Main Component

**State Management:**

```javascript
const [stats, setStats] = useState({
  total_users: 0,
  total_minted: 0,
  total_tasks: 0
})
const [feed, setFeed] = useState([])  // Array of transactions
const [simulationActive, setSimulationActive] = useState(true)
const [selectedTransaction, setSelectedTransaction] = useState(null)
```

**API Integration:**

```javascript
const API_URL = "http://127.0.0.1:8000"

const fetchData = async () => {
  const statsRes = await axios.get(`${API_URL}/stats`)
  const feedRes = await axios.get(`${API_URL}/feed?limit=20`)
  const statusRes = await axios.get(`${API_URL}/simulation/status`)
  
  setStats(statsRes.data)
  setFeed(feedRes.data)
  setSimulationActive(statusRes.data.active)
}

// Poll every 2 seconds
useEffect(() => {
  fetchData()
  const interval = setInterval(fetchData, 2000)
  return () => clearInterval(interval)
}, [])
```

### index.css - Skeuomorphic Design System

**Design Tokens:**

```css
:root {
  /* Colors */
  --bg-primary: #0a0a0f;
  --bg-card: #1a1a24;
  --accent-success: #10b981;
  --accent-error: #ef4444;
  
  /* Shadows */
  --shadow-sm: 0 2px 8px rgba(0, 0, 0, 0.4);
  --shadow-md: 0 4px 16px rgba(0, 0, 0, 0.5);
  --shadow-lg: 0 8px 32px rgba(0, 0, 0, 0.6);
}
```

**Component Styles:**

- **Cards**: Elevated with layered shadows, border glow on hover
- **Buttons**: Gradient backgrounds, transform on hover
- **Modal**: Backdrop blur, slide-up animation
- **Typography**: Gradient text for headers, monospace for IDs

---

## 🎨 Customization Guide

### Adding a New Task Type

#### 1. Update genesis_driver.py

```python
TASK_TYPES = [
    ("GARDENING", 1.0),
    ("CODING", 1.2),
    ("CONSTRUCTION", 1.5),
    ("TEACHING", 1.3),  # Add your new type
]
```

#### 2. Update App.jsx (add emoji)

```javascript
const getTaskIcon = (type) => {
  if (type === "GARDENING") return "🌱"
  if (type === "CODING") return "💻"
  if (type === "CONSTRUCTION") return "🏗️"
  if (type === "TEACHING") return "📚"  // Add emoji
  return "⚙️"
}
```

### Changing the Economic Formula

Edit `genesis_driver.py`:

```python
def calculate_mint_amount(self, hours, task_type, reputation):
    # Default formula:
    base = hours * TASK_TYPES[task_type]
    
    # Custom formula examples:
    
    # Example 1: Add time-of-day bonus
    hour = datetime.now().hour
    time_bonus = 1.2 if 9 <= hour <= 17 else 1.0
    
    # Example 2: Add experience multiplier
    submissions_count = get_user_submissions(worker_id)
    exp_bonus = min(1.5, 1.0 + (submissions_count * 0.01))
    
    return base * reputation * time_bonus * exp_bonus
```

### Adding New API Endpoints

Edit `hec-core/api/routes.py`:

```python
@router.get("/leaderboard")
def get_leaderboard(limit: int = 10, db: Session = Depends(get_db)):
    top_workers = (
        db.query(User)
        .order_by(User.total_minted.desc())
        .limit(limit)
        .all()
    )
    return [
        {
            "wallet": u.wallet_address,
            "minted": u.total_minted,
            "reputation": u.reputation_score
        }
        for u in top_workers
    ]
```

### Customizing the UI Theme

Edit `hec-dashboard/src/index.css`:

```css
/* Change to light theme */
:root {
  --bg-primary: #f9fafb;
  --bg-card: #ffffff;
  --text-primary: #1f2937;
  --border-subtle: rgba(0, 0, 0, 0.1);
}

/* Change accent color */
:root {
  --accent-primary: #8b5cf6;  /* Purple instead of indigo */
}
```

### Migrating to PostgreSQL

#### 1. Install psycopg2

```bash
pip install psycopg2-binary
```

#### 2. Update database/models.py

```python
# Replace this:
SQLALCHEMY_DATABASE_URL = "sqlite:///./hec_world_v3.db"

# With this:
SQLALCHEMY_DATABASE_URL = "postgresql://user:password@localhost/hec_db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
```

#### 3. Create PostgreSQL database

```sql
CREATE DATABASE hec_db;
CREATE USER hec_user WITH PASSWORD 'your_password';
GRANT ALL PRIVILEGES ON DATABASE hec_db TO hec_user;
```

---

## 📚 API Documentation

### GET /stats

**Description:** Returns global economy statistics

**Response:**
```json
{
  "total_users": 42,
  "total_minted": 327.5,
  "total_tasks": 89
}
```

### GET /feed?limit=10

**Description:** Returns recent task submissions

**Query Parameters:**
- `limit` (optional): Number of tasks to return (default: 10)

**Response:**
```json
[
  {
    "id": "a59115a3-eee2-420f-86b2-0a0e5aa5e510",
    "worker": "f0368745...",
    "type": "CODING",
    "hours": 2.8,
    "verdict": "APPROVED",
    "time": "2025-11-24T22:40:55.989523"
  }
]
```

### POST /submit_task

**Description:** Submit a new task for verification

**Request Body:**
```json
{
  "worker_id": "0x7c8a9b2e...",
  "task_type": "CODING",
  "hours": 3.5,
  "description": "Implemented authentication system",
  "proof_media": "https://example.com/photo.jpg",
  "geolocation": {"lat": 37.7749, "lon": -122.4194}
}
```

**Response:**
```json
{
  "status": "submitted",
  "submission_id": "cd242ae3-8f9a-4123..."
}
```

### POST /simulation/start

**Description:** Start the simulation driver

**Response:**
```json
{
  "status": "Simulation Started"
}
```

### GET /simulation/status

**Description:** Check if simulation is active

**Response:**
```json
{
  "active": true
}
```

---

## 🗄️ Database Schema

### Entity Relationship Diagram

```
┌─────────────┐
│    User     │
├─────────────┤
│ wallet_address (PK)
│ total_minted
│ reputation_score
│ skills
│ created_at
└─────────────┘
       │
       │ 1:N
       │
       ▼
┌─────────────────┐        ┌─────────────┐
│ TaskSubmission  │───────▶│    Task     │
├─────────────────┤   N:1  ├─────────────┤
│ submission_id (PK)        │ task_id (PK)
│ worker_id (FK)            │ type
│ task_id (FK)              │ duration_hours
│ agent_verdict             │ geo_fence
│ time_start                │ description
│ time_end                  └─────────────┘
└─────────────────┘

┌─────────────────┐
│ SystemConfig    │
├─────────────────┤
│ key (PK)
│ value
└─────────────────┘
```

### Table Descriptions

#### users
Stores worker profiles and reputation

| Column | Type | Description |
|--------|------|-------------|
| wallet_address | String (PK) | Unique blockchain address |
| total_minted | Float | Lifetime EC minted |
| reputation_score | Float | 0.0-1.0, affects minting |
| skills | JSON | Skill multipliers |
| created_at | DateTime | Registration timestamp |

#### tasks
Defines task metadata

| Column | Type | Description |
|--------|------|-------------|
| task_id | String (PK) | UUID |
| type | String | GARDENING, CODING, CONSTRUCTION |
| duration_hours | Float | Reported time spent |
| geo_fence | JSON | GPS coordinates |
| description | String | Task details |

#### task_submissions
Tracks verification results

| Column | Type | Description |
|--------|------|-------------|
| submission_id | String (PK) | UUID |
| worker_id | String (FK) | Links to users |
| task_id | String (FK) | Links to tasks |
| agent_verdict | String | APPROVED or REJECTED |
| time_start | DateTime | Task start time |
| time_end | DateTime | Task completion time |

#### system_config
Stores global settings

| Column | Type | Description |
|--------|------|-------------|
| key | String (PK) | Config name |
| value | String | Config value |

**Current Configs:**
- `simulation_active`: "true" or "false"

---

## 🚢 Deployment

See [DEPLOYMENT.md](DEPLOYMENT.md) for detailed deployment instructions.

### Quick Deploy to Vercel

```bash
cd hec-dashboard
npm install -g vercel
vercel login
vercel
```

**Note:** Backend must run locally or be deployed separately (Railway/Render recommended).

---

## 🔍 Troubleshooting

### Dashboard shows all zeros

**Cause:** Backend or simulation not running

**Solution:**
1. Verify API is running: `curl http://localhost:8000`
2. Check simulation: Look for output in genesis_driver terminal
3. Click "Resume" button if simulation is paused

### "Module not found" errors

**Cause:** Missing Python dependencies

**Solution:**
```bash
pip install fastapi uvicorn sqlalchemy
```

### Port 8000 already in use

**Cause:** Previous API instance still running

**Solution:**
```bash
# Windows
taskkill /F /IM python.exe

# Mac/Linux
pkill python
```

### Frontend build fails

**Cause:** Node version incompatibility

**Solution:**
```bash
# Check Node version
node --version  # Should be 16+

# Upgrade Node if needed
# Use nvm (Node Version Manager)
```

### Database locked error

**Cause:** Multiple processes accessing SQLite

**Solution:**
1. Stop all Python processes
2. Delete `hec_world_v3.db`
3. Restart API (will recreate database)

---

## 🤝 Contributing

We welcome contributions! Here's how to get started:

### 1. Fork the Repository

Click "Fork" on GitHub to create your copy.

### 2. Create a Branch

```bash
git checkout -b feature/your-feature-name
```

### 3. Make Changes

- Follow existing code style
- Add comments for complex logic
- Test thoroughly locally

### 4. Commit with Descriptive Messages

```bash
git commit -m "feat: Add leaderboard API endpoint"
git commit -m "fix: Resolve database locking issue"
git commit -m "docs: Update README with PostgreSQL migration"
```

### 5. Push and Create Pull Request

```bash
git push origin feature/your-feature-name
```

Then create a PR on GitHub with:
- Clear description of changes
- Screenshots (if UI changes)
- Testing steps

### Contribution Ideas

- [ ] Add chart visualization (GDP over time)
- [ ] Implement user authentication
- [ ] Create mobile app (React Native)
- [ ] Add real AI vision model integration
- [ ] Build dispute resolution system
- [ ] Migrate to PostgreSQL
- [ ] Add comprehensive testing
- [ ] Create admin dashboard
- [ ] Implement WebSocket for real-time updates
- [ ] Add i18n (internationalization)

---

## 📜 License

MIT License

Copyright (c) 2025 HumanEffortCoin Contributors

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

---

## 🙏 Acknowledgments

- **Economics**: Inspired by labor theory of value and proof-of-work
- **Design**: Skeuomorphic minimalism trend in modern UI
- **Tech Stack**: FastAPI, React, SQLAlchemy communities
- **Concept**: Built as a demonstration of autonomous economic systems

---

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/YOUR_USERNAME/human-effort-coin/issues)
- **Discussions**: [GitHub Discussions](https://github.com/YOUR_USERNAME/human-effort-coin/discussions)
- **Email**: your-email@example.com

---

**⚡ Built with HEC - Powering the Future of Labor-Backed Economics**
