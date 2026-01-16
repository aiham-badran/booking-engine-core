# tests/sdk/test_composition.py

from core.application.use_cases.create_organization import CreateOrganization
from core.application.use_cases.get_organization import GetOrganization
from core.application.use_cases.create_user import CreateUser
from core.application.use_cases.get_user import GetUser
from core.application.use_cases.update_booking_settings import UpdateBookingSettings
from core.application.use_cases.get_booking_settings import GetBookingSettings
from core.application.use_cases.check_availability import CheckAvailability
from core.application.use_cases.create_booking import CreateBooking
from core.application.use_cases.get_booking import GetBooking
from core.domain.entities.booking_settings import BookingSettings

from sdk.booking_engine.client import BookingEngineClient

from tests.core.test_organization_module import FakeOrganizationRepository
from tests.core.test_user_module import FakeUserRepository
from tests.core.test_settings_module import FakeSettingsRepository
from tests.core.test_booking_module import FakeBookingRepository


def build_test_sdk() -> BookingEngineClient:
    # Repositories
    org_repo = FakeOrganizationRepository()
    user_repo = FakeUserRepository()
    settings_repo = FakeSettingsRepository()
    booking_repo = FakeBookingRepository()


    fake_settings = BookingSettings(
        organization_id="org-1",
        booking_type="instant",
        working_days=["mon"],
        working_hours=[("09:00", "17:00")],
    )

    # Use Cases
    create_org = CreateOrganization(org_repo)
    get_org = GetOrganization(org_repo)

    create_user = CreateUser(user_repo)
    get_user = GetUser(user_repo)

    update_settings = UpdateBookingSettings(settings_repo)
    get_settings = GetBookingSettings(settings_repo)

    create_booking = CreateBooking(
        repository=booking_repo,
        availability_checker=CheckAvailability(fake_settings)  
    )
    get_booking = GetBooking(booking_repo)

    return BookingEngineClient(
        create_org_uc=create_org,
        get_org_uc=get_org,
        create_user_uc=create_user,
        get_user_uc=get_user,
        update_settings_uc=update_settings,
        get_settings_uc=get_settings,
        create_booking_uc=create_booking,
        get_booking_uc=get_booking,
    )
