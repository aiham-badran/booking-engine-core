"""
Check Availability Use Case
"""

from datetime import date
from core.domain.entities.booking_settings import BookingSettings
from core.domain.value_objects.time_slot import TimeSlot

class CheckAvailability:
    def __init__(self, settings: BookingSettings):
        self._settings = settings

    def execute(self, booking_date: date, slot: TimeSlot) -> bool:
        if not self._is_working_day(booking_date):
            return False

        if not self._is_within_working_hours(slot):
            return False

        return True

    def _is_working_day(self, booking_date: date) -> bool:
        day = booking_date.strftime("%a").lower()[:3]
        return day in self._settings.working_days

    def _is_within_working_hours(self, slot: TimeSlot) -> bool:
        return any(
            hours.contains(slot)
            for hours in self._settings.working_hours
        )