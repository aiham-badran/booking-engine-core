"""
OrganizationId Value Object
"""


class OrganizationId:
    """
    Value object representing an organization identifier.

    Why it exists:
    - Prevents treating organization IDs as arbitrary strings.
    - Enforces basic validation at the domain level.
    """

    def __init__(self, value: str) -> None:
        if not value or not value.strip():
            raise ValueError("OrganizationId cannot be empty")

        self._value = value

    @property
    def value(self) -> str:
        """
        Returns the raw organization ID value.
        """
        return self._value
