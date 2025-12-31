import pytest

def test_before_create_hook_is_called():
    from datetime import datetime
    from src.bookings.create_booking import create_booking
    from src.availability.availability import Availability
    from src.bookings.booking_repository import BookingRepository
    from src.rules.booking_rules import BookingRulesService
    from src.auth.authorization_service import AuthorizationService
    from src.users.user import User
    from src.extensions.hook_manager import HookManager

    called = {"before": False}

    def before_create(context, payload):
        called["before"] = True

    hook_manager = HookManager()
    hook_manager.register_before("create_booking", "company_1", before_create)

    availability = Availability(
        "a1", "service_1", "company_1",
        datetime(2025, 1, 1, 9),
        datetime(2025, 1, 1, 15)
    )

    user = User("user_1", "company_1")

    create_booking(
        booking_id="b1",
        context_id="company_1",
        service_id="service_1",
        user=user,
        start_time=datetime(2025, 1, 1, 10),
        end_time=datetime(2025, 1, 1, 11),
        availabilities=[availability],
        booking_repository=BookingRepository(),
        rules_service=BookingRulesService(),
        authorization_service=AuthorizationService(),
        hook_manager=hook_manager
    )

    assert called["before"] is True


def test_before_create_hook_can_block_booking():
    from datetime import datetime
    from src.bookings.create_booking import create_booking
    from src.availability.availability import Availability
    from src.bookings.booking_repository import BookingRepository
    from src.rules.booking_rules import BookingRulesService
    from src.auth.authorization_service import AuthorizationService
    from src.users.user import User
    from src.extensions.hook_manager import HookManager

    def before_create(context, payload):
        raise ValueError("Blocked by hook")

    hook_manager = HookManager()
    hook_manager.register_before("create_booking", "company_1", before_create)

    availability = Availability(
        "a1", "service_1", "company_1",
        datetime(2025, 1, 1, 9),
        datetime(2025, 1, 1, 15)
    )

    user = User("user_1", "company_1")

    with pytest.raises(ValueError):
        create_booking(
            booking_id="b1",
            context_id="company_1",
            service_id="service_1",
            user=user,
            start_time=datetime(2025, 1, 1, 10),
            end_time=datetime(2025, 1, 1, 11),
            availabilities=[availability],
            booking_repository=BookingRepository(),
            rules_service=BookingRulesService(),
            authorization_service=AuthorizationService(),
            hook_manager=hook_manager
        )

def test_after_cancel_hook_is_called():
    from datetime import datetime
    from src.bookings.booking import Booking
    from src.bookings.cancel_booking import cancel_booking
    from src.bookings.booking_repository import BookingRepository
    from src.users.user import User
    from src.extensions.hook_manager import HookManager

    called = {"after": False}

    def after_cancel(context, booking):
        called["after"] = True

    hook_manager = HookManager()
    hook_manager.register_after("cancel_booking", "company_1", after_cancel)

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
        booking_repository=repo,
        hook_manager=hook_manager
    )

    assert called["after"] is True

def test_hook_is_context_isolated():
    from src.extensions.hook_manager import HookManager

    called = {"x": False}

    def hook(context, payload):
        called["x"] = True

    hook_manager = HookManager()
    hook_manager.register_before("create_booking", "company_2", hook)

    hook_manager.run_before("create_booking", "company_1", {})

    assert called["x"] is False
