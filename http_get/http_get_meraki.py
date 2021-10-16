#https://n149.meraki.com/DevNet-Always-On/n/ZV4Dxbvc/manage/usage/list
#!/usr/bin/env python3
import requests
import pprint
myheaders={'X-Cisco-Meraki-API-Key': <skip>}
orgId = '549236'
url = 'https://dashboard.meraki.com/api/v0/organizations/' + orgId +
'/networks'
response = requests.get(url, headers=myheaders, verify=False)
pprint.pprint(response.json())