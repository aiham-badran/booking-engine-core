from src.bookings.booking import Booking


def create_booking(
    booking_id: str,
    context_id: str,
    service_id: str,
    user,
    start_time,
    end_time,
    availabilities,
    booking_repository,
    rules_service,
    authorization_service,
    hook_manager=None
):
    # 0️⃣ Before Hook
    if hook_manager:
        hook_manager.run_before(
            "create_booking",
            context_id,
            {
                "booking_id": booking_id,
                "service_id": service_id,
                "user": user,
                "start_time": start_time,
                "end_time": end_time
            }
        )

    # 1️⃣ Authorization (optional)
    if hasattr(user, "role") and user.role is not None:
        if not authorization_service.is_allowed(user, "book_service"):
            raise ValueError("User not allowed to book")

    existing_bookings = booking_repository.list_by_context(context_id)

    allowed = rules_service.can_book(
        context_id=context_id,
        service_id=service_id,
        start_time=start_time,
        end_time=end_time,
        availabilities=availabilities,
        existing_bookings=existing_bookings
    )

    if not allowed:
        raise ValueError("Booking rules rejected")

    booking = Booking(
        booking_id=booking_id,
        context_id=context_id,
        service_id=service_id,
        user_id=user.user_id,
        start_time=start_time,
        end_time=end_time,
        status="CONFIRMED"
    )

    booking_repository.add(booking)

    # 2️⃣ After Hook
    if hook_manager:
        hook_manager.run_after(
            "create_booking",
            context_id,
            booking
        )

    return booking
