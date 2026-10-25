import shutil
import datetime
import os

def backup_database():
    db_file = "trading_agent.db"
    if not os.path.exists(db_file):
        print("No database found to backup.")
        return
        
    backup_dir = "backups"
    os.makedirs(backup_dir, exist_ok=True)
    
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = os.path.join(backup_dir, f"trading_agent_{timestamp}.db")
    
    shutil.copy(db_file, backup_path)
    print(f"✅ Database successfully backed up to {backup_path}")

if __name__ == "__main__":
    backup_database()
