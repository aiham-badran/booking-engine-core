class UserSDK:
  def __init__(self, create_uc, get_uc):
    self._create_uc = create_uc
    self._get_uc = get_uc


  def create(self, user_id: str, organization_id: str, name: str):
    return self._create_uc.execute(
    user_id=user_id,
    organization_id=organization_id,
    name=name
    )


  def get(self, user_id: str):
    return self._get_uc.execute(user_id=user_id)