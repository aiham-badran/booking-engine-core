from datetime import datetime
from src.rules.booking_rules import BookingRulesService
from src.policies.booking_policy import BookingPolicy


def test_booking_rejected_if_duration_less_than_minimum():
    rules = BookingRulesService()

    policy = BookingPolicy(
        min_duration_minutes=60,
        max_duration_minutes=180,
        buffer_minutes=0,
        allow_same_day_booking=True,
        cancel_before_minutes=0
    )

    allowed = rules._validate_duration(
        start_time=datetime(2025, 1, 1, 10),
        end_time=datetime(2025, 1, 1, 10, 30),
        policy=policy
    )

    assert allowed is False

def test_booking_rejected_if_duration_exceeds_maximum():
    rules = BookingRulesService()

    policy = BookingPolicy(
        min_duration_minutes=30,
        max_duration_minutes=60,
        buffer_minutes=0,
        allow_same_day_booking=True,
        cancel_before_minutes=0
    )

    allowed = rules._validate_duration(
        start_time=datetime(2025, 1, 1, 9),
        end_time=datetime(2025, 1, 1, 11),
        policy=policy
    )

    assert allowed is False

def test_booking_allowed_within_policy_limits():
    rules = BookingRulesService()

    policy = BookingPolicy(
        min_duration_minutes=30,
        max_duration_minutes=120,
        buffer_minutes=0,
        allow_same_day_booking=True,
        cancel_before_minutes=0
    )

    allowed = rules._validate_duration(
        start_time=datetime(2025, 1, 1, 10),
        end_time=datetime(2025, 1, 1, 11),
        policy=policy
    )

    assert allowed is True

from datetime import datetime, timedelta


def test_same_day_booking_not_allowed():
    rules = BookingRulesService()

    policy = BookingPolicy(
        min_duration_minutes=30,
        max_duration_minutes=120,
        buffer_minutes=0,
        allow_same_day_booking=False,
        cancel_before_minutes=0
    )

    start = datetime.now() + timedelta(hours=1)
    end = start + timedelta(minutes=60)

    allowed = rules._validate_same_day(start, policy)

    assert allowed is False
