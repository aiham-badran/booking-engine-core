from datetime import datetime

def test_booking_outside_availability_is_rejected():
    """
    GIVEN a service availability
    WHEN booking is outside availability
    THEN booking should be rejected
    """
    from src.availability.availability import Availability
    from src.rules.booking_rules import BookingRulesService

    availability = Availability(
        "a1", "service_1", "company_1",
        datetime(2025, 1, 1, 10),
        datetime(2025, 1, 1, 12)
    )

    rules = BookingRulesService()

    assert rules.can_book(
        context_id="company_1",
        service_id="service_1",
        start_time=datetime(2025, 1, 1, 9),
        end_time=datetime(2025, 1, 1, 10),
        availabilities=[availability],
        existing_bookings=[]
    ) is False
