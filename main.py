
from src.school_management.models.student import Student
from src.school_management.models.teacher import Teacher
from src.school_management.models.subject import Subject
from src.school_management.models.assessment import Assessment
from src.school_management.models.class_group import ClassGroup
from src.school_management.models.lesson import Lesson
from src.school_management.models.schedule import Schedule
from datetime import time

def main():
    class_10a = ClassGroup('10A')
    math = Subject("Matemática")
    teacher = Teacher(2, "Maria Costa", "maria@email.com", "T001", "Matemática")
    class_11a = ClassGroup('11A')

    lessons = [Lesson(
        subject=math,
        teacher=teacher,
        class_group= class_10a,
        day_of_week="Monday",
        start_time= time(9, 0),
        end_time= time(10, 30),),
                Lesson(
                subject=math,   
                teacher=teacher,
                class_group= class_11a,
                day_of_week="Wednesday",
                start_time= time(11, 0),
                end_time= time(12, 30),)
    
]
  
    schedule = Schedule() # create a new schedule
    

    for l in lessons: # for every lesson in the list of lessons, add it to the schedule
        schedule.add_lesson(l) #
        print(l) # print the lesson that was added to the schedule
 

#    student = Student(1, "João Silva", "joao@email.com", "A001", "10A")

#    teacher1 = Teacher(3, "Maria Costa", "maria@email.com", "T002", "Matemática")


#    test_1 = Assessment("Teste 1", "test", 40)
#    test_2 = Assessment("Teste 2", "test", 40)
#    assignment = Assessment("Trabalho 1", "assignment", 20)
#    turma_a = ClassGroup('10 A')

#    teacher.assign_grade(student, math, test_1, 16)
#    teacher.assign_grade(student, math, test_2, 14)
#    teacher.assign_grade(student, math, assignment, 18)

#    turma_a.add_student(student)
#    turma_a.add_teacher(teacher)
#    turma_a.add_teacher(teacher1)

#    students= turma_a.list_students()
#    for s in students:
#        print(s.name)

#    profs= turma_a.list_teachers()
#    for t in profs:
#        print(t.name)

    
    #print("\n--- Grades ---")
    #for grade in student.list_grades():
        #print(grade)

    #print("\n--- Average ---")
   #print(student.calculate_subject_average(math))

if __name__ == "__main__":
    main()
