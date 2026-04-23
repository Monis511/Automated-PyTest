class Database:
    def __init__(self):
        self.storage = []

    def save_item(self, item_data):
        if not item_data.get("name") or not item_data.get("location"):
            return False, "Missing Fields"
        self.storage.append(item_data)
        return True, "Success"