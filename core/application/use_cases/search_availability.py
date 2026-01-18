# core/application/use_cases/search_availability.py

class SearchAvailabilityUseCase:
    """
    Returns available time slots for a given day.
    """

    def __init__(self, availability_repository, booking_repository):
        self.availability_repository = availability_repository
        self.booking_repository = booking_repository

    def execute(self, organization_id, target_date):
        base_slots = self.availability_repository.get_daily_slots(
            organization_id=organization_id,
            target_date=target_date,
        )

        bookings = self.booking_repository.get_for_day(
            organization_id=organization_id,
            target_date=target_date,
        )

        available_slots = []

        for slot in base_slots:
            conflict = False
            for booking in bookings:
                if booking.is_active() and booking.time_slot.overlaps(slot):
                    conflict = True
                    break

            if not conflict:
                available_slots.append(slot)

        return available_slots
