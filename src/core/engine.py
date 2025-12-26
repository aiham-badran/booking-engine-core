class CoreEngine:
    """
    Core Engine.
    Responsible for orchestrating request flow and context resolution.
    """

    def __init__(self, context_registry):
        self._context_registry = context_registry

    def execute(self, context_id: str, operation):
        context = self._context_registry.get(context_id)
        return operation(context)
