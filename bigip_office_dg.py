#!/usr/bin/python
import json
import tempfile
import urllib2
import uuid
import os
import datetime

# Settings
fileversion = "/tmp/microsoft_version.txt"
fileDG = "/tmp/exchangedg.txt"
datagroupName = "office"

# helper to call the webservice and parse the response
def webApiGet(methodName, instanceName, clientRequestId):
    ws = https://endpoints.office.com
    requestPath = ws + '/' + methodName + '/' + instanceName + '?clientRequestId=' + clientRequestId
    response = urllib2.urlopen(requestPath)
    return json.loads(response.read().decode())

print(str(datetime.datetime.now())+" Starting office ip addresses update")
# Generate Client ID
clientRequestId = str(uuid.uuid4())

# Check version
try:
    f = open(fileversion)
    latestVersion = f.read()
except:
    latestVersion = '0000000000'
    f = open(fileversion, "w")
    f.write(latestVersion)
finally:
    f.close()

# call version method to check the latest version, and pull new data if version number is different
version = webApiGet('version', 'Worldwide', clientRequestId)
f = open("/tmp/microsoft_version.txt", "w")
f.write(version['latest'])
f.close()

print(str(datetime.datetime.now()) + " DB local Version: " + latestVersion)
print(str(datetime.datetime.now()) + " DB Online Version: " + version['latest'])

if version['latest'] > latestVersion:
    print(str(datetime.datetime.now()) + ' New version of Office 365 worldwide IP Addresses detected')
# write the new version number to the data file
    # invoke endpoints method to get the new data
    endpointSets = webApiGet('endpoints', 'Worldwide', clientRequestId)
    # filter results for Allow and Optimize endpoints, and transform these into tuples with port and category
    flatIps = []
    for endpointSet in endpointSets:
        if endpointSet['category'] in ('Optimize', 'Allow') and endpointSet['serviceArea'] in ('Exchange'):
            ips = endpointSet['ips'] if 'ips' in endpointSet else []
            # IPv4 strings have dots while IPv6 strings have colons
            ip4s = [ip for ip in ips if '.' in ip]
            flatIps.extend([(ip) for ip in ip4s])
    f = open(fileDG, "w")
    for ip in sorted(set(flatIps)):
       f.write("network "+ip+",\n")
    f.close()
    # TODO send mail (e.g. with smtplib/email modules) with new endpoints data
    print(str(datetime.datetime.now()) + ' Updating datagroup '+datagroupName)
    os.system("tmsh modify sys file data-group "+datagroupName+" source-path file:"+fileDG)
else:
    print(str(datetime.datetime.now()) + ' Office 365 worldwide IP Addresses are up-to-date')

