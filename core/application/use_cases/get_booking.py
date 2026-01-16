"""
Get Booking Use Case
"""

from typing import Optional

from core.domain.entities.booking import Booking
from core.domain.repositories.booking_repository import BookingRepository


class GetBooking:
    """
    Use case responsible for retrieving bookings.
    """

    def __init__(self, repository: BookingRepository) -> None:
        self._repository = repository

    def execute(self, booking_id: str) -> Optional[Booking]:
        """
        Retrieve a booking by its identifier.
        """
        if not booking_id or not booking_id.strip():
            raise ValueError("BookingId cannot be empty")

        return self._repository.get_by_id(booking_id)
