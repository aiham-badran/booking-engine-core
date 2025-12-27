def test_role_belongs_to_context():
    """
    GIVEN a role
    THEN it must belong to a context
    """
    from src.auth.role import Role

    role = Role(
        role_id="admin",
        context_id="company_1"
    )

    assert role.role_id == "admin"
    assert role.context_id == "company_1"
