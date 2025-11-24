# HEC GitHub & Vercel Deployment Guide

## 📋 Pre-Deployment Checklist

✅ Old database files removed  
✅ .gitignore created  
✅ README.md added  
✅ vercel.json configured  
✅ Project cleaned up  

## 🚀 GitHub Upload

### 1. Initialize Git Repository

```bash
cd "c:/Users/theni/OneDrive/Desktop/Projects/Human Effort Coin"
git init
git add .
git commit -m "Initial commit: HEC Proof-of-Labor Economic Oracle"
```

### 2. Create GitHub Repository

1. Go to [GitHub](https://github.com/new)
2. Create new repository named `human-effort-coin`
3. **Do NOT** initialize with README (we already have one)

### 3. Push to GitHub

```bash
git remote add origin https://github.com/<YOUR_USERNAME>/human-effort-coin.git
git branch -M main
git push -u origin main
```

## 🌐 Vercel Deployment

### Option 1: Vercel CLI (Recommended)

```bash
cd hec-dashboard
npm install -g vercel
vercel login
vercel
```

### Option 2: Vercel Web Dashboard

1. Go to [Vercel Dashboard](https://vercel.com/new)
2. Import your GitHub repository
3. Framework Preset: **Vite**
4. Root Directory: `hec-dashboard`
5. Click **Deploy**

## ⚙️ Configuration

### Environment Variables

The frontend is currently hardcoded to use `http://127.0.0.1:8000` for the API.

**For production**, you'll need to:

1. **Option A: Run backend locally**
   - Users clone the repo
   - Run API and simulation locally
   - Frontend connects to localhost:8000

2. **Option B: Deploy backend separately** (Advanced)
   - Deploy backend to Railway/Render
   - Update `API_URL` in `hec-dashboard/src/App.jsx`
   - Migrate from SQLite to PostgreSQL

### Vercel Configuration

The `vercel.json` in `hec-dashboard/` handles:
- SPA routing (all routes → index.html)
- Build and output directories
- Framework detection

## 🔧 Post-Deployment

### Update README

Add your deployed URL to README.md:

```markdown
## 🌐 Live Demo

**Dashboard**: https://your-app.vercel.app

**Note**: Backend must be run locally. See installation instructions below.
```

### Test Deployment

1. Visit your Vercel URL
2. You'll see the dashboard (stats will show zeros)
3. To populate data:
   - Clone repo locally
   - Run backend + simulation
   - Dashboard will connect and show live data

## 📊 Current Deployment Model

```
┌─────────────────┐
│  Vercel Cloud   │  ← Frontend Only (Static)
│   (Dashboard)   │
└────────┬────────┘
         │
         │ API Calls (http://localhost:8000)
         │
         ▼
┌─────────────────┐
│  Local Machine  │  ← Backend + Simulation
│   (API + DB)    │
└─────────────────┘
```

## 🎯 Recommended Next Steps

1. **Deploy frontend** to Vercel
2. **Document local backend** setup in README
3. **Optional**: Create video demo showing the system
4. **Optional**: Migrate to cloud database for full cloud deployment

## 🛠️ Troubleshooting

### "API is not available"
- Ensure backend is running locally on port 8000
- Check CORS is enabled in `hec-core/api/main.py`

### Build fails on Vercel
- Verify `package.json` has all dependencies
- Check Node version compatibility (16+)

### Dashboard shows zeros
- Backend must be running
- Simulation must be started
- Click "Resume" button in dashboard

---

**Ready for GitHub and Vercel!** 🚀
