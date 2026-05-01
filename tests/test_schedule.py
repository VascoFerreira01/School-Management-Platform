import pytest
from datetime import time

from src.school_management.models.schedule import Schedule
from src.school_management.models.lesson import Lesson
from src.school_management.models.subject import Subject
from src.school_management.models.teacher import Teacher 
from src.school_management.models.class_group import ClassGroup

#create_sample_lesson
def create_sample_lesson():
    subject = Subject("Math")
    teacher = Teacher(1, "Maria", "m@email.com", "T001", "Math")
    class_group = ClassGroup("10A")

    return Lesson(
        subject,
        teacher, 
        class_group,
        'Monday', 
        time(9,0),
        time (10, 0),
    )

def test_schedule_add_lesson():
    schedule = Schedule() #creates a blank new schedule
    lesson = create_sample_lesson () # creates a blank lesson with the create_sample_lesson function

    schedule.add_lesson(lesson)

    assert lesson in schedule.list_lessons() # checks if the lesson created was added to the schedule lessons list (self.lessons) using add_lesson method

def test_schedule_cannot_add_duplicate_lesson():
    schedule = Schedule()
    lesson = create_sample_lesson()
    schedule.add_lesson(lesson)

    with pytest.raises(ValueError):
        schedule.add_lesson(lesson)

def test_get_lessons_by_day():
    schedule = Schedule()

    lesson1= create_sample_lesson()
    lesson2 = create_sample_lesson()

    lesson2.day_of_week = 'Tuesday'

    schedule.add_lesson(lesson1)
    schedule.add_lesson(lesson2)

    monday_lessons= schedule.get_lessons_by_day('Monday')

    assert lesson1 in monday_lessons
    assert lesson2 not in monday_lessons