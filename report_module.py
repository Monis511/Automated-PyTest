class ReportManager:
    def __init__(self, db_instance):
        self.db = db_instance

    def submit_report(self, name, location):
        
        item = {"name": name, "location": location}
        status, message = self.db.save_item(item)
        return status, message