from datetime import datetime

def test_booking_entity_basic_fields():
    """
    GIVEN a booking
    THEN it must contain required core fields
    """
    from src.bookings.booking import Booking

    booking = Booking(
        booking_id="b1",
        context_id="company_1",
        service_id="service_1",
        user_id="user_1",
        start_time=datetime(2025, 1, 1, 10),
        end_time=datetime(2025, 1, 1, 11),
        status="CONFIRMED"
    )

    assert booking.booking_id == "b1"
    assert booking.context_id == "company_1"
    assert booking.service_id == "service_1"
    assert booking.user_id == "user_1"
    assert booking.status == "CONFIRMED"
