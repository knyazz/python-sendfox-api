"""
The API unsubscribe endpoint
Documentation: https://sendfox.helpscoutdocs.com/article/135-endpoints
"""

from sendfox.api import BaseApi


class Unsubscribe(BaseApi):
    """
    Provide unsubscribe functionality.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize the endpoint
        """
        super().__init__(*args, **kwargs)
        self.endpoint = 'unsubscribe'

    def unsubscribe(self, email, **queryparams):
        """
        Unsubscribe email in your SendFox account.
        Required params: email
        :param email: The unique id for the list.
        :type email: :py:class:`str`
        :param queryparams: The query string parameters
        """
        queryparams['email'] = email
        return self._client._patch(url=self._build_path(), **queryparams)
