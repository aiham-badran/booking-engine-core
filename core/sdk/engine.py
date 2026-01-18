# core/sdk/engine.py
"""
BookingEngine Facade / Gatekeeper

Purpose:
- Central entry point for all external interactions
- Enforce access to Core modules through this SDK only
- Provide clear public API for bookings and availability
"""

from core.application.use_cases import create_booking, cancel_booking, update_booking, search_availability
from core.domain.entities import Booking, Availability

class BookingEngine:
    """
    Facade for interacting with Booking Core

    All operations must go through this class.
    Direct use of Core modules is prohibited.
    """

    def __init__(self, organization_id: str):
        self.organization_id = organization_id

    def create_booking(self, booking_data):
        # Delegate to internal Use Case
        return create_booking(self.organization_id, booking_data)

    def cancel_booking(self, booking_id):
        return cancel_booking(self.organization_id, booking_id)

    def update_booking(self, booking_id, updated_data):
        return update_booking(self.organization_id, booking_id, updated_data)

    def search_availability(self, date, duration=None):
        return search_availability(self.organization_id, date, duration)


# from core.sdk.dto import CreateBookingDTO
# from core.sdk.exceptions import BookingConflictError as SDKBookingConflictError
# from core.domain.policies.booking_policy import BookingConflictError as DomainConflictError
# from core.application.use_cases.create_booking import CreateBookingUseCase
# from core.application.use_cases.cancel_booking import CancelBookingUseCase
# from core.sdk.events import BookingCreatedEvent, BookingCancelledEvent
# from core.sdk.plugin import PluginManager


# class BookingEngine:
#     """
#     Public SDK Facade for the booking engine core.
#     """

#     def __init__(
#         self,
#         create_booking_uc: CreateBookingUseCase,
#         cancel_booking_uc: CancelBookingUseCase,
#         plugin_manager: PluginManager | None = None,
#     ):
#         self._create_booking_uc = create_booking_uc
#         self._cancel_booking_uc = cancel_booking_uc
#         self._plugin_manager = plugin_manager

#     def create_booking(self, dto: CreateBookingDTO):
#         try:
#             booking = self._create_booking_uc.execute(
#                 organization_id=dto.organization_id,
#                 user_id=dto.user_id,
#                 time_slot=dto.time_slot,
#             )

#             if self._plugin_manager:
#                 self._plugin_manager.dispatch(
#                     BookingCreatedEvent(booking)
#                 )

#             return booking

#         except DomainConflictError as e:
#             raise SDKBookingConflictError(str(e))

#     def cancel_booking(self, booking):
#         self._cancel_booking_uc.execute(booking)

#         if self._plugin_manager:
#             self._plugin_manager.dispatch(
#                 BookingCancelledEvent(booking)
#             )
