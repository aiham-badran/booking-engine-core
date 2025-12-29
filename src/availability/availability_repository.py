class AvailabilityRepository:
    """
    In-memory repository for Availability slots.
    """

    def __init__(self):
        self._availabilities = []

    def add(self, availability):
        self._availabilities.append(availability)

    def list(self, context_id: str, service_id: str):
        return [
            availability for availability in self._availabilities
            if availability.context_id == context_id
            and availability.service_id == service_id
        ]
