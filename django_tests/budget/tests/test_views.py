import requests


# endpoint = 'http://127.0.0.1:8000/random/'
endpoint = 'http://127.0.0.1:8000/create/'

get_response = requests.post(endpoint, json={'name':'arm bush', 'slug':'ab','budget':1000})
print(get_response.json())