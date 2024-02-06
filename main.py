import os

from dotenv import load_dotenv

from app.Entity.JiraClientConfiguration import JiraClientConfiguration
from app.Service import WorkdaysProvider
from app.Service import WeekdayService
from app.Client import JiraClient

def main() -> None:
    startOfTheWeek = WeekdayService.getStartOfTheWeek()
    config = getJiraClientConfiguration()
    workerId = JiraClient.getWorkerId(config)

    for day in WorkdaysProvider.getWorkdays():
        for issue in day.issues:
            JiraClient.createWorklog(
                {
                    'originTaskId': issue.key,
                    'timeSpentSeconds': issue.timeSpentHours * 3600,
                    'started': WeekdayService.getDayDateOfWeek(startOfTheWeek, day.dayId).strftime('%Y-%m-%d'),
                    'comment': issue.comment,
                    'worker': workerId,
                },
                config
            )

def getJiraClientConfiguration() -> JiraClientConfiguration:
    load_dotenv('.env')

    token = os.getenv('JIRA_PERSONAL_ACCESS_TOKEN')
    baseUrl = os.getenv('JIRA_BASE_URL')

    return JiraClientConfiguration(baseUrl, token)

if __name__ == "__main__":
    main()
