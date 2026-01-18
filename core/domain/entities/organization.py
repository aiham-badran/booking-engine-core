# core/domain/entities/organization.py

class Organization:
    """
    Represents a tenant in the booking engine.
    All data in the system MUST belong to an organization.
    """

    def __init__(self, id: str, name: str, timezone: str):
        self.id = id
        self.name = name
        self.timezone = timezone

    def __eq__(self, other):
        return isinstance(other, Organization) and self.id == other.id
