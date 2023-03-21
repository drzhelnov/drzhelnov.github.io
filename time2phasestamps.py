# Credit: ChatGPT Mar 14 Version (https://help.openai.com/en/articles/6825453-chatgpt-release-notes). Free Research Preview.

# Initial prompt:
# write a python script that takes a json file named timestamps-raw.json as input. this file contains a json array with a field timestamp, among others. this field contains unix time, with an optional decimal part. so the script needs to create a new property "phasestamp" with a string value that is based on the value of the timestamp field, as follows: if the time is 4:00-4:59am, then "very early"; if 5:00-6:59am, "early"; if 7:00-10:59am, "morning"; if 11am-12:59pm, "noon"; if 1:00-4:59pm, "afternoon"; if 5:00-6:59pm, "evening"; if 7:00-9:59pm, "late"; if 10pm-3:59am, "night". Also, the script need to add a new property "datestamp" that contains a value based on the timestamp field, in the "yyyy-mm-dd" format. Finally, the script will remove the field timestamp and save the output as phasestamps-raw.json.

# Final output, with modifications:

import json
import os
import sys
from datetime import datetime, timedelta, timezone

# Get the input file path from the command-line arguments
if len(sys.argv) < 2:
    print("Usage: python script.py /path/to/timestamps-raw.json")
    sys.exit(1)

input_file = sys.argv[1]

# Define the working directory and file names
work_dir = "_data"
output_file = "phasestamps-raw.json"

# Specify the timezone offset in hours from UTC
timezone_offset = -6

# Create the timezone object
timezone_obj = timezone(timedelta(hours=timezone_offset))

# Define the time ranges for each phase
phase_ranges = [
    ("after midnight", (0, 4)),
    ("very early", (4, 5)),
    ("early", (5, 7)),
    ("morning", (7, 11)),
    ("noon", (11, 13)),
    ("afternoon", (13, 17)),
    ("evening", (17, 19)),
    ("late", (19, 22)),
    ("before midnight", (22, 24)),
]

# Load the input file
with open(input_file) as f:
    data = json.load(f)

# Process each timestamp
for entry in data:
    # Parse the timestamp as a datetime object in UTC
    timestamp = datetime.utcfromtimestamp(float(entry["timestamp"])).replace(tzinfo=timezone.utc)

    # Adjust the timestamp to the specified timezone
    timestamp = timestamp.astimezone(timezone_obj)
    
    # Add the phasestamp property
    hour = timestamp.hour + timestamp.minute / 60
    for phase, (start, stop) in phase_ranges:
        if start <= hour < stop:
            entry["phasestamp"] = phase
            break
    
    # Add the datestamp property
    entry["datestamp"] = timestamp.strftime("%Y-%m-%d")
    
    # Remove the timestamp and modified properties
    del entry["timestamp"]
    del entry["modified"]

    # Remove the modified property
    

# Save the output file
with open(os.path.join(work_dir, output_file), "w") as f:
    json.dump(data, f)
