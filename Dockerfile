# 🔹 Use official lightweight Python image
FROM python:3.9-slim

# 🔹 Set working directory
WORKDIR /app

# 🔹 Copy all project files into the container
COPY . .

# 🔹 Install Python dependencies
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

# 🔹 Create logs directory and file
RUN mkdir -p logs && touch logs/app.log

# 🔹 Expose Streamlit default port
EXPOSE 8501

# 🔹 Start both the log simulator and Streamlit app together
CMD ["bash", "-c", "python simulate_logs.py & streamlit run dashboard.py --server.port=8501 --server.address=0.0.0.0"]
