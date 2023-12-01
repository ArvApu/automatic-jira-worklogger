from typing import List

from app.Entity.Issue import Issue
from app.Enum.Weekday import Weekday

class Workday:
    def __init__(self, dayId: Weekday, issues: List[Issue]):
        self.dayId = dayId
        self.issues = issues
