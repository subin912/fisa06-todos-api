import json
import requests
from datetime import datetime

minute = datetime.now().minute
todo_id = minute + 1 if minute < 59 else 1

url = f"https://jsonplaceholder.typicode.com/todos/{todo_id}"
res = requests.get(url)
data = res.json()

path = "/tmp/김수빈_test.json"

try:
    with open(path, "r") as f:
        existing = json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
    existing = []

existing.append({
    "collected_at": datetime.now().isoformat(),
    "todo": data
})

with open(path, "w") as f:
    json.dump(existing, f, indent=2, ensure_ascii=False)