import platform
import os
import json

system=platform.system()
if system=="Windows":
    name1="Windows"
elif system=="Linux":
    name1="Linux"
else:
    name1="Unknown"

p={
    "system": {
        "name": name1,
        "release": platform.release(),
        "version": platform.version(),
        "machine": platform.machine()
    },
    "computer": {
        "processor": platform.processor(),
        "cpu": os.cpu_count(),
        "computer_name": platform.node()
    },
    "python": {
        "version": platform.python_version()
    }
    }

with open("result.json","w", encoding="utf-8") as file:
    json.dump(p, file, ensure_ascii=False)
        
