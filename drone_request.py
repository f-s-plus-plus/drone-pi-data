import requests
import json


class Request:
    def __init__(self, host):
        self.host = host
        credentials = json.load(open('credentials.json'))
        req = requests.post(
            url='http://{}:3000/login'.format(self.host),
            params={
                'email': credentials['email'],
                'password': credentials['password']
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



