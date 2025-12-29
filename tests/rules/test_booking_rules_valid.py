from datetime import datetime

def test_booking_is_allowed_inside_availability():
    """
    GIVEN a service availability
    WHEN booking is inside availability and no conflicts
    THEN booking should be allowed
    """
    from src.availability.availability import Availability
    from src.rules.booking_rules import BookingRulesService

    availability = Availability(
        "a1", "service_1", "company_1",
        datetime(2025, 1, 1, 10),
        datetime(2025, 1, 1, 12)
    )

    existing_bookings = []

    rules = BookingRulesService()

    assert rules.can_book(
        context_id="company_1",
        service_id="service_1",
        start_time=datetime(2025, 1, 1, 10),
        end_time=datetime(2025, 1, 1, 11),
        availabilities=[availability],
        existing_bookings=existing_bookings
    ) is True
