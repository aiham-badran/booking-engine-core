import pytest
from datetime import datetime

def test_booking_can_be_rescheduled():
    from src.bookings.booking import Booking

    booking = Booking(
        "b1", "company_1", "service_1", "user_1",
        datetime(2025, 1, 1, 10),
        datetime(2025, 1, 1, 11),
        "CONFIRMED"
    )

    booking.reschedule(
        datetime(2025, 1, 1, 12),
        datetime(2025, 1, 1, 13)
    )

    assert booking.start_time.hour == 12
    assert booking.end_time.hour == 13

def test_owner_can_reschedule_booking():
    from src.bookings.booking import Booking
    from src.bookings.reschedule_booking import reschedule_booking
    from src.bookings.booking_repository import BookingRepository
    from src.rules.booking_rules import BookingRulesService
    from src.users.user import User
    from src.availability.availability import Availability

    availability = Availability(
        "a1", "service_1", "company_1",
        datetime(2025, 1, 1, 9),
        datetime(2025, 1, 1, 15)
    )

    booking = Booking(
        "b1", "company_1", "service_1", "user_1",
        datetime(2025, 1, 1, 10),
        datetime(2025, 1, 1, 11),
        "CONFIRMED"
    )

    repo = BookingRepository()
    repo.add(booking)

    user = User("user_1", "company_1")

    reschedule_booking(
        booking_id="b1",
        user=user,
        new_start_time=datetime(2025, 1, 1, 12),
        new_end_time=datetime(2025, 1, 1, 13),
        booking_repository=repo,
        rules_service=BookingRulesService(),
        availabilities=[availability]
    )

    assert booking.start_time.hour == 12


def test_reschedule_rejected_by_rules():
    from src.bookings.booking import Booking
    from src.bookings.reschedule_booking import reschedule_booking
    from src.bookings.booking_repository import BookingRepository
    from src.rules.booking_rules import BookingRulesService
    from src.users.user import User

    booking = Booking(
        "b1", "company_1", "service_1", "user_1",
        datetime(2025, 1, 1, 10),
        datetime(2025, 1, 1, 11),
        "CONFIRMED"
    )

    repo = BookingRepository()
    repo.add(booking)

    user = User("user_1", "company_1")

    with pytest.raises(ValueError):
        reschedule_booking(
            booking_id="b1",
            user=user,
            new_start_time=datetime(2025, 1, 1, 8),
            new_end_time=datetime(2025, 1, 1, 9),
            booking_repository=repo,
            rules_service=BookingRulesService(),
            availabilities=[]
        )


def test_random_user_cannot_reschedule():
    from src.bookings.booking import Booking
    from src.bookings.reschedule_booking import reschedule_booking
    from src.bookings.booking_repository import BookingRepository
    from src.rules.booking_rules import BookingRulesService
    from src.users.user import User

    booking = Booking(
        "b1", "company_1", "service_1", "user_1",
        datetime(2025, 1, 1, 10),
        datetime(2025, 1, 1, 11),
        "CONFIRMED"
    )

    repo = BookingRepository()
    repo.add(booking)

    random_user = User("user_2", "company_1")

    with pytest.raises(ValueError):
        reschedule_booking(
            booking_id="b1",
            user=random_user,
            new_start_time=datetime(2025, 1, 1, 12),
            new_end_time=datetime(2025, 1, 1, 13),
            booking_repository=repo,
            rules_service=BookingRulesService(),
            availabilities=[]
        )
