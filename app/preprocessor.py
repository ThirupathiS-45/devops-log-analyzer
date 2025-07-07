import re
from datetime import datetime

def parse_log_line(line):
    """
    Parses a raw log line into structured format: timestamp, level, message
    """
    # Example log format: [2025-07-06 21:00:01] ERROR: Something went wrong
    pattern = r"\[(.*?)\]\s+(\w+):\s+(.*)"

    match = re.match(pattern, line)
    if match:
        timestamp_str, level, message = match.groups()
        try:
            timestamp = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")
        except ValueError:
            timestamp = None
        return {
            "timestamp": timestamp,
            "level": level,
            "message": message
        }
    else:
        # If it doesn't match, return raw
        return {
            "timestamp": None,
            "level": "UNKNOWN",
            "message": line
        }

# For test
if __name__ == "__main__":
    sample = "[2025-07-06 21:00:01] ERROR: DB connection failed"
    print(parse_log_line(sample))
