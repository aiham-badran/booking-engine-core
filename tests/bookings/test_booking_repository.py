from datetime import datetime

def test_booking_repository_isolated_by_context():
    """
    GIVEN bookings from different contexts
    WHEN stored
    THEN they must be isolated by context
    """
    from src.bookings.booking import Booking
    from src.bookings.booking_repository import BookingRepository

    repo = BookingRepository()

    b1 = Booking(
        "b1", "company_1", "service_1", "user_1",
        datetime(2025, 1, 1, 10),
        datetime(2025, 1, 1, 11),
        "CONFIRMED"
    )

    b2 = Booking(
        "b2", "company_2", "service_1", "user_2",
        datetime(2025, 1, 1, 10),
        datetime(2025, 1, 1, 11),
        "CONFIRMED"
    )

    repo.add(b1)
    repo.add(b2)

    company_1_bookings = repo.list_by_context("company_1")

    assert len(company_1_bookings) == 1
    assert company_1_bookings[0].booking_id == "b1"
