import os

from datetime import datetime, timedelta
from dotenv import load_dotenv

from app.Entity.JiraClientConfiguration import JiraClientConfiguration
from app.Enum.Weekday import Weekday
from app.Service import WorkdaysProvider
from app.Client import JiraClient

def main() -> None:
    startOfTheWeek = getStartOfTheWeek()
    config = getJiraClientConfiguration()
    workerId = JiraClient.getWorkerId(config)

    for day in WorkdaysProvider.getWorkdays():
        for issue in day.issues:
            JiraClient.createWorklog(
                {
                    'originTaskId': issue.key,
                    'timeSpentSeconds': issue.timeSpentHours * 3600,
                    'started': getDayDateOfWeek(startOfTheWeek, day.dayId).strftime('%Y-%m-%d'),
                    'comment': issue.comment,
                    'worker': workerId,
                },
                config
            )

def getStartOfTheWeek() -> datetime:
    today = datetime.now()
    startOfTheWeek = today - timedelta(days=today.weekday())

    return startOfTheWeek.replace(hour=0, minute=0, second=0, microsecond=0)

def getDayDateOfWeek(startOfTheWeekDate: datetime, weekday: Weekday) -> datetime:
    return startOfTheWeekDate + timedelta(days=(weekday.value - 1))

def getJiraClientConfiguration() -> JiraClientConfiguration:
    load_dotenv('.env')

    token = os.getenv('JIRA_PERSONAL_ACCESS_TOKEN')
    baseUrl = os.getenv('JIRA_BASE_URL')

    return JiraClientConfiguration(baseUrl, token)

if __name__ == "__main__":
    main()
