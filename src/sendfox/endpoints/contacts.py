"""
The API contacts endpoint
Documentation: https://sendfox.helpscoutdocs.com/article/135-endpoints
"""

from sendfox.api import BaseApi


class Contacts(BaseApi):
    """
    Provide paginated contacts.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize the endpoint
        """
        super().__init__(*args, **kwargs)
        self.endpoint = 'contacts'
        self.contact_id = None

    def get_all(self, get_all=False, **queryparams):
        """
        Get information about all contacts in the account.
        :param get_all: Should the query get all results
        :type get_all: :py:class:`bool`
        :param queryparams: The query string parameters
        queryparams['email'] = email
        """
        self.contact_id = None
        _func = self._iterate if get_all else self._client._get
        return _func(url=self._build_path(), **queryparams)

    def create(self, data):
        """
        Create a new contact in your SendFox account.
        Required params: email
        Optional params:
            first_name
            last_name
            lists (array of list ids)
        :param data: The request body parameters
        :type data: :py:class:`dict`
        data = {
            "email": string*,
            "first_name": string*,
            "last_name": string*,
            "lists": string*,
        }
        """
        if "email" not in data:
            raise KeyError("The contact must have a email")

        response = self._client._post(url=self._build_path(), data=data)

        self.contact_id = response['id'] if response is not None else None
        return response

    def get(self, contact_id, **queryparams):
        """
        Get information about a specific contact in your SendFox account.
        :param contact_id: The unique id for the list.
        :type contact_id: :py:class:`str`
        :param queryparams: The query string parameters
        """
        self.contact_id = contact_id
        return self._client._get(
            url=self._build_path(contact_id), **queryparams)
