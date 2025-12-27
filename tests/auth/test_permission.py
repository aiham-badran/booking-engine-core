def test_permission_is_simple_value_object():
    """
    GIVEN a permission
    THEN it should be identified by a name
    """
    from src.auth.permission import Permission

    permission = Permission("create_user")

    assert permission.name == "create_user"
