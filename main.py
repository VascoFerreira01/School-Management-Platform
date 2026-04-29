
from src.school_management.models.student import Student
from src.school_management.models.teacher import Teacher
from src.school_management.models.subject import Subject
from src.school_management.models.assessment import Assessment
from src.school_management.models.class_group import ClassGroup

def main():
    student = Student(1, "João Silva", "joao@email.com", "A001", "10A")
    teacher = Teacher(2, "Maria Costa", "maria@email.com", "T001", "Matemática")
    teacher1 = Teacher(3, "Maria Costa", "maria@email.com", "T002", "Matemática")

    math = Subject("Matemática")

    test_1 = Assessment("Teste 1", "test", 40)
    test_2 = Assessment("Teste 2", "test", 40)
    assignment = Assessment("Trabalho 1", "assignment", 20)
    turma_a = ClassGroup('10 A')

    teacher.assign_grade(student, math, test_1, 16)
    teacher.assign_grade(student, math, test_2, 14)
    teacher.assign_grade(student, math, assignment, 18)

    turma_a.add_student(student)
    turma_a.add_teacher(teacher)
    turma_a.add_teacher(teacher1)

    students= turma_a.list_students()
    for s in students:
        print(s.name)

    profs= turma_a.list_teachers()
    for t in profs:
        print(t.name)

    
    #print("\n--- Grades ---")
    #for grade in student.list_grades():
        #print(grade)

    #print("\n--- Average ---")
   #print(student.calculate_subject_average(math))

if __name__ == "__main__":
    main()
