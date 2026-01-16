"""
WorkingDay Value Object
"""


class WorkingDay:
    """
    Value object representing a working day.
    """

    _allowed_days = {
        "mon", "tue", "wed", "thu", "fri", "sat", "sun"
    }

    def __init__(self, value: str) -> None:
        if value not in self._allowed_days:
            raise ValueError("Invalid working day")

        self._value = value

    @property
    def value(self) -> str:
        return self._value
