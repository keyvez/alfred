#!/Users/gaurav/.pyenv/shims/python

import requests
import json

# API endpoint URL
API_URL = "http://localhost:11434/api/tags"

try:
    # Send a GET request to the API endpoint
    response = requests.get(API_URL)
    response.raise_for_status()  # Raise an exception for non-2xx status codes
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
    exit(1)

try:
    # Parse the response JSON
    json_obj = json.loads(response.content)
    print()
except ValueError:
    print("Error: Invalid response from server")
    exit(1)

# Print the names of the available models
print("{\"items\": [")
for model in json_obj["models"]:
    print(' {"title": "' + model['name'] + '", "arg": "' + model['name'] + '"},')
print("]}")