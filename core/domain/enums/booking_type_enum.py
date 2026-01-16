"""
BookingType Enum
"""

from enum import Enum


class BookingTypeEnum(str, Enum):
    """
    Enum representing allowed booking types.
    """

    INSTANT = "instant"
    SCHEDULED = "scheduled"
