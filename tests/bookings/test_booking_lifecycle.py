import pytest


def test_booking_can_be_cancelled():
    from datetime import datetime
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

    booking.cancel()

    assert booking.status == "CANCELLED"

def test_cancel_already_cancelled_booking_fails():
    from datetime import datetime
    from src.bookings.booking import Booking

    booking = Booking(
        booking_id="b1",
        context_id="company_1",
        service_id="service_1",
        user_id="user_1",
        start_time=datetime(2025, 1, 1, 10),
        end_time=datetime(2025, 1, 1, 11),
        status="CANCELLED"
    )

    with pytest.raises(ValueError):
        booking.cancel()
