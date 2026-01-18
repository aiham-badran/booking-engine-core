# core/domain/entities/booking.py
from dataclasses import dataclass
from core.domain.value_objects.time_slot import TimeSlot
from core.domain.enums.BookingStatus import BookingStatus

class Booking:
    """
    Represents a booking made by a user within an organization.
    """

    def __init__(
        self,
        id: str,
        organization_id: str,
        user_id: str,
        time_slot: TimeSlot,
        status: str = BookingStatus.ACTIVE,
    ):
        self.id = id
        self.organization_id = organization_id
        self.user_id = user_id
        self.time_slot = time_slot
        self.status = status

    def cancel(self):
        self.status = BookingStatus.CANCELLED

    @property
    def is_cancelled(self) -> bool:
        return self.status == BookingStatus.CANCELLED
