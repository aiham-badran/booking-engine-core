"""
User Entity
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class User:
    """
    Core User entity.

    Why it exists:
    - Represents a system user.
    - Always belongs to a single organization.

    What it does:
    - Holds user data only.
    - Contains no business logic.
    """
    id: str
    organization_id: str
    name: str
