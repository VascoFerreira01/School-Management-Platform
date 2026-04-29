class ClassGroup:

    def __init__(self, name: str):
        if not name:
            raise ValueError('Class group name cannot be empty')
        
        self.name = name
        self.students = []
        self.teachers =[]
        self.subjects = []

    def add_student(self, student) -> None:
        if student in self.students:
            raise ValueError('Student already belongs to this class group')
        self.students.append(student)

    def add_teacher(self, teacher) -> None:
        if teacher in self.teachers:
            raise ValueError('Teacher already belongs to this class group')
        self.teachers.append(teacher)
        
    def add_subject(self, subject) -> None:
        if subject in self.subjects:
            raise ValueError('Subject already belongs to this class group')
        self.subjects.append(subject)

    def list_students(self) -> list:
        return self.students
    
    def list_teachers(self) -> list:
        return self.teachers
    
    def list_subjecs(self) -> list:
        return self.subjects
    
    def __str__(self):
        print(f'Class group: {self.name}')