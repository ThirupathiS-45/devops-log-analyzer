import pandas as pd
from prophet import Prophet

class LogAnomalyDetector:
    def __init__(self):
        self.model = Prophet()
        self.fitted = False

    def prepare_data(self, log_entries):
        """
        Convert logs to time series data: count of logs per minute
        """
        df = pd.DataFrame(log_entries)
        if df.empty:
            return pd.DataFrame(columns=["ds", "y"])

        df['timestamp'] = pd.to_datetime(df['timestamp'])
        df = df.set_index('timestamp').resample('1min').count()['message'].reset_index()
        df.columns = ['ds', 'y']
        return df

    def train(self, log_entries):
        ts_data = self.prepare_data(log_entries)

        # Check if enough data to train
        if len(ts_data.dropna()) < 2:
            print("⚠️ Not enough data to train Prophet model.")
            return

        self.model.fit(ts_data)
        self.fitted = True

    def detect_anomalies(self, log_entries):
        if not self.fitted:
            self.train(log_entries)

        ts_data = self.prepare_data(log_entries)

        if len(ts_data.dropna()) < 2:
            print("ℹ️ Not enough data to detect anomalies.")
            return pd.DataFrame(columns=["ds", "y", "yhat", "yhat_upper"])

        future = self.model.make_future_dataframe(periods=5, freq='min')
        forecast = self.model.predict(future)

        # Merge forecast and actuals
        merged = pd.merge(forecast[['ds', 'yhat', 'yhat_upper', 'yhat_lower']],
                          ts_data, on='ds', how='left')
        anomalies = merged[merged['y'] > merged['yhat_upper']]
        return anomalies[['ds', 'y', 'yhat', 'yhat_upper']]

# Example usage (for testing)
if __name__ == "__main__":
    sample_logs = [
        {'timestamp': '2025-07-06 22:00:00', 'level': 'ERROR', 'message': 'A'},
        {'timestamp': '2025-07-06 22:00:10', 'level': 'ERROR', 'message': 'B'},
        {'timestamp': '2025-07-06 22:01:00', 'level': 'ERROR', 'message': 'C'},
        {'timestamp': '2025-07-06 22:02:00', 'level': 'ERROR', 'message': 'D'},
        {'timestamp': '2025-07-06 22:02:30', 'level': 'ERROR', 'message': 'E'},
        {'timestamp': '2025-07-06 22:02:40', 'level': 'ERROR', 'message': 'F'},
    ]
    detector = LogAnomalyDetector()
    anomalies = detector.detect_anomalies(sample_logs)
    print("🔍 Anomalies Detected:\n", anomalies)
