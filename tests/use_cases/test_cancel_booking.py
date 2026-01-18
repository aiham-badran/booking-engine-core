import unittest
from datetime import datetime
from core.application.use_cases.cancel_booking import CancelBookingUseCase
from core.domain.entities.booking import Booking
from core.domain.value_objects.time_slot import TimeSlot


class TestCancelBookingUseCase(unittest.TestCase):

    def test_cancel_booking(self):
        booking = Booking(
            id="1",
            organization_id="org",
            user_id="user",
            time_slot=TimeSlot(
                start=datetime(2026, 1, 1, 10, 0),
                end=datetime(2026, 1, 1, 11, 0)
            ),
        )

        CancelBookingUseCase().execute(booking)

        self.assertTrue(booking.is_cancelled)
