
import requests
import json

"""
Modify these please
"""
#For NXAPI to authenticate the client using client certificate, set 'client_cert_auth' to True.
#For basic authentication using username & pwd, set 'client_cert_auth' to False.
client_cert_auth=False
switchuser='admin'
switchpassword='Admin_1234!'
#client_cert='PATH_TO_CLIENT_CERT_FILE'
#client_private_key='PATH_TO_CLIENT_PRIVATE_KEY_FILE'
#ca_cert='PATH_TO_CA_CERT_THAT_SIGNED_NXAPI_SERVER_CERT'

url='http://10.10.20.95/ins'
myheaders={'content-type':'application/json-rpc'}
payload=[
  {
    "jsonrpc": "2.0",
    "method": "cli",
    "params": {
      "cmd": "show version",
      "version": 1
    },
    "id": 1
  }
]
response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(switchuser,switchpassword)).json()
print(response)
