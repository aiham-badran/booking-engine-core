"""
Fake in-memory BookingRepository for testing use cases
"""
from core.domain.repositories.booking_repository import BookingRepository


class FakeBookingRepository(BookingRepository):

    def __init__(self):
        self._bookings = []

    def save(self, booking):
        self._bookings.append(booking)

    def exists(self, organization_id, time_slot):
        return any(
            b.organization_id == organization_id
            and b.time_slot.overlaps(time_slot)
            and not b.is_cancelled
            for b in self._bookings
        )

    def get_all(self):
        return self._bookings
