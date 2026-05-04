import json
from backend.config.settings import settings

class StorageService:
    @staticmethod
    def load_data():
        with open(settings.DATA_PATH, "r", encoding="utf-8") as f:
            return json.load(f)

    @staticmethod
    def save_data(new_item: dict):
        data = StorageService.load_data()
        data["informativos"].append(new_item)
        with open(settings.DATA_PATH, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
            