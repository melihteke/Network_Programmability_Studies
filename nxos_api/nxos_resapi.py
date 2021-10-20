import requests
import json
import re

url = "https://sandbox-nxos-1.cisco.com"

r = requests.get(url,
        headers = restconf_headers,
        auth=(device["username"], device["password"]),
        verify=False)