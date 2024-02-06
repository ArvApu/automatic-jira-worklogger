import requests

from app.Entity.JiraClientConfiguration import JiraClientConfiguration

def createWorklog(data: dict, configuration: JiraClientConfiguration) -> None:
    endpoint = f'{configuration.baseUrl}/rest/tempo-timesheets/4/worklogs'

    response = requests.post(endpoint, headers=configuration.getHeaders(), json=data)

    if response.status_code != 200:
        raise Exception(f"Failed to create worklog for {data['originTaskId']}. Error: {response.text}")

    print(f"Worklog created successfully for '{data['originTaskId']}' on date {data['started']}")

def getWorkerId(configuration: JiraClientConfiguration) -> str:
    endpoint = f'{configuration.baseUrl}/rest/api/2/myself'

    response = requests.get(endpoint, headers=configuration.getHeaders())

    if response.status_code != 200:
        raise Exception(f"Failed to fetch worker details. Response: {response.text}")

    userData = response.json()

    print(f"Worklog will be updated for user: {userData['name']}")

    return userData['key']
