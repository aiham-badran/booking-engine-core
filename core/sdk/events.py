# core/sdk/events.py

class Event:
    """Base class for all events"""
    pass


class BookingCreatedEvent(Event):
    def __init__(self, booking):
        self.booking = booking


class BookingCancelledEvent(Event):
    def __init__(self, booking):
        self.booking = booking
