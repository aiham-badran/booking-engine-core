def test_user_has_context():
    """
    GIVEN a user
    THEN it must belong to a context
    """
    from src.users.user import User

    user = User(
        user_id="user_1",
        context_id="company_1"
    )

    assert user.user_id == "user_1"
    assert user.context_id == "company_1"
