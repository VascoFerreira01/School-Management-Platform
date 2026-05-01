from datetime import time

class Lesson:
    def __init__(
            self,
            subject, 
            teacher, 
            class_group, 
            day_of_week: str, 
            start_time:time, 
            end_time: time,
            ):
        
        if not day_of_week:
            raise ValueError('Day of week cannot be empty')
        
        if start_time >= end_time:
            raise ValueError('Start time must be before end time')
        
        self.subject = subject
        self.teacher = teacher
        self.class_group = class_group
        self.day_of_week = day_of_week
        self.start_time = start_time
        self.end_time = end_time

    def __str__(self) -> str:
        return ( f'Day: {self.day_of_week} | start: {self.start_time} |  end: {self.end_time}' '\n'
                 f'Subject: {self.subject.name} | Teacher: {self.teacher.name} | Class Group: {self.class_group.name}')