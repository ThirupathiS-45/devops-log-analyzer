import time
from datetime import datetime
import random
import os
import pytz  # for timezone support

# Setup
log_levels = ["INFO", "WARNING", "ERROR", "DEBUG"]
messages = {
    "INFO": "System running smoothly",
    "WARNING": "Memory usage is high",
    "ERROR": "Database connection failed",
    "DEBUG": "Checking API response time"
}

log_file = "logs/app.log"
timezone = pytz.timezone("Asia/Kolkata")

# Ensure logs directory exists
os.makedirs("logs", exist_ok=True)

# 🚀 Reset log if it's a new day
if os.path.exists(log_file):
    with open(log_file, 'r') as f:
        first_line = f.readline()
        if first_line:
            old_date = first_line[1:11]  # Extract 'YYYY-MM-DD'
            today = datetime.now(timezone).strftime('%Y-%m-%d')
            if old_date != today:
                open(log_file, 'w').close()  # Clear log if date changed
        else:
            open(log_file, 'w').close()  # Empty file → reset

print("🚀 Simulating logs continuously...")

# 🔁 Continuous log simulation
while True:
    level = random.choice(log_levels)
    message = messages[level]
    timestamp = datetime.now(timezone).strftime('%Y-%m-%d %H:%M:%S')
    log_line = f"[{timestamp}] {level}: {message}\n"

    with open(log_file, "a") as f:
        f.write(log_line)

    print(f"📝 Written: {log_line.strip()}")
    time.sleep(random.randint(1, 3))  # simulate variable frequency
