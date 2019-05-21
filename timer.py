from datetime import date, timedelta, datetime

def timer():
    start_date = (date.today() + timedelta(days=30)).isoformat()
    return start_date

def timerdb(timing):
    start_date = (timing.date() + timedelta(days=30)).isoformat()
    return start_date

def today():
    return date.today()