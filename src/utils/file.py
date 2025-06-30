import json
from dataclasses import asdict
from typing import List

def save_json(file_name: str, data: List[any]):
    with open(file_name + ".json", "w", encoding="utf-8") as file:
        json.dump([asdict(item) for item in data], file, ensure_ascii=False, indent=2)