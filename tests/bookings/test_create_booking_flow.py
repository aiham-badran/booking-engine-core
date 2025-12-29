from datetime import datetime
import pytest

def test_create_booking_public_user_allowed():
    """
    GIVEN user without role
    WHEN booking within availability
    THEN booking should be created (public booking)
    """
    from datetime import datetime
    from src.bookings.create_booking import create_booking
    from src.availability.availability import Availability
    from src.bookings.booking_repository import BookingRepository
    from src.rules.booking_rules import BookingRulesService
    from src.auth.authorization_service import AuthorizationService
    from src.users.user import User

    user = User("user_1", "company_1")  # No role

    availability = Availability(
        "a1", "service_1", "company_1",
        datetime(2025, 1, 1, 10),
        datetime(2025, 1, 1, 12)
    )

    booking = create_booking(
        booking_id="b1",
        context_id="company_1",
        service_id="service_1",
        user=user,
        start_time=datetime(2025, 1, 1, 10),
        end_time=datetime(2025, 1, 1, 11),
        availabilities=[availability],
        booking_repository=BookingRepository(),
        rules_service=BookingRulesService(),
        authorization_service=AuthorizationService()
    )

    assert booking.booking_id == "b1"
    assert booking.context_id == "company_1"

def test_create_booking_with_permission_required():
    """
    GIVEN user with role and booking permission
    WHEN booking
    THEN booking should be allowed
    """
    from datetime import datetime
    from src.bookings.create_booking import create_booking
    from src.availability.availability import Availability
    from src.bookings.booking_repository import BookingRepository
    from src.rules.booking_rules import BookingRulesService
    from src.auth.authorization_service import AuthorizationService
    from src.users.user import User
    from src.auth.role import Role
    from src.auth.permission import Permission

    user = User("user_1", "company_1")
    role = Role("client", "company_1")
    role.add_permission(Permission("book_service"))
    user.role = role

    availability = Availability(
        "a1", "service_1", "company_1",
        datetime(2025, 1, 1, 10),
        datetime(2025, 1, 1, 12)
    )

    booking = create_booking(
        booking_id="b1",
        context_id="company_1",
        service_id="service_1",
        user=user,
        start_time=datetime(2025, 1, 1, 10),
        end_time=datetime(2025, 1, 1, 11),
        availabilities=[availability],
        booking_repository=BookingRepository(),
        rules_service=BookingRulesService(),
        authorization_service=AuthorizationService()
    )

    assert booking.booking_id == "b1"


def test_create_booking_fails_when_rules_reject():
    """
    GIVEN invalid booking time
    WHEN creating booking
    THEN booking should be rejected
    """
    from src.bookings.create_booking import create_booking
    from src.availability.availability import Availability
    from src.bookings.booking_repository import BookingRepository
    from src.rules.booking_rules import BookingRulesService
    from src.auth.authorization_service import AuthorizationService
    from src.users.user import User

    user = User("user_1", "company_1")

    availability = Availability(
        "a1", "service_1", "company_1",
        datetime(2025, 1, 1, 10),
        datetime(2025, 1, 1, 12)
    )

    with pytest.raises(ValueError):
        create_booking(
            booking_id="b1",
            context_id="company_1",
            service_id="service_1",
            user=user,
            start_time=datetime(2025, 1, 1, 9),
            end_time=datetime(2025, 1, 1, 10),
            availabilities=[availability],
            booking_repository=BookingRepository(),
            rules_service=BookingRulesService(),
            authorization_service=AuthorizationService()
        )
