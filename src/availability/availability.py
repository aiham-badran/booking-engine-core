class Availability:
    """
    Availability entity.
    Represents a time slot for a service within a context.
    """

    def __init__(
        self,
        availability_id: str,
        service_id: str,
        context_id: str,
        start_time,
        end_time
    ):
        self.availability_id = availability_id
        self.service_id = service_id
        self.context_id = context_id
        self.start_time = start_time
        self.end_time = end_time
