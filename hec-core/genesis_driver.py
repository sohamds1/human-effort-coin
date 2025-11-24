import time
import random
import uuid
import json
import sys
import os
import datetime

# Ensure we can import from the local folder
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from sqlalchemy.orm import Session
from sqlalchemy import func
from database.models import init_db, SessionLocal, User, TaskSubmission, Task, SystemConfig

# ==========================================
# 0. MOCK LEDGER
# ==========================================
class MockLedger:
    def mint_tokens(self, worker_address, hours, skill_multiplier=1):
        time.sleep(0.2) 
        return f"0x{uuid.uuid4().hex}"

# ==========================================
# 1. CONFIGURATION
# ==========================================
SYSTEM_TICK_RATE = 1.5
REPUTATION_PENALTY = 0.1

# ==========================================
# 2. THE AGENT BRAIN (Simulated)
# ==========================================
def query_hec_overseer(submission_data):
    print(f"\n[🧠 AGENT] Receiving Task {submission_data['task_id'][:8]}...")
    time.sleep(0.5) 

    vision_score = random.uniform(0.60, 0.99)
    is_fraud = random.random() < 0.05
    
    tools_detected = ["shovel", "gloves"] if submission_data['task_type'] == "GARDENING" else ["laptop", "vscode"]

    if is_fraud:
        verdict = "REJECT"
        reason = "ERR_REPLAY_ATTACK (Vector DB Match > 0.98)"
    elif vision_score < 0.80:
        verdict = "REJECT"
        reason = f"Visual Evidence Weak (Score: {vision_score:.2f})"
    else:
        verdict = "MINT"
        reason = "Metadata verified. Objects detected. Fraud check clean."

    return {
        "task_id": submission_data['task_id'],
        "final_action": verdict,
        "reasoning": reason,
        "vision_score": vision_score
    }

# ==========================================
# 3. WORLD SIMULATOR
# ==========================================
class WorldSim:
    def __init__(self):
        print("   > Connecting to Local DB...")
        self.db: Session = SessionLocal()
        print("   > Initializing Mock Ledger...")
        self.ledger = MockLedger()
        
    def generate_random_user(self):
        user_id = str(uuid.uuid4())
        wallet = f"0x{uuid.uuid4().hex[:40]}"
        user = User(
            user_id=user_id,
            wallet_address=wallet,
            reputation_score=1.0,
            total_minted=0.0,
            skills=[{"tag": "manual_labor", "multiplier": 1.0}],
            status="ACTIVE"
        )
        self.db.add(user)
        self.db.commit()
        return user

    def generate_task(self, user):
        task_types = ["GARDENING", "CODING", "CONSTRUCTION"]
        t_type = random.choice(task_types)
        hours = round(random.uniform(1.0, 5.0), 1)
        
        task_id = str(uuid.uuid4())
        
        # Create Task Record
        new_task = Task(
            task_id=task_id,
            creator_id=user.user_id,
            type=t_type,
            geo_fence={"lat": 34.05, "long": -118.24, "radius_meters": 50},
            required_evidence=["GPS", "TIMELAPSE_VIDEO"],
            status="OPEN"
        )
        self.db.add(new_task)
        self.db.commit()
        
        print(f"[🌍 WORLD] Worker {user.wallet_address[:6]}... submitting {hours}hrs of {t_type}")
        
        payload = {
            "task_id": task_id,
            "worker_id": user.user_id,
            "worker_wallet": user.wallet_address,
            "task_type": t_type,
            "hours_logged": hours,
            "gps": "34.05, -118.24",
            "media_url": f"ipfs://{uuid.uuid4().hex}"
        }
        return payload

    def execute_mint(self, wallet, hours, task_type):
        multipliers = {"GARDENING": 1.0, "CONSTRUCTION": 1.5, "CODING": 1.2}
        mult = multipliers.get(task_type, 1.0)
        
        print(f"[⛓️ LEDGER] Calling Smart Contract: Mint {hours} hrs @ {mult}x...")
        tx_hash = self.ledger.mint_tokens(wallet, hours, skill_multiplier=mult)
        print(f"[💰 SUCCESS] Tokens Minted. Tx: {tx_hash[:16]}...")

    def run_cycle(self):
        # 0. Check System Status
        config = self.db.query(SystemConfig).filter(SystemConfig.key == "simulation_active").first()
        if config and config.value == "false":
            print("[zzz] Simulation Paused...", end="\r")
            return

        # 1. Get User
        user = self.db.query(User).order_by(func.random()).first()
        if not user or random.random() < 0.3:
            user = self.generate_random_user()
            print(f"[+] New User Registered: {user.wallet_address[:8]}...")

        # 2. Generate Work
        task_data = self.generate_task(user)
        
        # 3. Agent Decides
        decision = query_hec_overseer(task_data)
        
        # 4. Actuation
        if decision['final_action'] == "MINT":
            print(f"[🤖 VERDICT] APPROVED. {decision['reasoning']}")
            self.execute_mint(
                task_data['worker_wallet'], 
                task_data['hours_logged'], 
                task_data['task_type']
            )
            user.total_minted += task_data['hours_logged'] # Simplified logic
            
            # Create Submission Record
            submission = TaskSubmission(
                submission_id=str(uuid.uuid4()),
                task_id=task_data['task_id'],
                worker_id=task_data['worker_id'],
                time_start=datetime.datetime.utcnow() - datetime.timedelta(hours=task_data['hours_logged']),
                time_end=datetime.datetime.utcnow(),
                duration_hours=task_data['hours_logged'],
                telemetry_data={"gps_log": task_data['gps']},
                proof_media=[task_data['media_url']],
                agent_verdict="APPROVED"
            )
            self.db.add(submission)
            
        else:
            print(f"[🛑 VERDICT] REJECTED. {decision['reasoning']}")
            user.reputation_score = round(max(0, user.reputation_score - REPUTATION_PENALTY), 2)
            print(f"[⚠️ PENALTY] User reputation slashed to {user.reputation_score}")
            
            # Create Submission Record
            submission = TaskSubmission(
                submission_id=str(uuid.uuid4()),
                task_id=task_data['task_id'],
                worker_id=task_data['worker_id'],
                time_start=datetime.datetime.utcnow() - datetime.timedelta(hours=task_data['hours_logged']),
                time_end=datetime.datetime.utcnow(),
                duration_hours=task_data['hours_logged'],
                telemetry_data={"gps_log": task_data['gps']},
                proof_media=[task_data['media_url']],
                agent_verdict="REJECTED"
            )
            self.db.add(submission)

        self.db.commit()

# ==========================================
# MAIN ENTRY POINT
# ==========================================
if __name__ == "__main__":
    print("\n=== INITIALIZING HEC OVERSEER NODE v1.0 (PHASE 2) ===")
    
    try:
        print("1. Checking Database Storage...")
        init_db()
        print("   ✅ Database Mounted.")
    except Exception as e:
        print(f"   ❌ Database Error: {e}")
        sys.exit(1)

    print("2. Booting Autonomous World Engine...")
    try:
        sim = WorldSim()
        print("   ✅ Engine Online.")
    except Exception as e:
        print(f"   ❌ Engine Failure: {e}")
        sys.exit(1)
        
    print("\n=== SYSTEM FULLY OPERATIONAL. LISTENING FOR TASKS ===\n")
    
    try:
        while True:
            sim.run_cycle()
            print("-" * 50)
            time.sleep(SYSTEM_TICK_RATE)
    except KeyboardInterrupt:
        print("\n[!] Manual Override. System Shutdown.")
