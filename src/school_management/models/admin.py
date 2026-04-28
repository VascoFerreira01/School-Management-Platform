from src.school_management.auth.roles import Role
from src.school_management.models.user import User


class Admin(User):

    def __init__(self, user_id: int, name: str, email: str, employee_number: str):
        super().__init__(user_id, name, email, Role.ADMIN)
        self.employee_number = employee_number
        self.available_reports = []


# available reports
# activate/deactivate users
# checks if has total access


    def add_report(self, report_name: str) -> None:

        if not report_name:  #this line means if the report_name is empty or None. 
            raise ValueError('Report cannot be empty.')
        
        self.available_reports.append(report_name)

    def list_reports(self):
        return self.available_reports
    
    def has_full_access(self) -> bool:
        return self.can('view_all')

    def deactivate_user(self, user:User ):
        user.is_active = False
    
    def activate_user(self, user:User):
        user.is_active = True
       
