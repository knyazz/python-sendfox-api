"""
SendFox Api SDK
Documentation at https://sendfox.helpscoutdocs.com/category/156-api
"""

# API Client
from sendfox.client import Client

from sendfox.endpoints.root import Root
from sendfox.endpoints.campaigns import Campaigns
from sendfox.endpoints.contacts import Contacts
from sendfox.endpoints.lists import Lists
from sendfox.endpoints.me import Me
from sendfox.endpoints.unsubscribe import Unsubscribe


class SendFox(Client):
    """
    SendFox class to communicate with API
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize the class expecting your api_key and user_id,
        attach the all endpoints
        """
        super().__init__(*args, **kwargs)
        # API Root
        self.root = self.api_root = Root(self)
        # Campaigns
        self.campaigns = Campaigns(self)
        # Contacts
        self.contacts = Contacts(self)
        # Lists
        self.lists = Lists(self)
        # Me
        self.me = Me(self)
        # Unsubscribe
        self.unsubscribe = Unsubscribe(self)
