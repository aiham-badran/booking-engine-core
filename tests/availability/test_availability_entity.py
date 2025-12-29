from datetime import datetime

def test_availability_belongs_to_service_and_context():
    """
    GIVEN an availability slot
    THEN it must belong to a service and a context
    """
    from src.availability.availability import Availability

    start = datetime(2025, 1, 1, 10, 0)
    end = datetime(2025, 1, 1, 11, 0)

    availability = Availability(
        availability_id="a1",
        service_id="service_1",
        context_id="company_1",
        start_time=start,
        end_time=end
    )

    assert availability.service_id == "service_1"
    assert availability.context_id == "company_1"
    assert availability.start_time == start
    assert availability.end_time == end
