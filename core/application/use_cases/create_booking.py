# core/application/use_cases/create_booking.py

import uuid
from core.domain.entities.booking import Booking
from core.domain.repositories.booking_repository import BookingRepository
from core.domain.value_objects.time_slot import TimeSlot
from core.domain.exceptions import BookingConflictError


class CreateBookingUseCase:
    """
    Handles the creation of bookings while enforcing booking rules.
    """

    def __init__(self, booking_repository: BookingRepository):
        self.booking_repository = booking_repository

    def execute(
        self,
        organization_id: str,
        user_id: str,
        time_slot: TimeSlot,
    ) -> Booking:
        """
        Create a booking if the given time slot is available.
        """

        if self.booking_repository.exists(
            organization_id=organization_id,
            time_slot=time_slot,
        ):
            raise BookingConflictError(
                "The selected time slot is already booked."
            )

        booking = Booking(
            id=str(uuid.uuid4()),
            organization_id=organization_id,
            user_id=user_id,
            time_slot=time_slot,
        )

        self.booking_repository.save(booking)
        return booking
