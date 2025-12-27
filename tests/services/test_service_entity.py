def test_service_belongs_to_context():
    """
    GIVEN a service
    THEN it must belong to a context
    """
    from src.services.service import Service

    service = Service(
        service_id="service_1",
        context_id="company_1"
    )

    assert service.service_id == "service_1"
    assert service.context_id == "company_1"
