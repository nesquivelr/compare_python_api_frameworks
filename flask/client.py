import json

import requests


def run():
    url = "http://localhost:5000/"
    data = {"id": "AN1234"}
    headers = {"Content-type": "application/json", "Accept": "text/plain"}
    r = requests.post(url, data=json.dumps(data), headers=headers)
    print(r.json()["status"])


if __name__ == "__main__":
    run()
