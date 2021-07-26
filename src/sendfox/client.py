"""
SendFox Api SDK
Documentation at https://sendfox.helpscoutdocs.com/category/156-api
"""
import functools


import requests
from requests.status_codes import codes

from urllib.parse import urljoin
from urllib.parse import urlencode

import logging

_logger = logging.getLogger('sendfox.client')


def _enabled_or_noop(fn):
    @functools.wraps(fn)
    def wrapper(self, *args, **kwargs):
        if self.enabled:
            return fn(self, *args, **kwargs)
    return wrapper


class SendfoxAPIError(Exception):
    pass


def _raise_response_error(r):
    # in case of a 500 error, the response might not be a JSON
    try:
        error_data = r.json()
    except ValueError:
        error_data = {"response": r}
    raise SendfoxAPIError(error_data)


BASE_URL = "https://api.sendfox.com/"


class Client:
    """
    class to communicate with API
    """

    def __init__(
        self,
        access_token=None,
        enabled=True,
        timeout=None,
        request_hooks=None,
        request_headers=None
    ):
        """
        Initialize the class with your optional user_id and required api_key.

        If `enabled` is not True, these methods become no-ops. This is
        particularly useful for testing or disabling with configuration.

        :param access_token: The OAuth2.0 access token
        :type access_token: :py:class:`str`
        :param enabled: Whether the API should execute any requests
        :type enabled: :py:class:`bool`
        :param timeout: (optional) How long to wait for the server to send
            data before giving up, as a float, or a :ref:`(connect timeout,
            read timeout) <timeouts>` tuple.
        :type timeout: float or tuple
        :param request_hooks: (optional) Hooks for :py:func:`requests.requests`.
        :type request_hooks: :py:class:`dict`
        :param request_headers: (optional) Headers for
            :py:func:`requests.requests`.
        :type request_headers: :py:class:`dict`
        """
        super().__init__()
        if not access_token:
            raise Exception("You must provide an OAuth access token or API key")

        self.enabled = enabled
        self.timeout = timeout
        self.base_url = BASE_URL
        self.request_headers = request_headers or requests.utils.default_headers()
        self.request_hooks = request_hooks or requests.hooks.default_hooks()

        self.request_headers['Authorization'] = 'Bearer ' + access_token

    def _make_request(self, **kwargs):
        json = kwargs.get('json')
        method = kwargs['method']
        url = kwargs['url']
        _logger.info(f"{method} Request: {url}")
        if json:
            _logger.info(f"PAYLOAD: {json}")

        try:
            response = requests.request(**kwargs)
        except requests.exceptions.RequestException as e:
            raise e
        else:
            status_code = response.status_code
            _logger.info(f"{method} Response: {status_code}")
            if status_code >= codes.BAD_REQUEST:
                _raise_response_error(response)

            if status_code == codes.NO_CONTENT:
                return None
            return response.json()

    @_enabled_or_noop
    def _post(self, url, data=None):
        """
        Handle authenticated POST requests

        :param url: The url for the endpoint including path parameters
        :type url: :py:class:`str`
        :param data: The request body parameters
        :type data: :py:data:`none` or :py:class:`dict`
        :returns: The JSON output from the API or an error message
        """
        url = urljoin(self.base_url, url)
        return self._make_request(**dict(
            method='POST',
            url=url,
            json=data,
            timeout=self.timeout,
            hooks=self.request_hooks,
            headers=self.request_headers
        ))

    @_enabled_or_noop
    def _get(self, url, **queryparams):
        """
        Handle authenticated GET requests

        :param url: The url for the endpoint including path parameters
        :type url: :py:class:`str`
        :param queryparams: The query string parameters
        :returns: The JSON output from the API
        """
        url = urljoin(self.base_url, url)
        if len(queryparams):
            url += '?' + urlencode(queryparams)
        return self._make_request(**dict(
            method='GET',
            url=url,
            timeout=self.timeout,
            hooks=self.request_hooks,
            headers=self.request_headers
        ))

    @_enabled_or_noop
    def _delete(self, url):
        """
        Handle authenticated DELETE requests

        :param url: The url for the endpoint including path parameters
        :type url: :py:class:`str`
        :returns: The JSON output from the API
        """
        url = urljoin(self.base_url, url)
        return self._make_request(**dict(
            method='DELETE',
            url=url,
            timeout=self.timeout,
            hooks=self.request_hooks,
            headers=self.request_headers
        ))

    @_enabled_or_noop
    def _patch(self, url, data=None):
        """
        Handle authenticated PATCH requests

        :param url: The url for the endpoint including path parameters
        :type url: :py:class:`str`
        :param data: The request body parameters
        :type data: :py:data:`none` or :py:class:`dict`
        :returns: The JSON output from the API
        """
        url = urljoin(self.base_url, url)
        return self._make_request(**dict(
            method='PATCH',
            url=url,
            json=data,
            timeout=self.timeout,
            hooks=self.request_hooks,
            headers=self.request_headers
        ))

    @_enabled_or_noop
    def _put(self, url, data=None):
        """
        Handle authenticated PUT requests

        :param url: The url for the endpoint including path parameters
        :type url: :py:class:`str`
        :param data: The request body parameters
        :type data: :py:data:`none` or :py:class:`dict`
        :returns: The JSON output from the API
        """
        url = urljoin(self.base_url, url)
        return self._make_request(**dict(
            method='PUT',
            url=url,
            json=data,
            timeout=self.timeout,
            hooks=self.request_hooks,
            headers=self.request_headers
        ))
