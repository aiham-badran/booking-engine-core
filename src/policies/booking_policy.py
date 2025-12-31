class BookingPolicy:
    def __init__(
        self,
        min_duration_minutes: int,
        max_duration_minutes: int,
        buffer_minutes: int,
        allow_same_day_booking: bool,
        cancel_before_minutes: int
    ):
        self.min_duration_minutes = min_duration_minutes
        self.max_duration_minutes = max_duration_minutes
        self.buffer_minutes = buffer_minutes
        self.allow_same_day_booking = allow_same_day_booking
        self.cancel_before_minutes = cancel_before_minutes
