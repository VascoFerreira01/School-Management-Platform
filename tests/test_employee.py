from src.school_management.models.employee import Employee
import pytest

# checks if employee has assigned area
# can clock in/ clock out
# cant clock out without clock in

def test_employee_has_assigned_area():
    employee = Employee(1, "Ana Santos", "ana@email.com", "E001", "bar")

    assert employee.get_assigned_area() == 'bar'

def test_employee_can_clock_in():   
    employee = Employee(1, "Ana Santos", "ana@email.com", "E001", "bar")

    employee.clock_in()

    assert employee.is_working is True
    assert len(employee.get_work_log()) == 1

def test_employee_can_clock_out():
    employee = Employee(1, "Ana Santos", "ana@email.com", "E001", "bar")

    employee.clock_in()
    employee.clock_out()

    assert employee.is_working is False
    assert employee.get_work_log()[0]['end'] is not None 
    # 0 means that we re accessing to the first element of the work log list(only we have)
    # 'end' is used to access the end time of the work log entry
    # is not True is used to grant that the end time is not None and that the employee has clocked out 

def test_employee_cannot_clock_out_without_clock_in():
    employee = Employee(1, "Ana Santos", "ana@email.com", "E001", "bar")

    with pytest.raises(ValueError):
        employee.clock_out()
