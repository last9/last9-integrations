import os
import requests
import json

LAST9_REFRESH_TOKEN = os.getenv("LAST9_REFRESH_TOKEN")
LAST9_ACCESS_TOKEN_API = "https://app.last9.io/api/v4/oauth/access_token"
LAST9_ORG = os.getenv("LAST9_ORG")

def api_token():
    headers = {'Content-Type': 'application/json'}
    data = {"refresh_token": LAST9_REFRESH_TOKEN}
    response = requests.post(LAST9_ACCESS_TOKEN_API, headers=headers, data=json.dumps(data))

    if response.status_code != 200:
        raise Exception("Access Token can't be retrieved, {}".format(response.text))

    body = response.json()
    return body["access_token"]

if not LAST9_REFRESH_TOKEN:
    raise Exception("LAST9_REFRESH_TOKEN is not set")

if not LAST9_ORG:
    raise Exception("LAST9_ORG is not set")

url = "https://app.last9.io/api/v4/organizations/{}/change_events".format(LAST9_ORG)
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
    raise Exception("Change Event -> Last9 failed. {}".format(response.text))
