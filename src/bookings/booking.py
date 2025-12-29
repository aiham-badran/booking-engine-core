class Booking:
    def __init__(
        self,
        booking_id: str,
        context_id: str,
        service_id: str,
        user_id: str,
        start_time,
        end_time,
        status: str
    ):
        self.booking_id = booking_id
        self.context_id = context_id
        self.service_id = service_id
        self.user_id = user_id
        self.start_time = start_time
        self.end_time = end_time
        self.status = status
