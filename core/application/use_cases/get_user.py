"""
Get User Use Case
"""

from typing import Optional

from core.domain.entities.user import User
from core.domain.repositories.user_repository import UserRepository
from core.domain.value_objects.user_id import UserId


class GetUser:
    """
    Use case responsible for retrieving users.

    Why it exists:
    - Provides a controlled access point for user retrieval.
    """

    def __init__(self, repository: UserRepository) -> None:
        self._repository = repository

    def execute(self, user_id: str) -> Optional[User]:
        """
        Retrieve a user by its identifier.
        """
        uid = UserId(user_id)
        return self._repository.get_by_id(uid.value)
