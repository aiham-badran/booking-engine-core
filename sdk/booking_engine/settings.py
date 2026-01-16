class SettingsSDK:
  def __init__(self, update_uc, get_uc):
    self._update_uc = update_uc
    self._get_uc = get_uc


  def update(self, organization_id: str, booking_type: str, working_days: list,  working_hours: list[tuple[str, str]],):
    return self._update_uc.execute(
    organization_id=organization_id,
    booking_type=booking_type,
    working_days=working_days,
    working_hours=working_hours
    )


  def get(self, organization_id: str):
    return self._get_uc.execute(organization_id=organization_id)