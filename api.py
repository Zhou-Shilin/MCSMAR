import requests
from log_writer import log
import time

def get_status(url, uuid, remote_uuid, apikey):
    api_url = url + "/api/instance"

    _params = {
        "uuid": uuid,
        "remote_uuid": remote_uuid,
        "apikey": apikey
    }

    _headers = {
        "Content-Type": "application/json; charset=utf-8"
    }

    response = requests.get(api_url, params=_params, headers=_headers)

    if response.status_code == 200:
        json_response = response.json()

        data = json_response["data"]
        status = data["status"]

        tempLog = "[" + time.ctime() + "] (api.py/get_status) Successful 200, status=" + str(status) + ",data="
        log(tempLog)
        log(data)

        return status
    else:
        print("failed: ", response)

        tempLog = "[" + time.ctime() + "] (api.py/get_status) Failed " + response.status_code
        log(tempLog)

        return "failed"

def start_app(url, uuid, remote_uuid, apikey):
    api_url = url, "/api/protected_instance/open"

    _params = {
        "uuid": uuid,
        "remote_uuid": remote_uuid,
        "apikey": apikey
    }

    _headers = {
        "Content-Type": "application/json; charset=utf-8"
    }

    response = requests.get(api_url, params=_params, headers=_headers)

    if response.status_code == 200:
        data = json_response["data"]

        tempLog = "[" + time.ctime() + "] (api.py/start_app) Successful 200, data="
        log(tempLog)
        log(data)

        return True
    else:
        print("failed: ", response)

        tempLog = "[" + time.ctime() + "] (api.py/start_app) Failed " + response.status_code
        log(tempLog)

        return False
