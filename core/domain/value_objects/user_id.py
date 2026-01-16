"""
UserId Value Object
"""


class UserId:
    """
    Value object representing a user identifier.

    Why it exists:
    - Prevents invalid user identifiers.
    - Enforces validation at the domain boundary.
    """

    def __init__(self, value: str) -> None:
        if not value or not value.strip():
            raise ValueError("UserId cannot be empty")

        self._value = value

    @property
    def value(self) -> str:
        """
        Returns the raw user ID value.
        """
        return self._value
