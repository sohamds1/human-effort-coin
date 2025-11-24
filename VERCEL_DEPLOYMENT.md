# HEC Vercel Deployment Guide

## 🚀 Full Stack Deployment to Vercel

Your HEC project is now configured for complete Vercel deployment (frontend + backend)!

### Prerequisites

1. Vercel account (free tier works)
2. GitHub repository (already done ✅)

### Step 1: Create Vercel Postgres Database

1. Go to https://vercel.com/dashboard
2. Click "Storage" → "Create Database"
3. Select "Postgres"
4. Choose a name: `hec-database`
5. Select region closest to you
6. Click "Create"

### Step 2: Get Database Connection String

1. In your Postgres database dashboard
2. Go to ".env.local" tab
3. Copy the `POSTGRES_URL` value
4. It looks like: `postgres://default:xxx@xxx-pooler.aws.neon.tech:5432/verceldb`

### Step 3: Deploy to Vercel

**Option A: Vercel CLI**
```bash
cd "c:/Users/theni/OneDrive/Desktop/Projects/Human Effort Coin"
vercel
```

**Option B: Vercel Dashboard**
1. Go to https://vercel.com/new
2. Import `sohamds1/human-effort-coin`
3. **Root Directory:** leave as root (not hec-dashboard)
4. Framework: Detected automatically
5. Click "Deploy"

### Step 4: Add Environment Variable

After deployment:
1. Go to your project settings
2. Navigate to "Environment Variables"
3. Add variable:
   - Name: `DATABASE_URL`
   - Value: Your `POSTGRES_URL` from Step 2
4. Click "Save"
5. Redeploy the project (Deployments → click "..." → Redeploy)

### Step 5: Initialize Database

Run the simulation locally to populate the cloud database:

```bash
# Update DATABASE_URL in your local .env
echo "DATABASE_URL=your_postgres_url_here" > .env

# Run simulation
python hec-core/genesis_driver.py
```

The simulation will now populate the Vercel Postgres database!

## 🎯 Architecture

```
┌────────────────────────────────┐
│     Vercel Deployment          │
├────────────────────────────────┤
│                                │
│  Frontend (React)              │
│  https://your-app.vercel.app   │
│           ↓                     │
│  API (/api/*)                  │
│  Serverless Functions          │
│           ↓                     │
│  Vercel Postgres               │
│  Cloud Database                │
│                                │
└────────────────────────────────┘
         ↑
         │ (writes data)
Local Simulation
(your computer)
```

## 📝 What Changed

### Backend
- ✅ PostgreSQL support added
- ✅ Environment variable configuration
- ✅ Vercel serverless entry point (`api/index.py`)
- ✅ Python requirements file

### Frontend
- ✅ Dynamic API URL (works locally and on Vercel)
- ✅ Production build configuration

### Configuration
- ✅ Root `vercel.json` for monorepo
- ✅ Database connection with fallback

## 🔧 Local Development

You can still develop locally:

```bash
# Without cloud database (SQLite)
python hec-core/genesis_driver.py

# With cloud database (PostgreSQL)
export DATABASE_URL="your_postgres_url"
python hec-core/genesis_driver.py
```

## ✅ Verification

After deployment:
1. Visit your Vercel URL
2. Dashboard should load (may show zeros initially)
3. Run simulation locally to populate data
4. Dashboard will update in real-time!

## 🎉 Result

- ✅ Frontend hosted on Vercel
- ✅ API hosted on Vercel (serverless)
- ✅ Database hosted on Vercel
- ✅ Fully cloud-deployed system!

---

**Your HEC system is production-ready!** 🚀
