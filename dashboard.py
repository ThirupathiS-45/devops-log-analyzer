import streamlit as st
import pandas as pd
from datetime import datetime
from app.preprocessor import parse_log_line
from app.anomaly_detector import LogAnomalyDetector

# --- Streamlit Page Setup ---
st.set_page_config(layout="wide")
st.title("📊 Real-Time DevOps Log Analyzer using AI")

# --- Sidebar: Auto-refresh interval ---
refresh_interval = st.sidebar.slider("🔁 Refresh every (seconds)", min_value=5, max_value=60, value=10)
st.sidebar.write("⏱️ Last updated:", datetime.now().strftime("%H:%M:%S"))

# --- Inject HTML Meta-Refresh ---
st.markdown(f"""
    <meta http-equiv="refresh" content="{refresh_interval}">
""", unsafe_allow_html=True)

# --- Load and parse logs ---
def load_logs(file_path):
    logs = []
    try:
        with open(file_path, 'r') as f:
            for line in f:
                parsed = parse_log_line(line)
                if parsed['timestamp']:
                    logs.append(parsed)
    except FileNotFoundError:
        st.error("❌ Log file not found.")
    return logs

logs = load_logs("logs/app.log")

if not logs:
    st.warning("⚠️ No logs available.")
    st.stop()

# --- Logs to DataFrame ---
df = pd.DataFrame(logs)
df['timestamp'] = pd.to_datetime(df['timestamp'])

# --- Display Recent Logs ---
with st.expander("📜 Latest 50 Log Entries"):
    st.dataframe(df.tail(50), use_container_width=True)

# --- Bar Chart: Logs Per Minute ---
count_df = df.set_index("timestamp").resample("1min").count()["message"].reset_index()
count_df.columns = ["Time", "Log Count"]
st.subheader("📈 Log Volume Over Time")
st.bar_chart(count_df.set_index("Time"))

# --- Anomaly Detection ---
st.subheader("🚨 Live Anomaly Detection")
if len(logs) >= 5:
    detector = LogAnomalyDetector()
    anomalies = detector.detect_anomalies(logs)
    if anomalies.empty:
        st.success("✅ No anomalies detected.")
    else:
        st.error("⚠️ Anomalies Detected:")
        st.dataframe(anomalies, use_container_width=True)
else:
    st.info("ℹ️ Not enough logs to analyze. Waiting for more entries...")
