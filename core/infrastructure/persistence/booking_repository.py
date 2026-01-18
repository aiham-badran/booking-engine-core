# core/infrastructure/persistence/booking_repository.py
from abc import ABC, abstractmethod
from core.domain.entities.booking import Booking
from core.domain.value_objects.time_slot import TimeSlot


class BookingRepository(ABC):
    """
    Contract for booking persistence.
    Implemented outside the core.
    """

    @abstractmethod
    def save(self, booking: Booking) -> None:
        pass

    @abstractmethod
    def find_conflicts(
        self,
        organization_id: str,
        time_slot: TimeSlot,
    ) -> list[Booking]:
        pass
