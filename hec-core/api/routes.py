from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import func
from database.models import SessionLocal, User, TaskSubmission, Task, SystemConfig
from pydantic import BaseModel
from typing import List, Optional
import uuid
import datetime

router = APIRouter()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Pydantic Models
class TaskSubmissionCreate(BaseModel):
    worker_id: str
    task_type: str
    hours_logged: float
    gps_logs: str
    media_url: str

class UserResponse(BaseModel):
    user_id: str
    wallet_address: str
    reputation_score: float
    total_minted: float
    status: str

# Routes
@router.post("/submit_task")
def submit_task(submission: TaskSubmissionCreate, db: Session = Depends(get_db)):
    # 1. Find or Create User (Mock Logic for now)
    user = db.query(User).filter(User.user_id == submission.worker_id).first()
    if not user:
        # In a real app, user creation would be separate. 
        # Here we auto-create for simulation flow if needed, or error.
        raise HTTPException(status_code=404, detail="User not found")

    # 2. Create Task Record (Implicitly)
    # In Blueprint, Task exists first. For now, we simulate a task being created or found.
    task_id = str(uuid.uuid4())
    new_task = Task(
        task_id=task_id,
        creator_id=submission.worker_id, # Self-assigned for now
        type=submission.task_type,
        geo_fence={"lat": 0.0, "long": 0.0, "radius": 100}, # Mock
        required_evidence=["GPS"],
        status="OPEN"
    )
    db.add(new_task)
    db.commit()

    # 3. Create Submission
    new_submission = TaskSubmission(
        submission_id=str(uuid.uuid4()),
        task_id=task_id,
        worker_id=submission.worker_id,
        time_start=datetime.datetime.utcnow() - datetime.timedelta(hours=submission.hours_logged),
        time_end=datetime.datetime.utcnow(),
        duration_hours=submission.hours_logged,
        telemetry_data={"gps_log": submission.gps_logs},
        proof_media=[submission.media_url],
        agent_verdict="PENDING"
    )
    db.add(new_submission)
    db.commit()
    
    return {"status": "submitted", "submission_id": new_submission.submission_id}

@router.get("/user/{wallet_address}", response_model=UserResponse)
def get_user(wallet_address: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.wallet_address == wallet_address).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.get("/stats")
def get_stats(db: Session = Depends(get_db)):
    total_users = db.query(User).count()
    total_minted = db.query(func.sum(User.total_minted)).scalar() or 0.0
    total_tasks = db.query(Task).count()
    return {
        "total_users": total_users,
        "total_minted": round(total_minted, 2),
        "total_tasks": total_tasks
    }

@router.get("/feed")
def get_feed(limit: int = 10, db: Session = Depends(get_db)):
    # Get recent submissions with worker details
    submissions = db.query(TaskSubmission).order_by(TaskSubmission.time_end.desc()).limit(limit).all()
    feed = []
    for sub in submissions:
        feed.append({
            "id": sub.submission_id,
            "worker": sub.worker_id[:8] + "...",
            "type": sub.task.type if sub.task else "UNKNOWN",
            "hours": sub.duration_hours,
            "verdict": sub.agent_verdict,
            "time": sub.time_end.isoformat()
        })
    return feed

@router.post("/simulation/start")
def start_simulation(db: Session = Depends(get_db)):
    config = db.query(SystemConfig).filter(SystemConfig.key == "simulation_active").first()
    if not config:
        config = SystemConfig(key="simulation_active", value="true")
        db.add(config)
    else:
        config.value = "true"
    db.commit()
    return {"status": "Simulation Started"}

@router.post("/simulation/stop")
def stop_simulation(db: Session = Depends(get_db)):
    config = db.query(SystemConfig).filter(SystemConfig.key == "simulation_active").first()
    if not config:
        config = SystemConfig(key="simulation_active", value="false")
        db.add(config)
    else:
        config.value = "false"
    db.commit()
    return {"status": "Simulation Stopped"}

@router.get("/simulation/status")
def get_simulation_status(db: Session = Depends(get_db)):
    config = db.query(SystemConfig).filter(SystemConfig.key == "simulation_active").first()
    is_active = config.value == "true" if config else True
    return {"active": is_active}
