import time

import requests


def call_service():
    url = "http://localhost:8089/service1"
    # url = "http://localhost:8089/nlp/han"

    headers = {
        "content-type": "application/json"
    }

    data = {
    }
    while True:
        try:
            time.sleep(0.5)
            # resp = requests.post(url, json=data, headers=headers)
            resp = requests.get(url)
            print(resp.content)
            #print(resp.json())
        except Exception as e :
            print(e)


if __name__ == '__main__':
    call_service()
