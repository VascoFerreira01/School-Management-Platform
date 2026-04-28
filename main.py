from src.school_management.models.employee import Employee
from src.school_management.models.student import Student
from src.school_management.models.teacher import Teacher


def main():
    student = Student(1, "João Silva", "joao@email.com", "A001", "10A")
    teacher = Teacher(2, "Maria Costa", "maria@email.com", "T001", "Matemática")
    employee = Employee(3, "Ana Santos", "ana@email.com", "E001", "bar")

    print(student.display_info())
    print(teacher.display_info())
    print(employee.display_info())

    print(student.can("view_own_grades"))
    print(teacher.can("manage_grades"))
    print(employee.can("manage_assigned_area"))


if __name__ == "__main__":
    main()
