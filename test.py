"""
Some basic tests to verify that the wrapper is working
"""
from sendfox import SendFox


client = SendFox('token')

print(client.me.get())

print(client.lists.get_all())

print(client.lists.get('222222'))

print(client.contacts.get_all())

print(client.campaigns.get_all())
