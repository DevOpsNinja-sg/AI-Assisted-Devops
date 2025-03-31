import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest

log_file = "system_logs.txt"

with open(log_file, "r") as file:
    logs = file.readlines()
    
data = []
for log in logs:
    parts = log.split(" ",3)
    if len(parts) < 4:
        continue
    timestamp = parts[0] + " "+ parts[1]
    level = parts[2]
    message = parts[3]
    data.append([timestamp, level, message])
    
df = pd.DataFrame(data, columns=["timestamp", "level", "message"])
df['timestamp'] = pd.to_datetime(df['timestamp'])

#Assign numeric values to log levels
log_level_mapping = {
    "INFO": 1,
    "WARNING": 2,
    "ERROR": 3,
    "CRITICAL": 4
}
df['level_score'] = df['level'].map(log_level_mapping)

# add message length
df['message_length'] = df['message'].apply(len)

#ai model for anomaly detection
model = IsolationForest(contamination=0.1, random_state=42)
df["anomaly"] = model.fit_predict(df[['level_score', 'message_length']])

# Mark anomalies in a readable format
df["is_anomaly"] = df["anomaly"].apply(lambda x: "❌ Anomaly" if x == -1 else "✅ Normal")

# Print only detected anomalies
anomalies = df[df["is_anomaly"] == "❌ Anomaly"]
print("\n🔍 **Detected Anomalies:**\n", anomalies)
        
    


