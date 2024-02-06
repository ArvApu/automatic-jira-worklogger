import os

from dotenv import load_dotenv

from app.Entity.JiraClientConfiguration import JiraClientConfiguration
from app.Service import WorkdaysProvider
from app.Service import WeekdayService
from app.Client import JiraClient

def main() -> None:
    # Services are not classes and no DI because I am lazy, one day will fix that... maybe... :D
    configuration = getJiraClientConfiguration()
    startOfTheWeek = WeekdayService.getStartOfTheWeek()
    currentUser = JiraClient.getCurrentUser(configuration)

    print(f"Worklog will be updated for user: {currentUser['displayName']}")

    for day in WorkdaysProvider.getWorkdays():
        for issue in day.issues:
            date = WeekdayService.getDayDateOfWeek(startOfTheWeek, day.dayId)

            worklog = JiraClient.createWorklog(
                configuration,
                issue.key,
                {
                    'timeSpentSeconds': issue.timeSpentHours * 3600,
                    'started': date.strftime('%Y-%m-%dT%H:%M:%S.%f%z'),
                    'comment': issue.comment,
                    'workerId': currentUser['accountId'],
                },
            )

            print(f"Worklog created for '{issue.key}' on date {date.strftime('%Y-%m-%d')}. Id: {worklog['id']}")

def getJiraClientConfiguration() -> JiraClientConfiguration:
    load_dotenv('.env')

    return JiraClientConfiguration(
        os.getenv('JIRA_BASE_URL'),
        os.getenv('ATLASSIAN_USERNAME'),
        os.getenv('ATLASSIAN_API_TOKEN'),
    )

if __name__ == "__main__":
    main()
