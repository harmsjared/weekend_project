import time
from datetime import datetime


def get_user():
    user = input("What is your name?\n")
    return user


def get_current_date():
    now = datetime.now()
    # Get current day of the week in English
    day_names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    current_day = day_names[now.weekday()]

    month_names = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
                   "November", "December"]
    current_month = month_names[now.month - 1]
    current_year = now.year
    current_date = now.day
    return current_day, current_month, current_year, current_date


def get_current_time():
    now = datetime.now().time()
    now_hour = now.hour
    current_minute = now.minute

    if now_hour < 12:
        time_salutation = "morning",
        am_pm = "AM"
    elif now_hour < 18:
        time_salutation = "afternoon",
        am_pm = "PM"
    else:
        time_salutation = "evening"
        am_pm = "PM"

    if now_hour == 0:
        current_hour = 12
    elif now_hour > 12:
        current_hour = now_hour - 12
    else:
        current_hour = now_hour

    return current_hour, current_minute, time_salutation, am_pm
