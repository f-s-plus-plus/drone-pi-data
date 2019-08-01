import requests
import json

""" 
This class is responsible for making requests to the backend api server
"""


class Request:
    # Request constructor that loads data from credentials.json and gets JWT token from drone pi
    def __init__(self):
        credentials = json.load(open('credentials.json'))
        self.host = credentials['host']
        # logs in via post request
        req = requests.post(
            url='http://{}:3000/login'.format(self.host),
            params={
                'email': credentials['email'],
                'password': credentials['password']
            }
        )
        # saves jwt token
        self.token = req.json()['token']

    # used for saving flights
    def save_flight(self, **kwargs):
        # makes post request to save flight
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
        # prints out the json that is returned
        return req.json()



