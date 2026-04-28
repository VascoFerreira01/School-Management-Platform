from src.school_management.auth.roles import Role
from src.school_management.models.user import User

'''"view_students",
        "manage_grades",
        "manage_summaries",
        "view_schedules"'''


class Teacher(User):

    def __init__(
        self, user_id: int, name: str, email: str, employee_number: str, subject: str
    ):
        super().__init__(user_id, name, email, Role.TEACHER)
        self.employee_number = employee_number
        self.subject = subject
        self.students = []
        self.sumaries = []
        self.grades = []
        
    #add_student
    def add_student(self, student):     
        self.students.append(student)

    #list_student
    def list_student(self):
        return self.students

    #create_summary
    def create_summary(self, summary):
        self.sumaries.append(summary)

    #list_summaries
    def list_summary(self):
        return self.sumaries
    
    #assin_grade
    def assign_grade(self, student, subject, value):
        from src.school_management.models.grade import Grade

        grade = Grade(student, subject, value)
        self.grades.append(grade)