import json
from typing import List

from app.Entity.Issue import Issue
from app.Entity.Workday import Workday
from app.Enum.Weekday import Weekday

def getWorkdays() -> List[Workday]:
    return parseJsonToWorkDays()

def parseJsonToWorkDays() -> List[Workday]:
    with open('.config.json', 'r') as file:
        data = json.load(file)

        result = []

        for item in data:
            issues = []
            for issueData in item['issues']:
                issue = Issue(issueData['key'], issueData['timeSpentHours'], issueData['comment'])
                issues.append(issue)

            workDay = Workday(Weekday(item['id']), issues)
            result.append(workDay)

        return result
