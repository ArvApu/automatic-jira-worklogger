from datetime import datetime, timedelta, timezone
from app.Enum.Weekday import Weekday

def getStartOfTheWeek() -> datetime:
    today = datetime.now(timezone.utc)
    startOfTheWeek = today - timedelta(days=today.weekday())

    return startOfTheWeek.replace(hour=0, minute=0, second=0, microsecond=0)

def getDayDateOfWeek(startOfTheWeekDate: datetime, weekday: Weekday) -> datetime:
    return startOfTheWeekDate + timedelta(days=(weekday.value - 1))
