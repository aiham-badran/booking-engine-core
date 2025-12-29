class BookingRepository:
    def __init__(self):
        self._bookings = []

    def add(self, booking):
        self._bookings.append(booking)

    def list_by_context(self, context_id: str):
        return [
            booking
            for booking in self._bookings
            if booking.context_id == context_id
        ]
