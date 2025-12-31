def cancel_booking(
    booking_id: str,
    user,
    booking_repository,
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
        raise ValueError("User not allowed to cancel booking")

    booking.cancel()

    if hook_manager:
        hook_manager.run_after(
            "cancel_booking",
            booking.context_id,
            booking
        )

    return booking
