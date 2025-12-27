class AuthorizationService:
    """
    Domain service responsible for permission checks.
    """

    def can(self, user, permission_name: str, context_id: str) -> bool:
        # 1. Context must match
        if user.context_id != context_id:
            return False

        # 2. User must have a role
        role = getattr(user, "role", None)
        if role is None:
            return False

        # 3. Role must belong to the same context
        if role.context_id != context_id:
            return False

        # 4. Role must have permission
        return role.has_permission(permission_name)
