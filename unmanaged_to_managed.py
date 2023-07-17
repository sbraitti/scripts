import requests
from requests.auth import HTTPBasicAuth
import json

WAPI_URL = "https://10.2.1.130/wapi/v2.12/" 
user = "admin"
password = "infoblox"

def get_unmanaged(network):
    url = WAPI_URL + "ipv4address?network=" + network + "&types=UNMANAGED&_return_fields=discovered_data,mac_address,ip_address"
    response = requests.get(url, verify=False, auth = HTTPBasicAuth(user,password))
    for item in response.json():
        #print(json.dumps(item))
        if item['discovered_data'].get('discovered_name') is not None:
            create_host(item)
    #print(json.dumps(response.json(), indent=1))

def create_host(item):
    url = WAPI_URL + 'record:host'
    data = {
        "name":item["discovered_data"].get("discovered_name"),
        "configure_for_dns": False,
        "ipv4addrs":
        [
            {
            "ipv4addr":item["ip_address"],
            "configure_for_dhcp": False
            }
        ]
        }
    response = requests.post(url, verify=False, auth = HTTPBasicAuth(user,password), json=data)
    print(response.json())
get_unmanaged("172.31.254.0/24")
#url = WAPI_URL + "network"



