import json
import requests
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
 auth = HTTPBasicAuth('admin', 'Admin_1234!')
 headers = {'Content-Type': 'application/json','Accept': 'application/json'}
 url = 'https://sandbox-nxos-1.cisco.com'
 payload = { "ins_api": {"version": "1.0", "type": "cli_show", "chunk": "0", "sid": "1", "input": 'show version', "output_format": "json"}}
 response = requests.post(url, data=json.dumps(payload), headers=headers, auth=auth)
 print(response)