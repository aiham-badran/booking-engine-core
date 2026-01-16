"""
BookingType Value Object
"""

from core.domain.enums.booking_type_enum import BookingTypeEnum


class BookingType:
    """
    Value object representing booking type.
    """

    def __init__(self, value: str) -> None:
        try:
            self._value = BookingTypeEnum(value).value
        except ValueError:
            raise ValueError("Invalid booking type")

    @property
    def value(self) -> str:
        return self._value
