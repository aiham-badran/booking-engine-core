from core.domain.value_objects.time_slot import TimeSlot

class BookingSDK:
  def __init__(self, create_uc, get_uc):
    self._create_uc = create_uc
    self._get_uc = get_uc


  def create(self, booking_id: str, organization_id: str, user_id: str, booking_date, start: str, end: str):
    return self._create_uc.execute(
    booking_id=booking_id,
    organization_id=organization_id,
    user_id=user_id,
    booking_date=booking_date,
    slot=TimeSlot(start,end)
    )


  def get(self, booking_id: str):
    return self._get_uc.execute(booking_id=booking_id) 