class BookingRulesService:
    """
    Domain service responsible for validating booking rules.
    Stateless and context-aware.
    """

    def can_book(
        self,
        context_id: str,
        service_id: str,
        start_time,
        end_time,
        availabilities,
        existing_bookings
    ) -> bool:
        # 1. Booking must be inside availability
        if not self._is_inside_availability(
            context_id,
            service_id,
            start_time,
            end_time,
            availabilities
        ):
            return False

        # 2. Booking must not conflict with existing bookings
        if self._has_conflict(start_time, end_time, existing_bookings):
            return False

        return True

    def _is_inside_availability(
        self,
        context_id,
        service_id,
        start_time,
        end_time,
        availabilities
    ) -> bool:
        for availability in availabilities:
            if (
                availability.context_id == context_id
                and availability.service_id == service_id
                and start_time >= availability.start_time
                and end_time <= availability.end_time
            ):
                return True
        return False

    def _has_conflict(self, start_time, end_time, existing_bookings) -> bool:
        for booking in existing_bookings:
            if (
                start_time < booking["end_time"]
                and end_time > booking["start_time"]
            ):
                return True
        return False
