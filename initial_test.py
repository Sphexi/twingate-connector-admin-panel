#this file will be used to connect to the twingate graphql api using ariadne and get a list of all connectors
#it will then loop through the list and check if the connector is active or not
#it will then output the connector name and the status of the connector using print()

#this is the import for the graphql library
#import graphql
from ariadne import *
import requests
import json

#this is the url for the twingate graphql api
#you will need to replace the url with your twingate url
url = "https://sphexi.twingate.com/api/graphql/"

#this is the query that will be used to get the list of connectors
#you can find the query in the twingate graphql api documentation
#https://docs.twingate.com/docs/graphql-api
query = """{
  connectors(after: null, first:10) {
    edges {
      node {
        id
        name
        state
        lastHeartbeatAt
      }
    }
    pageInfo {
      startCursor
      hasNextPage
    }
  }
}
"""

				


#this is the header that will be used to authenticate to the twingate graphql api
#you will need to replace the x-api-key with your api key
#you can find your api key by logging into the twingate portal and going to the settings page
#you will find your api key under the api keys section
headers = {
    'X-API-KEY': 'CZOpp40B7verSmPAqlZKG1NZZbtqgDcLfyPaUes8Ylb_7utA5bDpnmAjBfIbmrMj-WRXQ_v2BWc59U4ZSw3ekciiSR6dmM4ffWDPoY8xWUgAF8_BTVKrFNjvekqcCkW7Y4T2WQ',
    'Content-Type': "application/json"
}

#this is the payload that will be used to send the query to the twingate graphql api
payload = query
print(payload)
#this is the response from the twingate graphql api
#this will send the query to the twingate graphql api and get the response
response = requests.request("POST", url, json={'query': payload}, headers=headers)

#this will convert the response from the twingate graphql api to a json object
#response = json.loads(response.text)

response_json = json.loads(response.text)['data']['connectors']['edges']
connectors = []
for connector in response_json:
    connectors.append(connector['node'])


print(connectors)
for x in response:
    print(x + ' test')
    print(response[x])
#this will loop through the list of connectors and print the name and state of each connector
for connector in response['data']['connectors']['edges']:
    print(connector['node']['name'] + ": " + connector['node']['state'])

#this will print a blank line
print()

#this will print the number of connectors that are active
print("Active Connectors: " + str(len([connector for connector in response['data']['connectors']['edges'] if connector['node']['state'] == "ALIVE"])))

#this will print the number of connectors that are inactive
print("Inactive Connectors: " + str(len([connector for connector in response['data']['connectors']['edges'] if connector['node']['state'] == "INACTIVE"])))

#this will print the number of connectors that are pending
print("Pending Connectors: " + str(len([connector for connector in response['data']['connectors']['edges'] if connector['node']['state'] == "PENDING"])))

#this will print the number of connectors that are disabled
print("Disabled Connectors: " + str(len([connector for connector in response['data']['connectors']['edges'] if connector['node']['state'] == "DISABLED"])))

#this will print the number of connectors that are unknown
print("Unknown Connectors: " + str(len([connector for connector in response['data']['connectors']['edges'] if connector['node']['state'] == "UNKNOWN"])))

#this will print the total number of connectors
print("Total Connectors: " + str(len(response['data']['connectors']['edges'])))

#this will print a blank line
print()

#this will print the percentage of connectors that are active
print("Active Connectors: " + str(round(len([connector for connector in response['data']['connectors']['edges'] if connector['node']['state'] == "ALIVE"]) / len(response['data']['connectors']['edges']) * 100, 2)) + "%")

#this will print the percentage of connectors that are inactive
print("Inactive Connectors: " + str(round(len([connector for connector in response['data']['connectors']['edges'] if connector['node']['state'] == "INACTIVE"]) / len(response['data']['connectors']['edges']) * 100, 2)) + "%")

#this will print the percentage of connectors that are pending
print("Pending Connectors: " + str(round(len([connector for connector in response['data']['connectors']['edges'] if connector['node']['state'] == "PENDING"]) / len(response['data']['connectors']['edges']) * 100, 2)) + "%")

#this will print the percentage of connectors that are disabled
print("Disabled Connectors: " + str(round(len([connector for connector in response['data']['connectors']['edges'] if connector['node']['state'] == "DISABLED"]) / len(response['data']['connectors']['edges']) * 100, 2)) + "%")

#this will print the percentage of connectors that are unknown
print("Unknown Connectors: " + str(round(len([connector for connector in response['data']['connectors']['edges'] if connector['node']['state'] == "UNKNOWN"]) / len(response['data']['connectors']['edges']) * 100, 2)) + "%")




