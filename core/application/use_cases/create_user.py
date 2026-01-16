"""
Create User Use Case
"""

from core.domain.entities.user import User
from core.domain.repositories.user_repository import UserRepository
from core.domain.value_objects.user_id import UserId
from core.domain.value_objects.organization_id import OrganizationId


class CreateUser:
    """
    Use case responsible for creating users.

    Why it exists:
    - Enforces controlled user creation.
    - Validates user and organization identity.
    """

    def __init__(self, repository: UserRepository) -> None:
        self._repository = repository

    def execute(
        self,
        user_id: str,
        organization_id: str,
        name: str,
    ) -> User:
        """
        Create and persist a new user.
        """
        uid = UserId(user_id)
        org_id = OrganizationId(organization_id)

        user = User(
            id=uid.value,
            organization_id=org_id.value,
            name=name,
        )

        self._repository.save(user)
        return user
