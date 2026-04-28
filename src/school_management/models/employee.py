from datetime import datetime

from src.school_management.auth.roles import Role
from src.school_management.models.user import User


class Employee(User):

    def __init__(
        self,
        user_id: int,
        name: str,
        email: str,
        employee_number: str,
        assigned_area: str,
    ):
        super().__init__(user_id, name, email, Role.EMPLOYEE)
        self.employee_number = employee_number
        self.assigned_area = assigned_area
        self.is_working = False # starts as not working because the employee has not clocked in yet
        self.work_log = []

#clock in and clock out
#get_work_log
#get_assigned_area

    def clock_in(self):

        if self.is_working: #check if the employee is already working, if so, raise an error
            raise(ValueError("Employee is already clocked in"))
        
        self.is_working = True
        self.work_log.append({'start' : datetime.now(), 'end': None})

    def clock_out(self):
        
        if not self.is_working: #check if the employee is not working, if so, raise an error 
            raise(ValueError('Employee is not working'))
        
        self.is_working = False
        self.work_log[-1]['end'] = datetime.now() #-1 is used to access the last element of the list
                                                  # 'end' is used to update the end time of the last work log entry 
                                                  # if we used 'start' we would be updating the last element in the start time instead of the end time

    def get_work_log(self):

        return self.work_log
    
    def get_assigned_area(self):
        return self.assigned_area