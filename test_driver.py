from db_module import Database
from report_module import ReportManager

def integration_driver():
    db = Database()
    manager = ReportManager(db)

    print("Executing ITC-01: Valid Input...")
    res, msg = manager.submit_report("Keys", "Library")
    print(f"Result: {res}, Message: {msg}\n")

    print("Executing ITC-02: Missing Location Input...")
    res, msg = manager.submit_report("Wallet", "")
    print(f"Result: {res}, Message: {msg}\n")

    print("Executing ITC-03: Missing Name Input...")
    res, msg = manager.submit_report("", "Cafe")
    print(f"Result: {res}, Message: {msg}\n")

    print("Executing ITC-04: Mismatched/Null Input...")
    res, msg = manager.submit_report(None, "Cafe")
    print(f"Result: {res}, Message: {msg}\n")

integration_driver()