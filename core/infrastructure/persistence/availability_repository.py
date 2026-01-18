# core/infrastructure/persistence/availability_repository.py

from typing import List
from core.domain.value_objects.time_slot import TimeSlot


class AvailabilityRepository:
    """
    Provides base availability slots (working hours, schedules).
    """

    def get_daily_slots(self, organization_id: str, target_date):
        raise NotImplementedError
