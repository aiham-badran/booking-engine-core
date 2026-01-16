"""
Create Organization Use Case
"""

from core.domain.entities.organization import Organization
from core.domain.repositories.organization_repository import (
    OrganizationRepository,
)
from core.domain.value_objects.organization_id import OrganizationId


class CreateOrganization:
    """
    Use case responsible for creating new organizations.

    Why it exists:
    - Enforces a single controlled entry point for organization creation.
    - Validates organization identity before creation.
    """

    def __init__(self, repository: OrganizationRepository) -> None:
        self._repository = repository

    def execute(self, organization_id: str, name: str) -> Organization:
        """
        Create and persist a new organization.
        """
        org_id = OrganizationId(organization_id)

        organization = Organization(
            id=org_id.value,
            name=name,
            settings={},
        )

        self._repository.save(organization)
        return organization
