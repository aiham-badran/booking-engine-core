# core/application/use_cases/get_booking_settings.py

from core.domain.repositories.settings_repository import SettingsRepository
from core.domain.entities.booking_settings import BookingSettings


class GetBookingSettings:
    def __init__(self, repository: SettingsRepository):
        self._repository = repository

    def execute(self, organization_id: str) -> BookingSettings:
        if not organization_id or not organization_id.strip():
            raise ValueError("OrganizationId cannot be empty")

        return self._repository.get_by_organization(organization_id)
