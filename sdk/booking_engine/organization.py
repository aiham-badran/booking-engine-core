class OrganizationSDK:
  def __init__(self, create_uc, get_uc):
    self._create_uc = create_uc
    self._get_uc = get_uc


  def create(self, organization_id: str, name: str):
    return self._create_uc.execute(
      organization_id=organization_id,
      name=name
    )


  def get(self, organization_id: str):
    return self._get_uc.execute(organization_id=organization_id)