import logging
from datetime import datetime
import os
import pandas as pd
from housing.constant import get_current_time_stamp 

# Logging directory name
LOG_DIR = "logs"

# Function to return the log file name log_<current timestamp>.log
def get_log_file_name():
    return f"log_{get_current_time_stamp()}.log"

# Get the log file name
LOG_FILE_NAME=get_log_file_name()

# Create a directory
os.makedirs(LOG_DIR, exist_ok=True)

# Get the log file path
LOG_FILE_PATH = os.path.join(LOG_DIR,LOG_FILE_NAME)

# Config the logging 
logging.basicConfig(filename=LOG_FILE_PATH,
filemode="w",
format='[%(asctime)s]^;%(levelname)s^;%(lineno)d^;%(filename)s^;%(funcName)s()^;%(message)s',
level=logging.INFO
)

def get_log_dataframe(file_path):
    data=[]
    with open(file_path) as log_file:
        for line in log_file.readlines():
            data.append(line.split("^;"))

    log_df = pd.DataFrame(data)
    columns=["Time stamp","Log Level","line number","file name","function name","message"]
    log_df.columns=columns
    
    log_df["log_message"] = log_df['Time stamp'].astype(str) +":$"+ log_df["message"]

    return log_df[["log_message"]]