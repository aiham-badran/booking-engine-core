import unittest
from datetime import datetime, timedelta

from core.sdk.engine import BookingEngine
from core.sdk.dto import CreateBookingDTO
from core.sdk.events import BookingCreatedEvent

from core.application.use_cases.create_booking import CreateBookingUseCase
from core.application.use_cases.cancel_booking import CancelBookingUseCase
from core.domain.value_objects.time_slot import TimeSlot

from tests.fakes.fake_booking_repository import FakeBookingRepository
from tests.fakes.fake_plugin_manager import FakePluginManager


class TestBookingEngine(unittest.TestCase):

    def test_plugin_event_dispatched(self):
        # Arrange
        booking_repo = FakeBookingRepository()
        plugin_manager = FakePluginManager()

        create_booking_uc = CreateBookingUseCase(booking_repo)
        cancel_booking_uc = CancelBookingUseCase()

        engine = BookingEngine(
            create_booking_uc=create_booking_uc,
            cancel_booking_uc=cancel_booking_uc,
            plugin_manager=plugin_manager,
        )

        slot = TimeSlot(
            start=datetime.now(),
            end=datetime.now() + timedelta(hours=1),
        )

        dto = CreateBookingDTO(
            organization_id="org-1",
            user_id="user-1",
            time_slot=slot,
        )

        # Act
        booking = engine.create_booking(dto)

        # Assert
        self.assertEqual(len(plugin_manager.events), 1)
        self.assertIsInstance(
            plugin_manager.events[0],
            BookingCreatedEvent,
        )
        self.assertEqual(
            plugin_manager.events[0].booking,
            booking,
        )
