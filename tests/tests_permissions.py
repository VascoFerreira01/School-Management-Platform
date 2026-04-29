from src.school_management.auth.permissions import has_permission
from src.school_management.auth.roles import Role


def test_admin_can_manage_users():
    assert has_permission(Role.ADMIN, "manage_users") is True


def test_student_can_manage_users():
    assert has_permission(Role.STUDENT, "manage_users") is False


def test_teacher_can_manage_grades():
    assert has_permission(Role.TEACHER, "manage_grades") is True


def test_employee_can_manage_assigned_area():
    assert has_permission(Role.EMPLOYEE, "manage_assigned_area") is True
