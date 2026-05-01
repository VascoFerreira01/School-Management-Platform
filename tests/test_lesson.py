import pytest
from datetime import time

from src.school_management.models.lesson import Lesson
from src.school_management.models.subject import Subject
from src.school_management.models.teacher import Teacher
from src.school_management.models.class_group import ClassGroup

#test_lesson_creation

def test_lesson_creation():   
    subject = Subject("Math")
    teacher = Teacher(1, "Maria", "m@email.com", "T001", "Math")
    class_group = ClassGroup("10A")

    lesson = Lesson(
        subject,
        teacher,
        class_group,
        "Monday",
        time(9, 0),
        time(10, 0),
    )

    assert lesson.subject == subject # lesson.subject takes the subject objtect abd compares with the object created in the test
    assert lesson.teacher == teacher
    assert lesson.class_group == class_group

#test_invalid_time
def test_invalid_time():
    subject = Subject("Math")
    teacher = Teacher(1, "Maria", "m@email.com", "T001", "Math")
    class_group = ClassGroup("10A")

    with pytest.raises(ValueError, match = 'Start time must be before end time'):
        Lesson(
            subject,
            teacher,
            class_group,
            "Monday",
            time(10, 0),
            time(9, 0),
        )

    