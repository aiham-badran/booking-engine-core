def test_service_repository_isolates_services_by_context():
    """
    GIVEN services from different contexts
    WHEN stored in repository
    THEN they must be isolated per context
    """
    from src.services.service import Service
    from src.services.service_repository import ServiceRepository

    repo = ServiceRepository()

    service_1 = Service("s1", "company_1")
    service_2 = Service("s2", "company_2")

    repo.add(service_1)
    repo.add(service_2)

    company_1_services = repo.list_by_context("company_1")
    company_2_services = repo.list_by_context("company_2")

    assert len(company_1_services) == 1
    assert company_1_services[0].service_id == "s1"

    assert len(company_2_services) == 1
    assert company_2_services[0].service_id == "s2"
