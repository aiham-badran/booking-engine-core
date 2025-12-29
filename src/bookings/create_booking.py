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
    authorization_service
):
    # 1️⃣ Authorization (optional)
    if hasattr(user, "role") and user.role is not None:
        if not authorization_service.is_allowed(
            user, "book_service"
        ):
            raise ValueError("User not allowed to book")

    # 2️⃣ Load existing bookings (same context)
    existing_bookings = booking_repository.list_by_context(context_id)

    # 3️⃣ Apply booking rules
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

    # 4️⃣ Create booking
    booking = Booking(
        booking_id=booking_id,
        context_id=context_id,
        service_id=service_id,
        user_id=user.user_id,
        start_time=start_time,
        end_time=end_time,
        status="CONFIRMED"
    )

    # 5️⃣ Save booking
    booking_repository.add(booking)

    return booking
