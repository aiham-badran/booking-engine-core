from datetime import timedelta, datetime

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
        existing_bookings,
        policy=None
    ) -> bool:
        # 1. Policy 
        if policy:
            if not self._validate_duration(start_time, end_time, policy):
                return False

            if not self._validate_same_day(start_time, policy):
                return False
        
        # 2. Booking must be inside availability
        if not self._is_inside_availability(
            context_id,
            service_id,
            start_time,
            end_time,
            availabilities
        ):
            return False

        # 3. Booking must not conflict with existing bookings
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
    
    def _validate_duration(self, start_time, end_time, policy) -> bool:
        duration_minutes = int((end_time - start_time).total_seconds() / 60)

        if duration_minutes < policy.min_duration_minutes:
            return False

        if duration_minutes > policy.max_duration_minutes:
            return False

        return True

    def _validate_same_day(self, start_time, policy) -> bool:
        if policy.allow_same_day_booking:
            return True

        today = datetime.now().date()
        return start_time.date() != today
