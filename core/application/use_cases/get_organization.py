"""
Get Organization Use Case
"""

from typing import Optional

from core.domain.entities.organization import Organization
from core.domain.repositories.organization_repository import (
    OrganizationRepository,
)
from core.domain.value_objects.organization_id import OrganizationId


class GetOrganization:
    """
    Use case responsible for retrieving organizations.

    Why it exists:
    - Provides a controlled access point for organization retrieval.
    - Validates organization identity before querying the repository.
    """

    def __init__(self, repository: OrganizationRepository) -> None:
        self._repository = repository

    def execute(self, organization_id: str) -> Optional[Organization]:
        """
        Retrieve an organization by its identifier.
        """
        org_id = OrganizationId(organization_id)
        return self._repository.get_by_id(org_id.value)
