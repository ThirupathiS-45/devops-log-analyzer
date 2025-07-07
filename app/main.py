import time
from datetime import datetime, timedelta
from preprocessor import parse_log_line
from log_reader import follow_log
from anomaly_detector import LogAnomalyDetector

# Config
LOG_PATH = "logs/app.log"
COLLECTION_WINDOW = 60  # seconds

# Initialize
log_buffer = []
detector = LogAnomalyDetector()
last_check = datetime.now()

print("🚀 Real-Time DevOps Log Analyzer Started...")

for line in follow_log(LOG_PATH):
    structured = parse_log_line(line)
    
    if structured['timestamp'] is not None:
        log_buffer.append(structured)

    # Check for anomalies every COLLECTION_WINDOW seconds
    if (datetime.now() - last_check).total_seconds() > COLLECTION_WINDOW:
        print("\n📊 Checking for anomalies...")
        if len(log_buffer) >= 5:  # enough data
            anomalies = detector.detect_anomalies(log_buffer)
            if anomalies.empty:
                print("✅ No anomalies detected.")
            else:
                print("🚨 Anomalies Detected:\n", anomalies)
        else:
            print("ℹ️ Not enough logs yet for detection.")
        
        last_check = datetime.now()
        # Optional: clear buffer or keep appending
        # log_buffer.clear()
