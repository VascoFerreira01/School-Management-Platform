import pytest

from src.school_management.models.class_group import ClassGroup 
from src.school_management.models.teacher import Teacher
from src.school_management.models.student import Student
from src.school_management.models.subject import Subject

student = Student(1, "João Silva", "joao@email.com", "A001", "10A")
class_group = ClassGroup("10A")
subject = Subject("Matemática")
teacher = Teacher(1, "Maria Costa", "maria@email.com", "T001", "Matemática")

# test_class_group_is_created_successfully
def test_class_group_is_created_successfully():
    class_group = ClassGroup("10A")

    assert class_group.name == '10A'

# test_classgroup_can_add_student
def test_classgroup_can_add_student():
    student = Student(1, "João Silva", "joao@email.com", "A001", "10A")
    class_group = ClassGroup("10A")

    class_group.add_student(student) # add the student to the class group 10A

    assert student in class_group.list_students() # puts the student in the list and checks if its there

# test_class_group_cannot_add_student_twice
def test_class_group_cannot_add_student_twice(): 
    student = Student(1, "João Silva", "joao@email.com", "A001", "10A")
    class_group = ClassGroup("10A")

    class_group.add_student(student) # add the student for the first time

    with pytest.raises(ValueError): # try to add the same student again, which should raise a ValueError
        class_group.add_student(student) 
        # in this 2 lines we are saying that when we ry to add the same student it raises ValueError

# test_class_group_can_add_teacher
def test_class_group_can_add_teacher():
    teacher = Teacher(1, "Maria Costa", "maria@email.com", "T001", "Matemática")
    class_group = ClassGroup("10A")

    class_group.add_teacher(teacher) # add the teacher to the class group 10A
    assert teacher in class_group.list_teachers() # puts the teacher in the list and checks if its there

# test_class_group_can_add_subject
def test_class_group_can_add_subject():
    subject = Subject("Matemática")
    class_group = ClassGroup("10A")

    class_group.add_subject(subject) # add the subject to the class group 10A
    assert subject in class_group.list_subjects() # puts the subject in the list and checks if its there