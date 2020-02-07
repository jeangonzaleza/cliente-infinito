import socket 
from datetime import datetime
import time
import requests
import json
  
def Main():
    while(True):
        host = 'http://34.66.186.52:8080/'
        #json_credential = 'cloudrun-credentials-266520-72b78095e227.json'
        #credentials = service_account.IDTokenCredentials.from_service_account_file(json_credential, target_audience = host)

        filename = "params_xy.json"

        with open(filename) as data:
            params = json.load(data)

        message = dict()
        message['message'] = json.dumps(params)
        #print(message)

        #session = AuthorizedSession(credentials)
        #message = None
        #request = session.post(host, data = message)
        requested = requests.post(host, json = message, timeout=1800.0)
        print(requested.text)
        time.sleep(3600)
  
if __name__ == '__main__': 
    Main() 
