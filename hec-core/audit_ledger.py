from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from database.models import User, TaskSubmission

# Connect to the DB that just got populated
# Fixed: Using hec_world.db instead of hec.db
engine = create_engine("sqlite:///./hec_world.db")
Session = sessionmaker(bind=engine)
session = Session()

print("\n=== 📊 HEC ECONOMY AUDIT REPORT ===")

# 1. Total Supply
total_users = session.query(User).count()
total_hours = session.query(func.sum(User.total_hours)).scalar() or 0
print(f"👥 Total Citizens:      {total_users}")
print(f"⏱️  Total Verified Hours: {round(total_hours, 2)}")
print(f"💰 Global GDP (EC):      {round(total_hours, 2)} EC")

# 2. Acceptance Rate
# Note: TaskSubmission table might be empty if genesis_driver didn't save them. 
# Also checking if status column exists in model.
try:
    total_tasks = session.query(TaskSubmission).count()
    # If status column doesn't exist, this might fail or we need another way.
    # Assuming the user's provided code implies these were saved, but based on my analysis of genesis_driver, they might not be.
    # I will try to run it as requested.
    rejected_tasks = session.query(TaskSubmission).filter(TaskSubmission.status == "REJECTED").count()
    rejection_rate = round((rejected_tasks/total_tasks)*100, 1) if total_tasks > 0 else 0.0
    print(f"📉 Rejection Rate:      {rejection_rate}% ({rejected_tasks}/{total_tasks} tasks)")
except Exception as e:
    print(f"📉 Rejection Rate:      N/A (Error reading tasks: {e})")

# 3. Top Worker
top_worker = session.query(User).order_by(User.total_hours.desc()).first()
if top_worker:
    print(f"\n🏆 Top Worker: {top_worker.id[:10]}...")
    print(f"   Hours: {round(top_worker.total_hours, 2)}")
    print(f"   Rep:   {top_worker.reputation}")

print("===================================\n")
