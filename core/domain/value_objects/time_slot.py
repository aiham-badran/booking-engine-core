# core/domain/value_objects/time_slot.py

from datetime import datetime


class TimeSlot:
    """
    Immutable value object representing a time range.
    """

    def __init__(self, start: datetime, end: datetime):
        
        if isinstance(start, str):
            start = datetime.fromisoformat(start)
        if isinstance(end, str):
            end = datetime.fromisoformat(end)
        
        if start >= end:
            raise ValueError("TimeSlot start must be before end")

        self.start = start
        self.end = end

    def overlaps(self, other: "TimeSlot") -> bool:
        return self.start < other.end and other.start < self.end

    def duration_minutes(self) -> int:
        return int((self.end - self.start).total_seconds() / 60)
