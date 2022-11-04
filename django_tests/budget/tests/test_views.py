import requests


# endpoint = 'http://127.0.0.1:8000/random/'
endpoint = 'http://127.0.0.1:8000/create/'

get_response = requests.post(endpoint, json={'name':'shock rear','slug':'shock-rear','budget':1500})
# get_response = requests.get(endpoint)

print(get_response.json())
