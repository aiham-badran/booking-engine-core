"""
Fake in-memory AvailabilityRepository
"""

class FakeAvailabilityRepository:
    def __init__(self, available_slots):
        self._slots = available_slots

    def get_available_slots(self, organization_id, date):
        return self._slots
