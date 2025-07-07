# 📊 Real-Time DevOps Log Analyzer using AI

This project brings **AI and DevOps together** to create a powerful, automated, and intelligent log monitoring system — essential for any team that values **uptime, performance, and proactive maintenance**.

---

## 🚀 Features

- 📡 Real-time log monitoring  
- 🤖 AI-based anomaly detection using Prophet  
- 📈 Visual dashboard with Streamlit  
- 🧪 Continuous log simulation for testing  
- 🐳 Fully containerized using Docker  

---

## 🧠 Tech Stack

- Python 3.9+  
- [Prophet](https://facebook.github.io/prophet/) – Time-series anomaly detection  
- [Streamlit](https://streamlit.io/) – Dashboard UI  
- [Docker](https://www.docker.com/) – Containerization  
- [cmdstanpy](https://mc-stan.org/users/interfaces/cmdstan) – Backend for Prophet  

---

## 📁 Project Structure

```
devops-log-analyzer/
│
├── app/
│   ├── log_reader.py         # Real-time log reader  
│   ├── anomaly_detector.py   # ML model for anomaly detection  
│   ├── preprocessor.py       # Log cleaning & parsing  
│   └── main.py               # Main loop to run detection  
│
├── logs/
│   └── app.log               # Log file (auto-generated)  
│
├── dashboard.py              # Streamlit dashboard  
├── simulate_logs.py          # Log simulator (random logs)  
├── requirements.txt          # Python dependencies  
├── Dockerfile                # Docker build config  
└── README.md                 # Project documentation  
```

---

## ⚙️ How to Run (Locally)

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/devops-log-analyzer.git
cd devops-log-analyzer
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

### 3. Install Requirements

```bash
pip install -r requirements.txt
```

### 4. Start Log Simulator (Terminal 1)

```bash
python simulate_logs.py
```

### 5. Run Log Analyzer (Terminal 2)

```bash
python app/main.py
```

### 6. Launch Streamlit Dashboard (Terminal 3)

```bash
streamlit run dashboard.py
```

---

## 🐳 Docker Instructions

### 🔧 Build Docker Image

```bash
docker build -t devops-log-analyzer .
```

### ▶️ Run Docker Container

```bash
docker run -p 8501:8501 devops-log-analyzer
```

> ⚠️ Note: If port 8501 is in use, try `-p 8502:8501` or stop the conflicting container.

---

## 🧪 Sample `requirements.txt`

```
streamlit
pandas
prophet
cmdstanpy
```

---

## ✅ Who Can Use This?

- 👩‍💻 DevOps Engineers – for real-time uptime alerting  
- 🧠 AI/ML Engineers – to integrate forecasting into monitoring  
- 🎓 Students – to explore real-time time-series ML projects  
- 🚀 Tech Teams – to detect issues before users do
