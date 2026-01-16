"""
Tests for Organization Module
"""

import unittest
from typing import Optional

from core.domain.entities.organization import Organization
from core.domain.value_objects.organization_id import OrganizationId
from core.domain.repositories.organization_repository import (
    OrganizationRepository,
)
from core.application.use_cases.create_organization import CreateOrganization
from core.application.use_cases.get_organization import GetOrganization


class FakeOrganizationRepository(OrganizationRepository):
    """
    Fake repository used only for testing.
    """

    def __init__(self) -> None:
        self.storage = {}
        self.saved_organization = None

    def save(self, organization: Organization) -> None:
        self.saved_organization = organization
        self.storage[organization.id] = organization

    def get_by_id(self, organization_id: str) -> Optional[Organization]:
        return self.storage.get(organization_id)


class TestOrganizationEntity(unittest.TestCase):

    def test_create_organization_entity(self) -> None:
        org = Organization(
            id="org-1",
            name="Test Org",
            settings={}
        )

        self.assertEqual(org.id, "org-1")
        self.assertEqual(org.name, "Test Org")
        self.assertEqual(org.settings, {})

    def test_organization_is_immutable(self) -> None:
        org = Organization(
            id="org-1",
            name="Test Org",
            settings={}
        )

        with self.assertRaises(Exception):
            org.name = "New Name"


class TestOrganizationId(unittest.TestCase):

    def test_valid_organization_id(self) -> None:
        org_id = OrganizationId("org-1")
        self.assertEqual(org_id.value, "org-1")

    def test_empty_organization_id_raises_error(self) -> None:
        with self.assertRaises(ValueError):
            OrganizationId("")

    def test_whitespace_organization_id_raises_error(self) -> None:
        with self.assertRaises(ValueError):
            OrganizationId("   ")


class TestOrganizationRepositoryContract(unittest.TestCase):

    def test_repository_cannot_be_instantiated(self) -> None:
        with self.assertRaises(TypeError):
            OrganizationRepository()


class TestCreateOrganizationUseCase(unittest.TestCase):

    def test_create_organization_successfully(self) -> None:
        repo = FakeOrganizationRepository()
        use_case = CreateOrganization(repo)

        organization = use_case.execute(
            organization_id="org-1",
            name="Test Org"
        )

        self.assertIsNotNone(organization)
        self.assertEqual(organization.id, "org-1")
        self.assertEqual(repo.saved_organization, organization)

    def test_create_organization_with_empty_id_fails(self) -> None:
        repo = FakeOrganizationRepository()
        use_case = CreateOrganization(repo)

        with self.assertRaises(ValueError):
            use_case.execute("", "Test Org")


class TestGetOrganizationUseCase(unittest.TestCase):

    def test_get_existing_organization(self) -> None:
        repo = FakeOrganizationRepository()
        org = Organization(
            id="org-1",
            name="Test Org",
            settings={}
        )
        repo.save(org)

        use_case = GetOrganization(repo)
        result = use_case.execute("org-1")

        self.assertEqual(result, org)

    def test_get_non_existing_organization_returns_none(self) -> None:
        repo = FakeOrganizationRepository()
        use_case = GetOrganization(repo)

        result = use_case.execute("missing-id")
        self.assertIsNone(result)

    def test_get_organization_with_empty_id_fails(self) -> None:
        repo = FakeOrganizationRepository()
        use_case = GetOrganization(repo)

        with self.assertRaises(ValueError):
            use_case.execute("")
