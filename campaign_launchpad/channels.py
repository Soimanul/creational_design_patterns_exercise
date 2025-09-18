
from abc import ABC, abstractmethod
from uuid import uuid4
from .budget import GlobalBudget
from .campaign import Campaign


class ChannelClient(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def create_campaign(self, campaign: Campaign) -> str:
        # TODO: Create a campaign on this channel and return an external id.
        if not isinstance(campaign, Campaign):
          raise TypeError("campaign must be a Campaign instance")
        
        if campaign.daily_budget <= 0:
          raise ValueError("Campaign daily budget must be positive")
        
        GlobalBudget().allocate(campaign.daily_budget)
        prefix = self.name[0].lower() + "-"
        external_id = f"{prefix}{uuid4().hex}"
        
        return external_id

    @abstractmethod
    def pause_campaign(self, campaign_id: str) -> None:
        pass


class GoogleAdsClient(ChannelClient):
  # TODO: Implement the Google Ads specific logic here.
  def __init__(self):
    super().__init__("google")

  def create_campaign(self, campaign: Campaign) -> str:
    if not isinstance(campaign, Campaign):
      raise TypeError("campaign must be a Campaign instance")
    if campaign.daily_budget <= 0:
      raise ValueError("Campaign daily budget must be positive")
    GlobalBudget().allocate(campaign.daily_budget)
    return f"g-{uuid4().hex}"

  def pause_campaign(self, campaign_id: str) -> None:
    return None

class FacebookAdsClient(ChannelClient):
  # TODO: Implement the Facebook Ads specific logic here.
  def __init__(self):
    super().__init__("facebook")

  def create_campaign(self, campaign: Campaign) -> str:
    if not isinstance(campaign, Campaign):
      raise TypeError("campaign must be a Campaign instance")
    if campaign.daily_budget <= 0:
      raise ValueError("Campaign daily budget must be positive")
    GlobalBudget().allocate(campaign.daily_budget)
    return f"f-{uuid4().hex}"

  def pause_campaign(self, campaign_id: str) -> None:
    return None

class ChannelClientFactory:
    @staticmethod
    def create(channel: str) -> ChannelClient:
      # TODO: Return the appropriate client based on the channel.
      normalized = channel.strip().lower()
      if normalized == "google":
        return GoogleAdsClient()
      if normalized == "facebook":
        return FacebookAdsClient()
      raise ValueError("Unknown channel")
