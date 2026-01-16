"""
User Repository Interface
"""

from abc import ABC, abstractmethod
from typing import Optional, List

from core.domain.entities.user import User


class UserRepository(ABC):
    """
    User repository contract.

    Why it exists:
    - Decouples user logic from persistence.
    - Allows multiple storage implementations.
    """

    @abstractmethod
    def save(self, user: User) -> None:
        """
        Persist a user entity.
        """

    @abstractmethod
    def get_by_id(self, user_id: str) -> Optional[User]:
        """
        Retrieve a user by its identifier.
        """

    @abstractmethod
    def get_by_organization(self, organization_id: str) -> List[User]:
        """
        Retrieve all users belonging to an organization.
        """
