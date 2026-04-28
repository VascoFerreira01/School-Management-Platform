from src.school_management.models.student import Student
from src.school_management.models.teacher import Teacher

# checks if the teacher has the correct role
# checks if the teacher can add/remove students
# checks if the teache can create summaries
# checks if the teacher has permission no manage grades

def test_teacher_can_add_student():
    teacher = Teacher(1, "Maria Costa", "maria@email.com", "T001", "Matemática")
    student = Student(2, "João Silva", "joao@email.com", "A001", "10A")

    teacher.add_student(student)

    assert student in teacher.list_student()

def test_teacher_can_create_summary():
    teacher = Teacher(1, "Maria Costa", "maria@email.com", "T001", "Matemática")
   
    teacher.create_summary('Introducao a equacoes')

    assert 'Introducao a equacoes' in teacher.list_summary()


def test_teacher_can_manage_grades():
    teacher = Teacher(1, "Maria Costa", "maria@email.com", "T001", "Matemática")
    
    assert teacher.can('manage_grades') is True