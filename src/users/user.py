class User:
    """
    Core User entity.
    Belongs to a single Context.
    """

    def __init__(self, user_id: str, context_id: str):
        self.user_id = user_id
        self.context_id = context_id
