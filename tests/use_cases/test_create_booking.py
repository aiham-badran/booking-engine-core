import unittest
from datetime import datetime
from core.application.use_cases.create_booking import CreateBookingUseCase
from core.domain.value_objects.time_slot import TimeSlot
from tests.fakes.fake_booking_repository import FakeBookingRepository
from core.domain.exceptions import BookingConflictError


class TestCreateBookingUseCase(unittest.TestCase):

    def setUp(self):
        self.booking_repo = FakeBookingRepository()
        self.use_case = CreateBookingUseCase(self.booking_repo)

    def test_create_booking_successfully(self):
        slot = TimeSlot(
            start=datetime(2026, 1, 1, 10, 0),
            end=datetime(2026, 1, 1, 11, 0)
        )

        booking = self.use_case.execute("org1", "user1", slot)

        self.assertEqual(len(self.booking_repo.get_all()), 1)
        self.assertFalse(getattr(booking, "is_cancelled", False))

    def test_cannot_book_same_slot_twice(self):
        slot = TimeSlot(
            start=datetime(2026, 1, 1, 10, 0),
            end=datetime(2026, 1, 1, 11, 0)
        )

        self.use_case.execute("org1", "user1", slot)

        with self.assertRaises(BookingConflictError):
            self.use_case.execute("org1", "user2", slot)
