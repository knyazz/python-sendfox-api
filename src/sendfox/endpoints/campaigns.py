"""
The API campaigns endpoint
Documentation: https://sendfox.helpscoutdocs.com/article/135-endpoints
"""

from sendfox.api import BaseApi


class Campaigns(BaseApi):
    """
    Provide paginated campaigns.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize the endpoint
        """
        super().__init__(*args, **kwargs)
        self.endpoint = 'campaigns'
        self.campaign_id = None

    def get_all(self, get_all=False, **queryparams):
        """
        Get information about all Campaigns in the account.
        :param get_all: Should the query get all results
        :type get_all: :py:class:`bool`
        :param queryparams: The query string parameters
        queryparams['emails'] = email
        """
        self.campaign_id = None
        _func = self._iterate if get_all else self._client._get
        return _func(url=self._build_path(), **queryparams)

    def get(self, campaign_id, **queryparams):
        """
        Get information about a specific campaign in your SendFox account.
        :param campaign_id: The unique id for the list.
        :type campaign_id: :py:class:`str`
        :param queryparams: The query string parameters
        """
        self.campaign_id = campaign_id
        return self._client._get(
            url=self._build_path(campaign_id), **queryparams)
