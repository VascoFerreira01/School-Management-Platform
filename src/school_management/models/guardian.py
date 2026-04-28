from src.school_management.auth.roles import Role
from src.school_management.models.user import User


class Guardian(User):

    def __init__(self, user_id: int, name: str, email: str, child_student_number: str):
        super().__init__(user_id, name, email, Role.GUARDIAN)
        self.child_student_number = child_student_number

    #get_child_number
    #can_view_child_grades
    #can_view_child_attendance
    #can_view_child_schedule

    def get_child_number(self):
        return self.child_student_number
    
    def can_view_child_grades(self):
        return self.can('view_child_grades')

    def can_view_child_attendance(self):
        return self.can('view_child_attendance')
    
    def can_view_child_schedule(self):
        return self.can('view_child_schedule')