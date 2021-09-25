"""
NX-API-BOT
"""
import requests
import json
"""
Modify these please
"""
url='https://sandbox-nxos-1.cisco.com'
switchuser='admin'
switchpassword='Admin_1234!'
myheaders={'content-type':'application/json-rpc'}
payload=[
{
"jsonrpc": "2.0",
"method": "cli",
"params": {
"cmd": "show version",
"version": 1.2
},
"id": 1
}
]
response = requests.post(url, data=json.dumps(payload), headers=myheaders, verify=False, auth=(switchuser,switchpassword)).json()