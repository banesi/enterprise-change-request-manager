

class ChangeRequest:
    def __init__(self,change_id,customer,risk,status,description,planned_days):
        self.change_id = change_id
        self.customer = customer
        self.risk = risk
        self.status = status
        self.description = description
        self.planned_days = planned_days
    
    def is_high_risk(self):
        
        if self.risk == 'High':
            return True
        else:
            return False
    
    def generate_summary(self):

        return (f"{self.change_id} - {self.customer} - {self.risk} Risk - {self.status} - {self.description}")
    
    def to_dict(self):

        return(
            {
                "change_id": self.change_id,
                "customer": self.customer,
                "risk": self.risk,
                "status": self.status,
                "description": self.description,
                "planned_days": self.planned_days
            }
        )
    
    def generate_customer_notification(self):

        return (
            f""" Dear {self.customer},

                Your change request {self.change_id} for {self.description} is currently {self.status}.

                Planned implementation window: within {self.planned_days} days.
                Risk Level: {self.risk}

                We will keep you updated throughout the change lifecycle.

                Regards,
                Enterprise Support Team"""



        )
    