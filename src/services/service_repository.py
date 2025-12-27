class ServiceRepository:
    """
    In-memory repository for Services.
    Services are isolated by context.
    """

    def __init__(self):
        self._services = []

    def add(self, service):
        self._services.append(service)

    def list_by_context(self, context_id: str):
        return [
            service for service in self._services
            if service.context_id == context_id
        ]
