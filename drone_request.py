#!/usr/bin/python

import requests


class Request:
    def __init__(self, host, **kwargs):
        self.host = host
        req = requests.post(
            url='http://{}:3000/login'.format(self.host),
            params={
                'email': kwargs['email'],
                'password': kwargs['password']
            }
        )
        self.token = req.json()['token']

    def save_flight(self, **kwargs):
        req = requests.post(
            url='http://{}:3000/flights'.format(self.host),
            json={
                'flight': {
                    'distance': kwargs['distance'],
                    'rating': kwargs['rating'],
                    'name': kwargs['name'],
                    'longitude': kwargs['longitude'],
                    'latitude': kwargs['latitude']
                }
            },
            headers={
                'Authorization': 'Bearer {}'.format(self.token)
            }
        )
        return req.json()



