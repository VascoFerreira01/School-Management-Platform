# roles of users in the school management platform

from enum import Enum


class Role(Enum):
    ADMIN = "admin"
    TEACHER = "teacher"
    STUDENT = "student"
    EMPLOYEE = "employee"
    GUARDIAN = "guardian"
