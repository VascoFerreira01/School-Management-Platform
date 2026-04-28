from src.school_management.auth.roles import Role

ROLE_PERMISSIONS = {
    Role.ADMIN: [
        "view_all",
        "manage_users",
        "manage_classes",
        "manage_inventory",
        "manage_schedules",
        "manage_grades",
        "manage_attendance",
        "view_reports",
    ],
    Role.TEACHER: [
        "view_students",
        "manage_grades",
        "manage_summaries",
        "view_schedules",
    ],
    Role.EMPLOYEE: ["view_assigned_area",
                     "manage_assigned_area",
                       "view_schedules"],

    Role.STUDENT: ["view_own_grades", 
                   "view_own_attendance", 
                   "view_own_schedule"],
                   
    Role.GUARDIAN: [
        "view_child_grades",
        "view_child_attendance",
        "view_child_schedule",
    ],
}


def has_permission(role: Role, permission: str) -> bool:
    """Check if a role has a specific permission."""
    return permission in ROLE_PERMISSIONS.get(role, [])
