#file to contain the graphql queries to twingate
#this file will be used to connect to the twingate graphql api using ariadne and get a list of all connectors
import __main__
from globals import *

url = "https://" + TWINGATE_DOMAIN + ".twingate.com/api/graphql/"
headers = {
    'X-API-KEY': TWINGATE_API_KEY,
    'Content-Type': "application/json"
}

def connectors():
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

    response = requests.request("POST", url, json={'query': query}, headers=headers)
    response_json = json.loads(response.text)['data']['connectors']['edges']
    connectors = []
    for connector in response_json:
        connectors.append(connector['node'])
    return connectors

def devices():
    query = """{
  devices(after: null, first:100) {
    edges {
      node {
        id
        name
        isTrusted
        osName
        deviceType

      }
    }
    pageInfo {
      startCursor
      hasNextPage
    }
  }
}
    """

    response = requests.request("POST", url, json={'query': query}, headers=headers)
    response_json = json.loads(response.text)['data']['devices']['edges']
    devices = []
    for device in response_json:
        devices.append(device['node'])
    return devices

def resources():
    query = """{
  resources(after: null, first:100) {
    edges {
      node {
        id
        name
        createdAt
        updatedAt
        isActive
        remoteNetwork{
            name
        }
        address {
                type
                value
                }
        protocols {
                allowIcmp
                tcp {
                    policy
                    ports {
                        start
                        end
                    }
                }
                udp{
                    policy
                    ports {
                        start
                        end
                    }
                }
        }

      }
    }
    pageInfo {
      startCursor
      hasNextPage
    }
  }
}"""

    response = requests.request("POST", url, json={'query': query}, headers=headers)
    response_json = json.loads(response.text)['data']['resources']['edges']
    resources = []
    for resource in response_json:
        resources.append(resource['node'])
    return resources