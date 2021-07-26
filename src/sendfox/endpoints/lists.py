"""
The API lists endpoint
Documentation: https://sendfox.helpscoutdocs.com/article/135-endpoints
"""

from sendfox.api import BaseApi


class Lists(BaseApi):
    """
    Provide paginated lists.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize the endpoint
        """
        super().__init__(*args, **kwargs)
        self.endpoint = 'lists'
        self.list_id = None

    def get_all(self, get_all=False, **queryparams):
        """
        Get information about all lists in the account.
        :param get_all: Should the query get all results
        :type get_all: :py:class:`bool`
        :param queryparams: The query string parameters
        """
        self.list_id = None
        _func = self._iterate if get_all else self._client._get
        return _func(url=self._build_path(), **queryparams)

    def create(self, data):
        """
        Create a new list in your SendFox account.
        Required params: name
        :param data: The request body parameters
        :type data: :py:class:`dict`
        data = {
            "name": string*
        }
        """
        if "name" not in data:
            raise KeyError("The list must have a name")

        response = self._client._post(url=self._build_path(), data=data)

        self.list_id = response['id'] if response is not None else None
        return response

    def get(self, list_id, **queryparams):
        """
        Get information about a specific list in your SendFox account.
        :param list_id: The unique id for the list.
        :type list_id: :py:class:`str`
        :param queryparams: The query string parameters
        """
        self.list_id = list_id
        return self._client._get(url=self._build_path(list_id), **queryparams)

    def delete_contact(self, list_id, contact_id):
        """
        Removes contact from list.
        Required params: list_id, contact_id
        :param list_id: The unique id for the list.
        :type list_id: :py:class:`str`
        :param contact_id: The unique contact id for the list.
        :type contact_id: :py:class:`str`
        """
        self.list_id = list_id
        return self._mc_client._delete(url=self._build_path(
            list_id, 'contacts', contact_id))
