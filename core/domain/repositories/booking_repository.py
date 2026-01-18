"""
Booking Repository Interface
"""

from abc import ABC, abstractmethod
from core.domain.value_objects.time_slot import TimeSlot

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
    def exists(self, organization_id: str, time_slot: TimeSlot) -> bool:
        pass