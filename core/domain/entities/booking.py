"""
Booking Entity
"""

from dataclasses import dataclass
from datetime import datetime

from core.domain.value_objects.time_slot import TimeSlot


@dataclass(frozen=True)
class Booking:
    """
    Booking entity.

    Why it exists:
    - Represents a confirmed booking.
    - Links organization, user, date and time slot.
    """
    id: str
    organization_id: str
    user_id: str
    date: datetime
    slot: TimeSlot
