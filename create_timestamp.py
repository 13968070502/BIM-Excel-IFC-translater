"""Create timestamp for STEP-File"""

from datetime import datetime


def create_timestamp():
    # Creation of timestamp
    timestamp = datetime.now()
    # Convert timestamp to string
    timestampStr = timestamp.strftime("%d-%m-%YT%H:%M:%S")

    return timestampStr