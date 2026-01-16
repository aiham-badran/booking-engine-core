"""
TimeSlot Value Object
"""
from datetime import time


class TimeSlot:
    """
    Value Object representing a time slot.
    """

    def __init__(self, start, end) -> None:
        self._start = self._parse(start)
        self._end = self._parse(end)

        if self._start >= self._end:
            raise ValueError("Start time must be before end time")

    @property
    def start(self) -> time:
        return self._start

    @property
    def end(self) -> time:
        return self._end

    def _parse(self, value) -> time:
        if isinstance(value, time):
            return value

        if isinstance(value, str):
            hour, minute = map(int, value.split(":"))
            return time(hour, minute)

        raise ValueError("Invalid time value")
