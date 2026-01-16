from sdk.booking_engine.organization import OrganizationSDK
from sdk.booking_engine.user import UserSDK
from sdk.booking_engine.settings import SettingsSDK
from sdk.booking_engine.availability import AvailabilitySDK
from sdk.booking_engine.booking import BookingSDK
from core.application.use_cases.check_availability import CheckAvailability


class BookingEngineClient:
    def __init__(
        self,
        create_org_uc,
        get_org_uc,
        create_user_uc,
        get_user_uc,
        update_settings_uc,
        get_settings_uc,
        create_booking_uc,
        get_booking_uc,
    ):
        self.organizations = OrganizationSDK(create_org_uc, get_org_uc)
        self.users = UserSDK(create_user_uc, get_user_uc)
        self.settings = SettingsSDK(update_settings_uc, get_settings_uc)

        self._get_settings_uc = get_settings_uc

        self.bookings = BookingSDK(create_booking_uc, get_booking_uc)

    def availability(self, organization_id):
        settings = self._get_settings_uc.execute(organization_id)
        availability_uc = CheckAvailability(settings)
        return AvailabilitySDK(availability_uc)
