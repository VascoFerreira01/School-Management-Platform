import pytest

from src.school_management.models.admin import Admin
from src.school_management.models.student import Student

# admin_has_full_access
# can_add_reports
# can activate/deactivate users

def test_admin_has_full_access():
    admin = Admin(1, "Diretor Escola", "diretor@email.com", "D001")

    assert admin.has_full_access() is True

def test_admin_can_add_reports():
    admin = Admin(1, "Diretor Escola", "diretor@email.com", "D001")
    admin.add_report('Inventory report')

    assert 'Inventory report' in admin.list_reports()

def test_admin_can_activate_and_deactivate_user():
    admin = Admin(1, "Diretor Escola", "diretor@email.com", "D001")
    student = Student(2, "João Silva", "joao@email.com", "A001", "10A")
   
    admin.activate_user(student)
    assert student.is_active is True

    admin.deactivate_user(student)
    assert student.is_active is False

def test_admin_cannot_add_empty_report():
    admin = Admin(1, "Diretor Escola", "diretor@email.com", "D001")

    with pytest.add_report(''):
        raise ValueError("The report can't be empty ")

    