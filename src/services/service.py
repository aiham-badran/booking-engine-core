class Service:
    """
    Service entity.
    Represents a bookable service within a Context.
    """

    def __init__(self, service_id: str, context_id: str):
        self.service_id = service_id
        self.context_id = context_id
