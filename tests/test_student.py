import pytest

# we will check if the balance starts at 0
# if add and remove balance works
# if doesnt accept negative values
# cant spend more than the balance
from src.school_management.models.student import Student


def test_student_start_with_no_balance():
    student = Student(1, "João Silva", "joao@email.com", "A001", "10A")

    assert student.card_balance == 0.0


def test_add_balance():
    student = Student(1, "João Silva", "joao@email.com", "A001", "10A")

    student.add_balance(10)

    assert student.card_balance == 10.0


def test_remove_balance():
    student = Student(1, "João Silva", "joao@email.com", "A001", "10A")

    student.add_balance(20)
    student.remove_balance(5)

    assert student.card_balance == 15.0


def test_negative_balance_raises_error():
    student = Student(1, "João Silva", "joao@email.com", "A001", "10A")

    with pytest.raises(ValueError):
        student.add_balance(-10)


def test_remove_more_than_balance_raises_error():
    student = Student(1, "João Silva", "joao@email.com", "A001", "10A")
    student.add_balance(10)

    with pytest.raises(ValueError):
        student.remove_balance(20)
