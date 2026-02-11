import json
import requests
from datetime import datetime
from pathlib import Path

minute = datetime.now().minute
todo_id = minute + 1 if minute < 59 else 1

url = f"https://jsonplaceholder.typicode.com/todos/{todo_id}"
res = requests.get(url)
data = res.json()

path = Path("김수빈_test.json")

if path.exists():
    try:
        existing = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        existing = []
else:
    existing = []

existing.append({
    "collected_at": datetime.now().isoformat(),
    "todo": data
})

path.write_text(json.dumps(existing, indent=2, ensure_ascii=False), encoding="utf-8")