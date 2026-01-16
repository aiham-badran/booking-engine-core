"""
Settings Repository Interface
"""

from abc import ABC, abstractmethod
from typing import Optional

from core.domain.entities.booking_settings import BookingSettings


class SettingsRepository(ABC):
    """
    Repository contract for booking settings.
    """

    @abstractmethod
    def save(self, settings: BookingSettings) -> None:
        """
        Persist booking settings.
        """

    @abstractmethod
    def get_by_organization(
        self, organization_id: str
    ) -> Optional[BookingSettings]:
        """
        Retrieve booking settings by organization ID.
        """
