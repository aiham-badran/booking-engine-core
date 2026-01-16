from datetime import time
from core.domain.value_objects.time_slot import TimeSlot


class WorkingHours:
    """
    Value object representing working hours.
    """

    def __init__(self, start: str, end: str) -> None:
        start_time = self._parse(start)
        end_time = self._parse(end)

        if start_time >= end_time:
            raise ValueError("Start time must be before end time")

        self._start = start_time
        self._end = end_time
        self._slot = TimeSlot(start_time, end_time)

    @property
    def start(self) -> time:
        return self._start

    @property
    def end(self) -> time:
        return self._end

    def contains(self, slot: TimeSlot) -> bool:
        return (
            self._start <= slot.start
            and slot.end <= self._end
        )

    def _parse(self, value: str) -> time:
        if isinstance(value, time):
            return value

        hour, minute = map(int, value.split(":"))
        return time(hour, minute)
