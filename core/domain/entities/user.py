# core/domain/entities/user.py

class User:
    """
    Represents a system user.
    A user ALWAYS belongs to an organization.
    """

    def __init__(self, id: str, organization_id: str, role: str):
        self.id = id
        self.organization_id = organization_id
        self.role = role

    def is_admin(self) -> bool:
        return self.role == "admin"
