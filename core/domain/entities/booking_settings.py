"""
Booking Settings Entity
"""
# core/domain/entities/booking_settings.py

from dataclasses import dataclass
from typing import List

from core.domain.value_objects.booking_type import BookingType
from core.domain.value_objects.working_day import WorkingDay
from core.domain.value_objects.working_hours import WorkingHours


@dataclass(frozen=True)
class BookingSettings:
    organization_id: str
    booking_type: BookingType
    working_days: List[str]
    working_hours: List[WorkingHours]

    def __init__(
        self,
        organization_id: str,
        booking_type: str,
        working_days: list[str],
        working_hours: list[tuple[str, str]],
    ) -> None:
        object.__setattr__(self, "organization_id", organization_id)
        object.__setattr__(self, "booking_type", BookingType(booking_type))
        object.__setattr__(
            self,
            "working_days",
            [WorkingDay(d).value for d in working_days],
        )
        object.__setattr__(
            self,
            "working_hours",
            [WorkingHours(start, end) for start, end in working_hours],
        )
