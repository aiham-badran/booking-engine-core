# tests/sdk/test_sdk_behavior.py
import unittest
from datetime import date
from .test_composition import build_test_sdk


class TestBookingEngineSDK(unittest.TestCase):

    def test_full_booking_flow(self):
        organization_id = "org-1"
        client = build_test_sdk()

        client.organizations.create(organization_id, "Hotel")
        client.users.create("user-1", organization_id, "Ahmed")

        client.settings.update(
            organization_id=organization_id,
            booking_type="instant",
            working_days=["mon"],
            working_hours=[("09:00", "17:00")],
        )

        availability = client.availability(organization_id)

        self.assertTrue(
            availability.check(
                booking_date=date(2025, 1, 6),
                start="10:00",
                end="11:00",
            )
        )

        booking = client.bookings.create(
            booking_id="b-1",
            organization_id=organization_id,
            user_id="user-1",
            booking_date=date(2025, 1, 6),
            start="10:00",
            end="11:00",
        )

        self.assertEqual(booking.id, "b-1")
