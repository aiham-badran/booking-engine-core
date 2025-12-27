class UserRepository:
    """
    In-memory repository for Users.
    Users are isolated by context.
    """

    def __init__(self):
        self._users = []

    def add(self, user):
        self._users.append(user)

    def list_by_context(self, context_id: str):
        return [
            user for user in self._users
            if user.context_id == context_id
        ]
