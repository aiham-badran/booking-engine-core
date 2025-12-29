from datetime import datetime

def test_availability_repository_isolated_by_context_and_service():
    """
    GIVEN availability slots for different services and contexts
    WHEN stored in repository
    THEN they must be isolated correctly
    """
    from src.availability.availability import Availability
    from src.availability.availability_repository import AvailabilityRepository

    repo = AvailabilityRepository()

    a1 = Availability(
        "a1", "service_1", "company_1",
        datetime(2025, 1, 1, 10), datetime(2025, 1, 1, 11)
    )

    a2 = Availability(
        "a2", "service_2", "company_1",
        datetime(2025, 1, 1, 12), datetime(2025, 1, 1, 13)
    )

    a3 = Availability(
        "a3", "service_1", "company_2",
        datetime(2025, 1, 1, 10), datetime(2025, 1, 1, 11)
    )

    repo.add(a1)
    repo.add(a2)
    repo.add(a3)

    service_1_company_1 = repo.list(
        context_id="company_1",
        service_id="service_1"
    )

    assert len(service_1_company_1) == 1
    assert service_1_company_1[0].availability_id == "a1"
