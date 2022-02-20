import requests
import sys

url = "replace me with a discord webhook URL"

data = {
    "content": "Server host performed activity",
    "username": "FTB Endeavour Server"
}

if sys.argv[1] == 'shutdown':
    data["embeds"] = [
        {
            "description": "The service was stopped by systemd",
            "title": "Server shutdown"
        }
    ]

if sys.argv[1] == 'restart':
    data["embeds"] = [
        {
            "description": "The service is being restarted by systemd",
            "title": "Server restarting"
        }
    ]

result = requests.post(url, json = data)

try:
    result.raise_for_status()
except requests.exceptions.HTTPError as err:
    print(err)
else:
    print("Webhook spammed successfully")