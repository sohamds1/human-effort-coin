from sqlalchemy import create_engine, Column, String, Float, Integer, JSON, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
import datetime

SQLALCHEMY_DATABASE_URL = "sqlite:///./hec_world_v3.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    
    user_id = Column(String, primary_key=True, index=True) # UUID
    wallet_address = Column(String, unique=True, index=True)
    reputation_score = Column(Float, default=1.0)
    total_minted = Column(Float, default=0.0)
    skills = Column(JSON, default=list) # List of {"tag": str, "multiplier": float}
    status = Column(String, default="ACTIVE")

class Task(Base):
    __tablename__ = "tasks"
    
    task_id = Column(String, primary_key=True, index=True)
    creator_id = Column(String, index=True)
    type = Column(String) # e.g., "PHYSICAL_GARDENING"
    geo_fence = Column(JSON) # {"lat": float, "long": float, "radius_meters": int}
    required_evidence = Column(JSON) # ["GPS", "TIMELAPSE_VIDEO"]
    status = Column(String, default="OPEN")

class TaskSubmission(Base):
    __tablename__ = "task_submissions"
    
    submission_id = Column(String, primary_key=True, index=True)
    task_id = Column(String, ForeignKey("tasks.task_id"))
    worker_id = Column(String, ForeignKey("users.user_id"))
    
    time_start = Column(DateTime)
    time_end = Column(DateTime)
    duration_hours = Column(Float)
    
    telemetry_data = Column(JSON) # {"gps_log": "ipfs://...", "accelerometer_log": "ipfs://..."}
    proof_media = Column(JSON) # ["ipfs://QmVideoHash"]
    
    agent_verdict = Column(String, default="PENDING") # PENDING, APPROVED, REJECTED
    
    # Relationships
    worker = relationship("User")
    task = relationship("Task")

class SystemConfig(Base):
    __tablename__ = "system_config"
    key = Column(String, primary_key=True, index=True)
    value = Column(String) # Store as string, parse as needed

def init_db():
    Base.metadata.create_all(bind=engine)
    
    # Seed default config if not exists
    db = SessionLocal()
    if not db.query(SystemConfig).filter(SystemConfig.key == "simulation_active").first():
        db.add(SystemConfig(key="simulation_active", value="true"))
        db.commit()
    db.close()
