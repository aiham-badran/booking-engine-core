def test_user_repository_stores_users_by_context():
    """
    GIVEN users from different contexts
    WHEN stored in repository
    THEN users must be isolated by context
    """
    from src.users.user import User
    from src.users.user_repository import UserRepository

    repo = UserRepository()

    user_1 = User("user_1", "company_1")
    user_2 = User("user_2", "company_2")

    repo.add(user_1)
    repo.add(user_2)

    company_1_users = repo.list_by_context("company_1")
    company_2_users = repo.list_by_context("company_2")

    assert len(company_1_users) == 1
    assert company_1_users[0].user_id == "user_1"

    assert len(company_2_users) == 1
    assert company_2_users[0].user_id == "user_2"
