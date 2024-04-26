#!/Users/gaurav/.pyenv/shims/python

import sys
import json
import requests

if len(sys.argv) != 3:
    print("Usage: ask.py <model> <freeform_text>")
    sys.exit(1)

model = sys.argv[1]
freeform_text = sys.argv[2]

# Define the query parameters
query = ''.join(sys.argv[1:])
payload = {
    "model": model,
    "stream": False,
    "prompt": freeform_text,
    "systemPrompt": "You are a helpful AI assistant."
}

# Send the request to the local Llama server
try:
    response = requests.post("http://localhost:11434/api/generate", json=payload)
    response.raise_for_status()
except requests.exceptions.RequestException as e:
    # If there's an error, print it to the debug console
    print(f"Error: {e}", file=sys.stderr)
    print(f"Status Code: {response.status_code}", file=sys.stderr)
    print(f"Response Text: {response.text}", file=sys.stderr)
    sys.exit(1)


# Parse the response JSON
try:
    data = output = json.loads(response.content)["response"]
    print(data)
except (KeyError, ValueError):
    # If the response is not valid JSON, print an error message
    print("Error: Invalid response from server", file=sys.stderr)
    sys.exit(1)