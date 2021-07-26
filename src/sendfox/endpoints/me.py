"""
The API Me endpoint
Documentation: https://sendfox.helpscoutdocs.com/article/135-endpoints
"""

from sendfox.api import BaseApi


class Me(BaseApi):
    """
    Gets information for authenticated user.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize the endpoint
        """
        super().__init__(*args, **kwargs)
        self.endpoint = 'me'

    def get(self, **queryparams):
        """
        Gets information for authenticated user.
        :param queryparams: The query string parameters
        """
        return self._client._get(url=self._build_path(), **queryparams)
