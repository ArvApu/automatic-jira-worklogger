import requests
import os

from datetime import datetime, timedelta
from dotenv import load_dotenv

from app.Entity.JiraClientConfiguration import JiraClientConfiguration
from app.Enum.Weekday import Weekday
from app.Service import WorkdaysProvider

def main() -> None:
    startOfTheWeek = getStartOfTheWeek()
    config = getJiraClientConfiguration()
    workerId = getWorkerId(config)

    for day in WorkdaysProvider.getWorkdays():
        for issue in day.issues:
            createWorklog(
                {
                    'originTaskId': issue.key,
                    'timeSpentSeconds': issue.timeSpentHours * 3600,
                    'started': getDayDateOfWeek(startOfTheWeek, day.dayId).strftime('%Y-%m-%d'),
                    'comment': issue.comment,
                    'worker': workerId,
                },
                config
            )

def createWorklog(data: dict, configuration: JiraClientConfiguration) -> None:
    endpoint = f'{configuration.baseUrl}/rest/tempo-timesheets/4/worklogs'

    response = requests.post(endpoint, headers=configuration.getHeaders(), json=data)

    if response.status_code != 200:
        raise Exception(f"Failed to create worklog for {data['originTaskId']}. Error: {response.text}")

    print(f"Worklog created successfully for '{data['originTaskId']}' on date {data['started']}")

def getStartOfTheWeek() -> datetime:
    today = datetime.now()
    startOfTheWeek = today - timedelta(days=today.weekday())
    return startOfTheWeek.replace(hour=0, minute=0, second=0, microsecond=0)

def getDayDateOfWeek(startOfTheWeekDate: datetime, weekday: Weekday) -> datetime:
    return startOfTheWeekDate + timedelta(days=(weekday.value - 1))

def getWorkerId(configuration: JiraClientConfiguration) -> str:
    endpoint = f'{configuration.baseUrl}/rest/api/2/myself'

    response = requests.get(endpoint, headers=configuration.getHeaders())

    if response.status_code != 200:
        raise Exception(f"Failed to fetch worker details. Response: {response.text}")

    userData = response.json()

    print(f"Worklog will be updated for user: {userData['name']}")

    return userData['key']

def getJiraClientConfiguration() -> JiraClientConfiguration:
    load_dotenv('.env')

    token = os.getenv('JIRA_PERSONAL_ACCESS_TOKEN')
    baseUrl = os.getenv('JIRA_BASE_URL')

    return JiraClientConfiguration(baseUrl, token)

if __name__ == "__main__":
    main()
