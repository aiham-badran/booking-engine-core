def reschedule_booking(
    booking_id: str,
    user,
    new_start_time,
    new_end_time,
    booking_repository,
    rules_service,
    availabilities,
    hook_manager=None
):
    bookings = booking_repository.list_by_context(user.context_id)
    booking = next((b for b in bookings if b.booking_id == booking_id), None)

    if booking is None:
        raise ValueError("Booking not found")

    is_owner = booking.user_id == user.user_id
    is_context_admin = (
        hasattr(user, "role")
        and user.role is not None
        and user.role.has_permission("manage_bookings")
    )

    if not (is_owner or is_context_admin):
        raise ValueError("User not allowed to reschedule booking")

    existing_bookings = [b for b in bookings if b.booking_id != booking.booking_id]

    allowed = rules_service.can_book(
        context_id=booking.context_id,
        service_id=booking.service_id,
        start_time=new_start_time,
        end_time=new_end_time,
        availabilities=availabilities,
        existing_bookings=existing_bookings
    )

    if not allowed:
        raise ValueError("Booking rules rejected")

    booking.reschedule(new_start_time, new_end_time)

    if hook_manager:
        hook_manager.run_after(
            "reschedule_booking",
            booking.context_id,
            booking
        )

    return booking
