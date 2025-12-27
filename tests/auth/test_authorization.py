def test_role_has_permissions():
    """
    GIVEN a role with permissions
    THEN it should expose them correctly
    """
    from src.auth.role import Role
    from src.auth.permission import Permission

    role = Role("admin", "company_1")
    perm_create = Permission("create_user")
    perm_delete = Permission("delete_user")

    role.add_permission(perm_create)
    role.add_permission(perm_delete)

    assert role.has_permission("create_user") is True
    assert role.has_permission("delete_user") is True
    assert role.has_permission("unknown") is False

def test_authorization_checks_context_and_permission():
    """
    GIVEN a user with a role
    WHEN checking permission in correct context
    THEN access should be granted
    """
    from src.users.user import User
    from src.auth.role import Role
    from src.auth.permission import Permission
    from src.auth.authorization_service import AuthorizationService

    user = User("user_1", "company_1")

    role = Role("admin", "company_1")
    role.add_permission(Permission("create_user"))

    user.role = role

    auth = AuthorizationService()

    assert auth.can(
        user=user,
        permission_name="create_user",
        context_id="company_1"
    ) is True

def test_authorization_fails_on_context_mismatch():
    """
    GIVEN a user with role in one context
    WHEN checking permission in another context
    THEN access should be denied
    """
    from src.users.user import User
    from src.auth.role import Role
    from src.auth.permission import Permission
    from src.auth.authorization_service import AuthorizationService

    user = User("user_1", "company_1")

    role = Role("admin", "company_1")
    role.add_permission(Permission("create_user"))

    user.role = role

    auth = AuthorizationService()

    assert auth.can(
        user=user,
        permission_name="create_user",
        context_id="company_2"
    ) is False
