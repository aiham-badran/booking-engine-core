"""
Tests for Booking Module
"""

import unittest
from datetime import datetime, time,date
from typing import Optional

from core.domain.entities.booking import Booking
from core.domain.repositories.booking_repository import BookingRepository
from core.application.use_cases.create_booking import CreateBooking
from core.application.use_cases.get_booking import GetBooking
from core.domain.value_objects.time_slot import TimeSlot
from core.domain.entities.booking_settings import BookingSettings
from core.application.use_cases.check_availability import CheckAvailability



class FakeBookingRepository(BookingRepository):
    """
    Fake booking repository for testing.
    """

    def __init__(self) -> None:
        self.storage = {}
        self.saved_booking = None

    def save(self, booking: Booking) -> None:
        self.saved_booking = booking
        self.storage[booking.id] = booking

    def get_by_id(self, booking_id: str) -> Optional[Booking]:
        return self.storage.get(booking_id)


class TestBookingEntity(unittest.TestCase):

    def test_create_booking_entity(self) -> None:
        slot = TimeSlot(time(10, 0), time(11, 0))
        booking = Booking(
            id="booking-1",
            organization_id="org-1",
            user_id="user-1",
            date=datetime(2025, 1, 6),
            slot=slot,
        )

        self.assertEqual(booking.organization_id, "org-1")
        self.assertEqual(booking.user_id, "user-1")

    def test_booking_is_immutable(self) -> None:
        slot = TimeSlot(time(10, 0), time(11, 0))
        booking = Booking(
            id="booking-1",
            organization_id="org-1",
            user_id="user-1",
            date=datetime(2025, 1, 6),
            slot=slot,
        )

        with self.assertRaises(Exception):
            booking.user_id = "user-2"


class TestBookingRepositoryContract(unittest.TestCase):

    def test_repository_cannot_be_instantiated(self) -> None:
        with self.assertRaises(TypeError):
            BookingRepository()


class TestCreateBookingUseCase(unittest.TestCase):

    def setUp(self) -> None:
        self.settings = BookingSettings(
            organization_id="org-1",
            booking_type="instant",
            working_days=["mon"],
            working_hours=[("09:00", "17:00")],
        )

        self.availability = CheckAvailability(self.settings)
        self.repo = FakeBookingRepository()
        self.use_case = CreateBooking(
            repository=self.repo,
            availability_checker=self.availability
        )

    def test_create_booking_when_available(self) -> None:
        slot = TimeSlot(time(10, 0), time(11, 0))
        booking = self.use_case.execute(
            booking_id="booking-1",
            organization_id="org-1",
            user_id="user-1",
            booking_date=date(2025, 1, 6),
            slot=slot,
        )

        self.assertIsNotNone(booking)
        self.assertEqual(self.repo.saved_booking, booking)

    def test_create_booking_when_not_available_fails(self) -> None:
        slot = TimeSlot(time(18, 0), time(19, 0))

        with self.assertRaises(ValueError):
            self.use_case.execute(
                booking_id="booking-1",
                organization_id="org-1",
                user_id="user-1",
                booking_date=date(2025, 1, 6),
                slot=slot,
            )


class TestGetBookingUseCase(unittest.TestCase):

    def test_get_existing_booking(self) -> None:
        repo = FakeBookingRepository()
        slot = TimeSlot(time(10, 0), time(11, 0))
        booking = Booking(
            id="booking-1",
            organization_id="org-1",
            user_id="user-1",
            date=datetime(2025, 1, 6),
            slot=slot,
        )
        repo.save(booking)

        use_case = GetBooking(repo)
        result = use_case.execute("booking-1")

        self.assertEqual(result, booking)

    def test_get_non_existing_booking_returns_none(self) -> None:
        repo = FakeBookingRepository()
        use_case = GetBooking(repo)

        result = use_case.execute("missing-id")
        self.assertIsNone(result)
