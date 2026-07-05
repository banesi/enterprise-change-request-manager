from file_handler import FileHandler
from managers import ChangeRequestManager

def main():
    input_change_data = FileHandler("data/change_requests.json","outputs/cab_report.json")
    input_change_data1 = FileHandler("data/change_requests.json","outputs/high_risk_changes.json")
    input_change_data2 = FileHandler("data/change_requests.json","outputs/customer_notifications.json")
    changes_data=input_change_data.load_from_json()
    managers1= ChangeRequestManager(changes_data)
    cab_report=managers1.generate_cab_report()
    input_change_data.dump_to_json(cab_report)
    high_risk_changes = managers1.get_high_risk_changes()
    generate_customer_notifications = managers1.generate_customer_notifications()
    input_change_data1.dump_to_json(high_risk_changes)
    input_change_data2.dump_to_json(generate_customer_notifications)




if __name__=='__main__':
    main()





