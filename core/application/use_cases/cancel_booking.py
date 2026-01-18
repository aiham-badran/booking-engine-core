# core/application/use_cases/cancel_booking.py

from core.domain.entities.booking import Booking


class CancelBookingUseCase:

    def execute(self, booking: Booking) -> None:
        booking.cancel()
