"""
Organization Repository Interface
"""

from abc import ABC, abstractmethod
from typing import Optional
from core.domain.entities.organization import Organization


class OrganizationRepository(ABC):
    """
    Organization repository contract.

    Why it exists:
    - Decouples the core domain from persistence details.
    - Allows any storage implementation without changing the core.
    """

    @abstractmethod
    def save(self, organization: Organization) -> None:
        """
        Persist an organization entity.
        """

    @abstractmethod
    def get_by_id(self, organization_id: str) -> Optional[Organization]:
        """
        Retrieve an organization by its identifier.
        """
