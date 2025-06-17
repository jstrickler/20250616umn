import os   # also imports os.path
from datetime import datetime

FILE_PATH = "C:/Users/Administrator/Desktop/pyuminn/DATA/ctemps.txt"
SHORT_PATH = "DATA/ctemps.txt"

print(f"{os.path.exists(FILE_PATH) = }\n")
print(f"{os.path.basename(FILE_PATH) = }\n")
print(f"{os.path.dirname(FILE_PATH) = }\n")
print(f"{os.path.abspath(SHORT_PATH) = }\n")
print(f"{os.path.split(FILE_PATH) = }\n")
print(f"{os.path.splitext(FILE_PATH) = }\n")
print(f"{os.path.isfile(FILE_PATH) = }\n")
print(f"{os.path.isdir(FILE_PATH) = }\n")
print(f"{os.path.getsize(FILE_PATH) = }\n")
raw_timestamp = os.path.getmtime(FILE_PATH)
print(f"{raw_timestamp = }\n")
timestamp = datetime.fromtimestamp(raw_timestamp)
print(f"{timestamp = }\n")

FOLDER = "DATA"
FILE_NAME = "mary.txt"

file_path = os.path.join(FOLDER, FILE_NAME)
print(f"{file_path = }\n")


