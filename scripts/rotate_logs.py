import os
import time
import shutil

def rotate_logs():
    backup_dir = "backups"
    if not os.path.exists(backup_dir):
        return
        
    now = time.time()
    cutoff = now - (30 * 86400) # 30 days retention
    
    for filename in os.listdir(backup_dir):
        filepath = os.path.join(backup_dir, filename)
        if os.path.isfile(filepath) and os.path.getmtime(filepath) < cutoff:
            os.remove(filepath)
            print(f"🧹 Cleaned old backup: {filename}")

if __name__ == "__main__":
    rotate_logs()
