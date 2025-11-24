from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
import os

# Import will be updated to use PostgreSQL
try:
    from ..hec-core.database.models import SessionLocal, init_db
    from ..hec-core.api.routes import router
except:
    # Fallback for Vercel
    import sys
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'hec-core'))
    from database.models import SessionLocal, init_db
    from api.routes import router

app = FastAPI(title="HEC Overseer Node API", version="1.0.0")

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize database
@app.on_event("startup")
def startup():
    init_db()

# Include routes
app.include_router(router)

# Root endpoint
@app.get("/")
def root():
    return {"status": "HEC Overseer Node Online", "environment": "Vercel Serverless"}

# This is required for Vercel
handler = app
