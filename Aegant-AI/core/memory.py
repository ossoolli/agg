import json
import os

class LongTermMemory:
    def __init__(self, file_path='storage/memory.json'):
        self.file_path = file_path
        if not os.path.exists('storage'):
            os.makedirs('storage')
        if not os.path.exists(self.file_path):
            with open(self.file_path, 'w', encoding='utf-8') as f:
                json.dump({}, f)

    def save_context(self, user_id, message, role='user'):
        with open(self.file_path, 'r+', encoding='utf-8') as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = {}
            history = data.get(str(user_id), [])
            history.append({"role": role, "content": message})
            data[str(user_id)] = history[-10:] # حفظ آخر 10 رسائل
            f.seek(0)
            json.dump(data, f, ensure_ascii=False, indent=4)
            f.truncate()

    def get_context(self, user_id):
        if not os.path.exists(self.file_path): return []
        with open(self.file_path, 'r', encoding='utf-8') as f:
            try:
                data = json.load(f)
                return data.get(str(user_id), [])
            except:
                return []