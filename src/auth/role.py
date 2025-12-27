class Role:
    """
    Role entity.
    Belongs to a single Context and holds permissions.
    """

    def __init__(self, role_id: str, context_id: str):
        self.role_id = role_id
        self.context_id = context_id
        self._permissions = []

    def add_permission(self, permission):
        self._permissions.append(permission)

    def has_permission(self, permission_name: str) -> bool:
        return any(
            perm.name == permission_name
            for perm in self._permissions
        )
