# core/sdk/__init__.py
"""
SDK Package Initialization

Purpose:
- Expose only public contracts (DTOs, Exceptions, Engine)
- Prevent access to internal Core modules
- Enforce Facade / Gatekeeper pattern
"""

from .engine import BookingEngine
from .dto import *
from .exceptions import *

__all__ = [
    'BookingEngine',
    'BookingDTO',
    'AvailabilityDTO',
    'BookingException',
    # add other public DTOs & exceptions here
]
