"""
Create Booking Use Case
"""

from datetime import date

from core.domain.entities.booking import Booking
from core.domain.repositories.booking_repository import BookingRepository
from core.domain.value_objects.organization_id import OrganizationId
from core.domain.value_objects.user_id import UserId
from core.domain.value_objects.time_slot import TimeSlot
from core.application.use_cases.check_availability import CheckAvailability


class CreateBooking:
    """
    Use case responsible for creating bookings.
    """

    def __init__(
        self,
        repository: BookingRepository,
        availability_checker: CheckAvailability,
    ) -> None:
        self._repository = repository
        self._availability = availability_checker

    def execute(
        self,
        booking_id: str,
        organization_id: str,
        user_id: str,
        booking_date: date,
        slot: TimeSlot,
    ) -> Booking:
        """
        Create a booking if the time slot is available.
        """

        if not booking_id or not booking_id.strip():
            raise ValueError("BookingId cannot be empty")

        org_id = OrganizationId(organization_id)
        uid = UserId(user_id)

        # ✅ Availability check
        if not self._availability.execute(booking_date, slot):
            raise ValueError("Time slot is not available")

        booking = Booking(
            id=booking_id,
            organization_id=org_id.value,
            user_id=uid.value,
            date=booking_date,
            slot=slot,
        )

        self._repository.save(booking)
        return booking
