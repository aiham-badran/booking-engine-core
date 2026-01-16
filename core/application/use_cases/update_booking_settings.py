"""
Update Booking Settings Use Case
"""

from core.domain.entities.booking_settings import BookingSettings
from core.domain.repositories.settings_repository import SettingsRepository
from core.domain.value_objects.booking_type import BookingType
from core.domain.value_objects.working_day import WorkingDay
from core.domain.value_objects.working_hours import WorkingHours
from core.domain.value_objects.organization_id import OrganizationId


class UpdateBookingSettings:
    """
    Use case responsible for updating booking settings.
    """

    def __init__(self, repository: SettingsRepository) -> None:
        self._repository = repository

    def execute(
        self,
        organization_id: str,
        booking_type: str,
        working_days,
        working_hours,
    ) -> BookingSettings:
        """
        Validate and persist booking settings.
        """
        org_id = OrganizationId(organization_id)
        bt = BookingType(booking_type)

        validated_days = [WorkingDay(day).value for day in working_days]
        validated_hours = [
            (WorkingHours(start, end).start, end)
            for start, end in working_hours
        ]

        settings = BookingSettings(
            organization_id=org_id.value,
            booking_type=bt.value,
            working_days=validated_days,
            working_hours=validated_hours,
        )

        self._repository.save(settings)
        return settings
