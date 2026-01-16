"""
Tests for User Module
"""

import unittest
from typing import Optional, List

from core.domain.entities.user import User
from core.domain.value_objects.user_id import UserId
from core.domain.repositories.user_repository import UserRepository
from core.application.use_cases.create_user import CreateUser
from core.application.use_cases.get_user import GetUser


class FakeUserRepository(UserRepository):
    """
    Fake repository used only for testing.
    """

    def __init__(self) -> None:
        self.storage = {}
        self.saved_user = None

    def save(self, user: User) -> None:
        self.saved_user = user
        self.storage[user.id] = user

    def get_by_id(self, user_id: str) -> Optional[User]:
        return self.storage.get(user_id)

    def get_by_organization(self, organization_id: str) -> List[User]:
        return [
            user for user in self.storage.values()
            if user.organization_id == organization_id
        ]


class TestUserEntity(unittest.TestCase):

    def test_create_user_entity(self) -> None:
        user = User(
            id="user-1",
            organization_id="org-1",
            name="Test User"
        )

        self.assertEqual(user.id, "user-1")
        self.assertEqual(user.organization_id, "org-1")
        self.assertEqual(user.name, "Test User")

    def test_user_is_immutable(self) -> None:
        user = User(
            id="user-1",
            organization_id="org-1",
            name="Test User"
        )

        with self.assertRaises(Exception):
            user.name = "New Name"


class TestUserId(unittest.TestCase):

    def test_valid_user_id(self) -> None:
        user_id = UserId("user-1")
        self.assertEqual(user_id.value, "user-1")

    def test_empty_user_id_raises_error(self) -> None:
        with self.assertRaises(ValueError):
            UserId("")

    def test_whitespace_user_id_raises_error(self) -> None:
        with self.assertRaises(ValueError):
            UserId("   ")


class TestUserRepositoryContract(unittest.TestCase):

    def test_repository_cannot_be_instantiated(self) -> None:
        with self.assertRaises(TypeError):
            UserRepository()


class TestCreateUserUseCase(unittest.TestCase):

    def test_create_user_successfully(self) -> None:
        repo = FakeUserRepository()
        use_case = CreateUser(repo)

        user = use_case.execute(
            user_id="user-1",
            organization_id="org-1",
            name="Test User"
        )

        self.assertIsNotNone(user)
        self.assertEqual(repo.saved_user, user)

    def test_create_user_with_empty_user_id_fails(self) -> None:
        repo = FakeUserRepository()
        use_case = CreateUser(repo)

        with self.assertRaises(ValueError):
            use_case.execute("", "org-1", "Test User")

    def test_create_user_with_empty_organization_id_fails(self) -> None:
        repo = FakeUserRepository()
        use_case = CreateUser(repo)

        with self.assertRaises(ValueError):
            use_case.execute("user-1", "", "Test User")


class TestGetUserUseCase(unittest.TestCase):

    def test_get_existing_user(self) -> None:
        repo = FakeUserRepository()
        user = User(
            id="user-1",
            organization_id="org-1",
            name="Test User"
        )
        repo.save(user)

        use_case = GetUser(repo)
        result = use_case.execute("user-1")

        self.assertEqual(result, user)

    def test_get_non_existing_user_returns_none(self) -> None:
        repo = FakeUserRepository()
        use_case = GetUser(repo)

        result = use_case.execute("missing-id")
        self.assertIsNone(result)

    def test_get_user_with_empty_id_fails(self) -> None:
        repo = FakeUserRepository()
        use_case = GetUser(repo)

        with self.assertRaises(ValueError):
            use_case.execute("")
