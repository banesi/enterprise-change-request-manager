from models import ChangeRequest

class ChangeRequestManager:
    def __init__(self,changes):
        self.changes = self.create_change_objects(changes)

    def create_change_objects(self,change_data):

        change_data_list=[]
        
        for change in change_data :
            new_change = ChangeRequest(change.get('change_id'), change.get('customer'), change.get('risk'), change.get('status'), change.get('description'), change.get('planned_days'))
            change_data_list.append(new_change)
        
        return change_data_list
    
    def generate_all_summaries(self):

        summaries=[]

        for change in self.changes:
            summary = change.generate_summary()
            summaries.append(summary)
        
        return summaries
    
    def get_high_risk_changes(self):

        high_risk_changes=[]

        for change in self.changes:

            if change.is_high_risk():
                high_risk_changes.append(change.to_dict())
        
        return high_risk_changes
        

    
    def generate_customer_notifications(self):

        customer_notifications = []

        for change in self.changes:
            customer_notofication = change.generate_customer_notification()
            customer_notifications.append(customer_notofication)

        return customer_notifications
    
    def generate_cab_report(self):

        total_changes = len(self.changes)
        scheduled = 0
        in_progress = 0
        completed = 0
        cancelled = 0 
        high_risk = 0
        medium_risk = 0
        low_risk = 0
        for change in self.changes:
            if change.status == "Scheduled":
                scheduled = scheduled+1
            if change.status == "In Progress":
                in_progress = in_progress + 1
            if change.status == "Completed":
                completed = completed + 1
            if change.status == "Cancelled":
                cancelled = cancelled + 1
        
        for change in self.changes:
            if change.is_high_risk():
                high_risk = high_risk + 1
            if change.risk == "Medium":
                medium_risk = medium_risk + 1
            if change.risk == "Low":
                low_risk = low_risk + 1
        
        return(

            {
                "total_changes": total_changes,
                "scheduled": scheduled,
                "in_progress": in_progress,
                "completed": completed,
                "cancelled": cancelled,
                "high_risk": high_risk,
                "medium_risk": medium_risk,
                "low_risk": low_risk
            }
        )




        



