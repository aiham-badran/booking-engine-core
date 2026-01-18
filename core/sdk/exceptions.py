# core/sdk/exceptions.py

class BookingEngineError(Exception):
    """Base exception for Booking Engine SDK"""
    pass


class BookingConflictError(BookingEngineError):
    pass


class BookingNotFoundError(BookingEngineError):
    pass
