class Context:
    """
    Context entity.
    Represents an isolated application or company.
    """

    def __init__(self, context_id: str):
        if not context_id:
            raise ValueError("context_id must not be empty")

        self.context_id = context_id
