"""
The base API object that allows constructions of various endpoint paths
"""
from itertools import chain


class BaseApi:
    """
    Simple class to buid path for entities
    """

    def __init__(self, client):
        """
        Initialize the class with you user_id and secret_key

        :param client: The sendfox client connection
        :type client: :mod:`sendfox.client.Client`
        """
        super().__init__()
        self._client = client
        self.endpoint = ''

    def _build_path(self, *args):
        """
        Build path with endpoint and args

        :param args: Tokens in the endpoint URL
        :type args: :py:class:`str`
        """
        return '/'.join(chain((self.endpoint,), map(str, args)))

    def _iterate(self, url, **queryparams):
        """
        Iterate over all pages for the given url.
        Feed in the result of self._build_path as the url.

        :param url: The url of the endpoint
        :type url: :py:class:`str`
        :param queryparams: The query string parameters
        :type queryparams: :py:class:`dict`
        """
        # fields as a query string parameter should be a string with
        # comma-separated substring values to pass along to
        # self._client._get(). It should also contain total_items whenever
        # the parameter is employed, which is forced here.
        if not self._client.enabled:
            return

        # Fetch results from sendfox
        result = self._client._get(url=url, **queryparams)
        return result
