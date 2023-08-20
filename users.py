import time
import datetime


def get_user():
    user = input("What is your name?\n")
    return user


def get_time():
    current_time = datetime.datetime.now().time()
    current_year = datetime.datetime.now().year
    print(current_time, current_year)


get_time()
