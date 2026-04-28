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
