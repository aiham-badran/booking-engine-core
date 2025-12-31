import pytest
from datetime import datetime


def test_owner_can_cancel_booking():
    from src.bookings.booking import Booking
    from src.bookings.cancel_booking import cancel_booking
    from src.bookings.booking_repository import BookingRepository
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

    cancel_booking(
        booking_id="b1",
        user=user,
        booking_repository=repo
    )

    assert booking.status == "CANCELLED"

def test_context_admin_can_cancel_booking():
    from src.bookings.booking import Booking
    from src.bookings.cancel_booking import cancel_booking
    from src.bookings.booking_repository import BookingRepository
    from src.users.user import User
    from src.auth.role import Role
    from src.auth.permission import Permission

    booking = Booking(
        "b1", "company_1", "service_1", "user_1",
        datetime(2025, 1, 1, 10),
        datetime(2025, 1, 1, 11),
        "CONFIRMED"
    )

    repo = BookingRepository()
    repo.add(booking)

    admin = User("admin_1", "company_1")
    role = Role("admin", "company_1")
    role.add_permission(Permission("manage_bookings"))
    admin.role = role

    cancel_booking(
        booking_id="b1",
        user=admin,
        booking_repository=repo
    )

    assert booking.status == "CANCELLED"



def test_random_user_cannot_cancel_booking():
    from src.bookings.booking import Booking
    from src.bookings.cancel_booking import cancel_booking
    from src.bookings.booking_repository import BookingRepository
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
        cancel_booking(
            booking_id="b1",
            user=random_user,
            booking_repository=repo
        )
