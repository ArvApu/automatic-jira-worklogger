import requests

from app.Entity.JiraClientConfiguration import JiraClientConfiguration

def createWorklog(configuration: JiraClientConfiguration, issueId: str, data: dict) -> dict:
    endpoint = f"{configuration.baseUrl}/rest/api/2/issue/{issueId}/worklog"

    response = requests.post(endpoint, headers=configuration.getHeaders(), json=data)

    if response.status_code != 201:
        raise Exception(f"Failed to create worklog for {issueId}. Error: {response.text}")

    return response.json()

def getCurrentUser(configuration: JiraClientConfiguration) -> dict:
    endpoint = f'{configuration.baseUrl}/rest/api/2/myself'

    response = requests.get(endpoint, headers=configuration.getHeaders())

    if response.status_code != 200:
        raise Exception(f"Failed to fetch worker details. Error: {response.text}")

    return response.json()
