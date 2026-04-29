from src.school_management.auth.roles import Role
from src.school_management.models.user import User


class Student(User):

    def __init__(
        self, user_id: int, name: str, email: str, student_number: str, class_name: str
    ):
        super().__init__(user_id, name, email, Role.STUDENT)
        self.student_number = student_number
        self.class_name = class_name
        self.card_balance = 0.0  # not a entry parameter because it will be updated by the system when the student makes purchases in the cafeteria or library
        self.grades = []
        
    def add_balance(
        self, amount: float
    ) -> None:  # -> None means that this method does not return anything
        if amount <= 0:
            raise ValueError("Amount must be positive")
        self.card_balance += amount

    def remove_balance(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Amount must be positive")

        if amount > self.card_balance:
            raise ValueError("Insufficient balance")
        self.card_balance -= amount

    def add_grade(self, grade) -> None:
        self.grades.append(grade)

    def list_grades(self) -> list:
        return self.grades
    
    def calculate_subject_average(self, subject):
        subject_grades = [grade for grade in self.grades if grade.subject == subject] 
        # Check if there are grades for that student in that subject

        if not subject_grades: # If the list is empty, it means there are no grades for that student in that subject
            raise ValueError('Student has no grades for this subject')
        
        total_weight = sum(grade.assessment.weight for grade in subject_grades) # Calculate the total weight of the assessments for that subject
        weighted_sum = sum(grade.value * grade.assessment.weight for grade in subject_grades) # Calculate the weighted sum of the grades for that subject

        return weighted_sum / total_weight if total_weight != 0 else 0 
    
    def __eq__(self, other):
        if not isinstance(other, Student): # check if the other object is an instance of the Student class
            return False 
        
        return self.user_id == other.user_id or self.student_number == other.student_number 