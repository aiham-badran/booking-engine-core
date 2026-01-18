# core/domain/policies/booking_policy.py

class BookingConflictError(Exception):
    pass


class BookingPolicy:
    """
    Business rules related to booking validation.
    """

    @staticmethod
    def ensure_no_conflicts(existing_bookings, new_time_slot):
        for booking in existing_bookings:
            if not booking.is_active():
                continue

            if booking.time_slot.overlaps(new_time_slot):
                raise BookingConflictError(
                    "Booking time conflicts with an existing booking"
                )
