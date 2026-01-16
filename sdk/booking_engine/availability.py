from datetime import datetime
from core.domain.value_objects.time_slot import TimeSlot

class AvailabilitySDK:

    def __init__(self, check_uc):
        self._check_uc = check_uc

    def check(self, booking_date, start: str, end: str) -> bool:
        dt = booking_date
        if isinstance(booking_date, str):
            dt = datetime.fromisoformat(booking_date)

        slot = TimeSlot(start, end)

        return self._check_uc.execute(
            dt,
            slot
        )
