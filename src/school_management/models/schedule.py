class Schedule:

    def __init__(self):
        self.lessons = []
    
    def add_lesson(self, lesson):
        if lesson in self.lessons:
                raise ValueError('Lesson already exists in schedule')
        self.lessons.append(lesson)

    def list_lessons(self):
        return self.lessons
    
    def get_lessons_by_day(self, day: str):
         return [lesson for lesson in self.lessons if lesson.day_of_week == day] 
    # create a list of lessons that are in self.lessons, only if the day  of the week is equal to the day that i asked
    
    def __str__(self):
         return '\n'.join(str(lesson) for lesson in self.lessons) # for every lesson in self.lessons, convert it to a string and join them with a new line character
    # create a string representation of the schedule by joining the string representation of each lesson with a new line character
    # self.lessons would be for example lesson = Lesson(subject, teacher, class_group, day_of_week, start_time, end_time) 
    # all those attributes would be printed in a single string 