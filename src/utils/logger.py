import os
import json

class Logger:

    def __init__(self, log_dir, filename="log.json"):
        self.log_dir = log_dir
        self.log_path = os.path.join(log_dir, filename)
        
        if not os.path.exists(self.log_path):
            os.makedirs(self.log_dir, exist_ok=True)
            with open(self.log_path, 'w') as f:
                json.dump([], f)

    def load(self):
        with open(self.log_path, "r") as f:
            return json.load(f)

    def append(self, item):
        data = self.load()
        data.append(item)
        with open(self.log_path, 'w') as f:
            f.seek(0)
            json.dump(data, f, indent=4)

    def amend(self, key_name, key_value, amendment):
        data = self.load()
        with open(self.log_path, 'w') as f:
            for item in data:
                if key_name in item and item[key_name] == key_value:
                    item.update(amendment)
                    break
            f.seek(0)
            json.dump(data, f, indent=4)

    def find(self, key_name, key_value):
        data = self.load()
        with open(self.log_path, 'r') as f:
            for item in data:
                if key_name in item and item[key_name] == key_value:
                    return item
