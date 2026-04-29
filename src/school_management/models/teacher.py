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
        self.summaries = []
        self.grades = []
        
    #add_student
    def add_student(self, student):     
        self.students.append(student)

    #list_student
    def list_students(self):
        return self.students

    #create_summary
    def create_summary(self, summary):
        self.summaries.append(summary)

    #list_summaries
    def list_summaries(self):
        return self.summaries
    
    #assign_grade
    def assign_grade(self, student, subject, assessment, value):
        from src.school_management.models.grade import Grade

        grade = Grade(student, subject, assessment, value)
        self.grades.append(grade)
        student.add_grade(grade)

        return grade 
    
    # sees if the teacher is already on the list of teachers by employee number 
    def __eq__(self, other):
        if not isinstance(other, Teacher):
            return False
        # Compara pelo número de funcionário ou pelo ID de utilizador
        return self.employee_number == other.employee_number or self.user_id == other.user_id