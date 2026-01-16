"""
Tests for Settings Module
"""

import unittest
from typing import Optional
from datetime import time

from core.domain.entities.booking_settings import BookingSettings
from core.domain.value_objects.booking_type import BookingType
from core.domain.value_objects.working_day import WorkingDay
from core.domain.value_objects.working_hours import WorkingHours
from core.domain.repositories.settings_repository import SettingsRepository
from core.application.use_cases.update_booking_settings import (
    UpdateBookingSettings,
)
from core.application.use_cases.get_booking_settings import (
    GetBookingSettings,
)


class FakeSettingsRepository(SettingsRepository):
    """
    Fake repository used only for testing.
    """

    def __init__(self) -> None:
        self.storage = {}
        self.saved_settings = None

    def save(self, settings: BookingSettings) -> None:
        self.saved_settings = settings
        self.storage[settings.organization_id] = settings

    def get_by_organization(
        self, organization_id: str
    ) -> Optional[BookingSettings]:
        return self.storage.get(organization_id)


class TestBookingSettingsEntity(unittest.TestCase):

    def test_create_booking_settings_entity(self) -> None:
        settings = BookingSettings(
            organization_id="org-1",
            booking_type="instant",
            working_days=["mon", "tue"],
            working_hours=[("09:00", "17:00")],
        )

        self.assertEqual(settings.organization_id, "org-1")
        self.assertEqual(settings.booking_type.value, "instant")

    def test_booking_settings_is_immutable(self) -> None:
        settings = BookingSettings(
            organization_id="org-1",
            booking_type="instant",
            working_days=["mon"],
            working_hours=[("09:00", "17:00")],
        )

        with self.assertRaises(Exception):
            settings.booking_type = "scheduled"


class TestBookingTypeValueObject(unittest.TestCase):

    def test_valid_booking_type(self) -> None:
        booking_type = BookingType("instant")
        self.assertEqual(booking_type.value, "instant")

    def test_invalid_booking_type_raises_error(self) -> None:
        with self.assertRaises(ValueError):
            BookingType("invalid")


class TestWorkingDayValueObject(unittest.TestCase):

    def test_valid_working_day(self) -> None:
        day = WorkingDay("mon")
        self.assertEqual(day.value, "mon")

    def test_invalid_working_day_raises_error(self) -> None:
        with self.assertRaises(ValueError):
            WorkingDay("xxx")


class TestWorkingHoursValueObject(unittest.TestCase):

    def test_valid_working_hours(self) -> None:
        hours = WorkingHours("09:00", "17:00")
        self.assertEqual(hours.start,time(9))

    def test_start_after_end_raises_error(self) -> None:
        with self.assertRaises(ValueError):
            WorkingHours("18:00", "17:00")


class TestSettingsRepositoryContract(unittest.TestCase):

    def test_repository_cannot_be_instantiated(self) -> None:
        with self.assertRaises(TypeError):
            SettingsRepository()


class TestUpdateBookingSettingsUseCase(unittest.TestCase):

    def test_update_settings_successfully(self) -> None:
        repo = FakeSettingsRepository()
        use_case = UpdateBookingSettings(repo)

        settings = use_case.execute(
            organization_id="org-1",
            booking_type="instant",
            working_days=["mon"],
            working_hours=[("09:00", "17:00")],
        )

        self.assertIsNotNone(settings)
        self.assertEqual(repo.saved_settings, settings)


class TestGetBookingSettingsUseCase(unittest.TestCase):

    def test_get_existing_settings(self) -> None:
        repo = FakeSettingsRepository()
        settings = BookingSettings(
            organization_id="org-1",
            booking_type="instant",
            working_days=["mon"],
            working_hours=[("09:00", "17:00")],
        )
        repo.save(settings)

        use_case = GetBookingSettings(repo)
        result = use_case.execute("org-1")

        self.assertEqual(result, settings)

    def test_get_settings_with_empty_org_id_fails(self) -> None:
        repo = FakeSettingsRepository()
        use_case = GetBookingSettings(repo)

        with self.assertRaises(ValueError):
            use_case.execute("")
