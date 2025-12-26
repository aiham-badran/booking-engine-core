class ContextRegistry:
    """
    Stores and resolves contexts.
    """

    def __init__(self):
        self._contexts = {}

    def register(self, context):
        self._contexts[context.context_id] = context

    def get(self, context_id: str):
        try:
            return self._contexts[context_id]
        except KeyError:
            raise KeyError(f"Context '{context_id}' not found")
