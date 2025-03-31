import pandas as pd
import numpy as np
import re
from collections import Counter

log_file = "system_logs.txt"

# Read the log file
log_entries = []
with open(log_file, 'r') as file:
    for line in file:
        match = re.match(r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (\w+) (.*)', line.strip())
        if match:
            timestamp, log_level, message = match.groups()
            log_entries.append([timestamp, log_level, message])
# Convert to DataFrame
log_df = pd.DataFrame(log_entries, columns=['timestamp', 'log_level', 'message'])
# Convert Timestamp to datetime
log_df['timestamp'] = pd.to_datetime(log_df['timestamp']);  

error_count = Counter(log_df[log_df["log_level"] == "ERROR"]['timestamp'].dt.floor("30s"))


threshold = 3

#detect anomalies
for time, count in error_count.items():
    if count > threshold:
        print(f"Anomaly detected at {timestamp}: {count} errors")
        
print("\nLog analysis complete.")
print(log_df)