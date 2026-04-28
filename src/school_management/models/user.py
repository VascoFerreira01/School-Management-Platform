from src.school_management.auth.permissions import has_permission
from src.school_management.auth.roles import Role

# The class User will be the father class for all the users


class User:
    def __init__(self, user_id: int, name: str, email: str, role: Role):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.role = role
        self.is_active = True

    def can(self, permission: str) -> bool:
        return has_permission(self.role, permission)

    def display_info(self) -> str:
        return f"{self.name} ({self.role.value})"
