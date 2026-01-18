from core.sdk.dto import CreateBookingDTO
from core.sdk.exceptions import BookingConflictError as SDKBookingConflictError
from core.domain.policies.booking_policy import BookingConflictError as DomainConflictError
from core.application.use_cases.create_booking import CreateBookingUseCase
from core.application.use_cases.cancel_booking import CancelBookingUseCase
from core.sdk.events import BookingCreatedEvent, BookingCancelledEvent
from core.sdk.plugin import PluginManager


class BookingEngine:
    """
    Public SDK Facade for the booking engine core.
    """

    def __init__(
        self,
        create_booking_uc: CreateBookingUseCase,
        cancel_booking_uc: CancelBookingUseCase,
        plugin_manager: PluginManager | None = None,
    ):
        self._create_booking_uc = create_booking_uc
        self._cancel_booking_uc = cancel_booking_uc
        self._plugin_manager = plugin_manager

    def create_booking(self, dto: CreateBookingDTO):
        try:
            booking = self._create_booking_uc.execute(
                organization_id=dto.organization_id,
                user_id=dto.user_id,
                time_slot=dto.time_slot,
            )

            if self._plugin_manager:
                self._plugin_manager.dispatch(
                    BookingCreatedEvent(booking)
                )

            return booking

        except DomainConflictError as e:
            raise SDKBookingConflictError(str(e))

    def cancel_booking(self, booking):
        self._cancel_booking_uc.execute(booking)

        if self._plugin_manager:
            self._plugin_manager.dispatch(
                BookingCancelledEvent(booking)
            )
