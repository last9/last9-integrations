import os
import requests
import json

LEVITATE_REFRESH_TOKEN = os.getenv("LEVITATE_REFRESH_TOKEN")
LEVITATE_ACCESS_TOKEN_API = "https://app.last9.io/api/v4/oauth/access_token"
LEVITATE_ORG = os.getenv("LEVITATE_ORG")

def api_token():
    headers = {'Content-Type': 'application/json'}
    data = {"refresh_token": LEVITATE_REFRESH_TOKEN}
    response = requests.post(LEVITATE_ACCESS_TOKEN_API, headers=headers, data=json.dumps(data))

    if response.status_code != 200:
        raise Exception("Access Token can't be retrieved, {}".format(response.text))

    body = response.json()
    return body["access_token"]

if not LEVITATE_REFRESH_TOKEN:
    raise Exception("LEVITATE_REFRESH_TOKEN is not set")

if not LEVITATE_ORG:
    raise Exception("LEVITATE_ORG is not set")

url = "https://app.last9.io/api/v4/organizations/{}/change_events".format(LEVITATE_ORG)
headers = {
    'Content-Type': 'application/json',
    'X-LAST9-API-TOKEN': 'Bearer {}'.format(api_token())
}
data = {
    "event_name": "deployment",
    "event_state": "start",
    "attributes": {
        "revision": "<git_commit_sha>",
        "user": "john.smith",
        "environment": "production"
    }
}
response = requests.put(url, headers=headers, data=json.dumps(data))

if response.status_code == 200:
    print("Change event registered successfully")
else:
    raise Exception("Change Event -> Levitate failed. {}".format(response.text))
