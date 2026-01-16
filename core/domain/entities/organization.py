"""
Organization Entity

Represents a single tenant inside the system.
This entity contains no booking or user-related logic.
"""

from dataclasses import dataclass
from typing import Dict


@dataclass(frozen=True)
class Organization:
    """
    Core Organization entity.

    Why it exists:
    - Represents the main tenant boundary in a multi-tenant system.
    - All data (bookings, users, settings) must belong to an organization.

    What it does:
    - Holds organization data only.
    - Contains no business logic.
    """
    id: str
    name: str
    settings: Dict[str, object]
