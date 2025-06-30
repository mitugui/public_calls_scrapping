import json

def save_json(file_name: str, data):
    with open(file_name + '.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=2)