"""
Booking Repository Interface
"""

from abc import ABC, abstractmethod
from typing import Optional

from core.domain.entities.booking import Booking


class BookingRepository(ABC):
    """
    Repository contract for bookings.
    """

    @abstractmethod
    def save(self, booking: Booking) -> None:
        """
        Persist a booking.
        """

    @abstractmethod
    def get_by_id(self, booking_id: str) -> Optional[Booking]:
        """
        Retrieve a booking by its identifier.
        """
