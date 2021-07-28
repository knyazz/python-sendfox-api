[![python-sendfox-api on PyPi](https://img.shields.io/pypi/v/python-sendfox-api)](https://pypi.org/project/python-sendfox-api/)
![MIT license](https://img.shields.io/pypi/l/python-sendfox-api)
![Beta](https://img.shields.io/pypi/status/python-sendfox-api)


# python-sendfox-api
A straighforward python client for Sendfox API

### Installation

This client is hosted at PyPi under the name `python-sendfox-api`, to install
it, simply run

`pip install python-sendfox-api`

### Initialization

Grab `ACCESS_TOKEN` from your SendFox account.

    from sendfox import SendFox

    client = SendFox('token')


### Examples

    # returns the paginated lists
    client.lists.get_all()

    # returns the list matching id '123456'
    client.lists.get('123456')

    # returns all the campaigns
    client.campaigns.get_all()

    # You can also disable at runtime with the optional ``enabled`` parameter.
    # Every API call will return None
    client = SendFox('token', enabled=False)

    # You are encouraged to specify a value in seconds for the ``timeout``
    # parameter to avoid hanging requests.
    client = SendFox('token', timeout=10.0)

    # You are encouraged to specify a User-Agent for requests to the SendFox
    # API. Headers can be specified using the ``request_headers`` parameter.
    headers = requests.utils.default_headers()
    headers['User-Agent'] = 'Example (example@example.com)'
    client = SendFox('token', request_headers=headers)
