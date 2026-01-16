"""
Tests for Availability Module
"""

import unittest
from datetime import date, time
from tests.core.factories import make_booking_settings

from core.domain.value_objects.time_slot import TimeSlot
from core.application.use_cases.check_availability import CheckAvailability
from core.domain.entities.booking_settings import BookingSettings


class TestTimeSlotValueObject(unittest.TestCase):

    def test_create_valid_time_slot(self) -> None:
        slot = TimeSlot(
            start=time(10, 0),
            end=time(11, 0),
        )
        self.assertEqual(slot.start, time(10, 0))

    def test_start_after_end_raises_error(self) -> None:
        with self.assertRaises(ValueError):
            TimeSlot(
                start=time(12, 0),
                end=time(11, 0),
            )


class TestCheckAvailabilityUseCase(unittest.TestCase):

    def setUp(self) -> None:
        self.settings = make_booking_settings()
        self.use_case = CheckAvailability(self.settings)

        self.use_case = CheckAvailability(self.settings)

    def test_time_inside_working_hours_is_available(self) -> None:
        slot = TimeSlot("10:00", "11:00")
        self.assertTrue(self.use_case.execute(date(2025, 1, 6), slot))

    def test_time_outside_working_hours_is_not_available(self):
        slot = TimeSlot("18:00", "19:00")
        self.assertFalse(self.use_case.execute(date(2025, 1, 6), slot))