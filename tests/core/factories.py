# tests/core/factories.py

from core.domain.entities.booking_settings import BookingSettings


def make_booking_settings():
    return BookingSettings(
        organization_id="org-1",
        booking_type="instant",
        working_days=["mon"],
        working_hours=[("09:00", "17:00")],
    )
