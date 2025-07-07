import time
from preprocessor import parse_log_line

def follow_log(file_path):
    with open(file_path, "r") as file:
        file.seek(0, 2)
        while True:
            line = file.readline()
            if not line:
                time.sleep(0.5)
                continue
            yield line.strip()

if __name__ == "__main__":
    log_path = "logs/app.log"
    print(f"👀 Monitoring log file: {log_path}")
    
    for log_line in follow_log(log_path):
        structured = parse_log_line(log_line)
        print(f"[STRUCTURED] {structured}")
