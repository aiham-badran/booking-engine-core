from datetime import datetime

def test_booking_conflict_is_rejected():
    """
    GIVEN an existing booking
    WHEN new booking overlaps
    THEN booking should be rejected
    """
    from src.rules.booking_rules import BookingRulesService

    existing_booking = {
        "start_time": datetime(2025, 1, 1, 10),
        "end_time": datetime(2025, 1, 1, 11),
    }

    rules = BookingRulesService()

    assert rules.can_book(
        context_id="company_1",
        service_id="service_1",
        start_time=datetime(2025, 1, 1, 10, 30),
        end_time=datetime(2025, 1, 1, 11, 30),
        availabilities=[],
        existing_bookings=[existing_booking]
    ) is False
