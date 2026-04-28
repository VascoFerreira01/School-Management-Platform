from src.school_management.models.guardian import Guardian

# if has student number
# can see schedule
# can see grades
# can see attendance

def test_guardian__has_child_student_number():
    guardian = Guardian(1, "Carlos Silva", "carlos@email.com", "A001")

    assert guardian.child_student_number == 'A001'

def test_guardian_can_view_child_grades():
    guardian = Guardian(1, "Carlos Silva", "carlos@email.com", "A001")

    assert guardian.can_view_child_grades() is True

def test_guardian_can_view_child_schedule():
    guardian = Guardian(1, "Carlos Silva", "carlos@email.com", "A001")

    assert guardian.can_view_child_schedule() is True

def test_guardian_can_view_child_attendance():
    guardian = Guardian(1, "Carlos Silva", "carlos@email.com", "A001")

    assert guardian.can_view_child_attendance() is True