"""
The API Root endpoint
Documentation: https://sendfox.helpscoutdocs.com/category/156-api
"""

from sendfox.api import BaseApi


class Root(BaseApi):
    """
    The API root resource returns the html page now.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize the endpoint
        """
        super(Root, self).__init__(*args, **kwargs)
        self.endpoint = ''

    def get(self, **queryparams):
        """
        Actually it is useless
        :param queryparams: The query string parameters
        """
        return self._client._get(url=self._build_path(), **queryparams)
