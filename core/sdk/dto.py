# core/sdk/dto.py

from dataclasses import dataclass
from core.domain.value_objects.time_slot import TimeSlot


@dataclass
class CreateBookingDTO:
    organization_id: str
    user_id: str
    time_slot: TimeSlot 


@dataclass
class CancelBookingDTO:
    booking_id: str
