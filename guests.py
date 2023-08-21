import json
import datetime

# Import guests.json, save as guests
with open("guests.json", "r") as guest_data:
    guests = json.load(guest_data)


# Gets room number of each guest
def get_room_number(guests):
    return guests['reservation']['roomNumber']


# sort guests, order by room number (aesthetic)
guests = sorted(guests, key=get_room_number)


# print(guests)
def show_guests():
    print('\nGuests:')
    for guest in guests:
        print(f"{guest['reservation']['roomNumber']}: {guest['firstName']} {guest['lastName']}")
    print(" ")


# Finds guest and gets guest attributes
def select_guest(choice):
    found_guest = False
    for guest in guests:
        room_number = guest['reservation']['roomNumber']
        if choice == room_number:
            found_guest = True
            unix_checkin_time, unix_checkout_time = guest['reservation']['startTimestamp'], guest['reservation'][
                'endTimestamp']

            guest_info = {
                "first_name": guest['firstName'],
                "last_name": guest['lastName'],
                "room_number": guest['reservation']['roomNumber'],
                "checkin": {
                    "day": time_assessment(unix_checkin_time, "day"),
                    "day_name": time_assessment(unix_checkin_time, "day_name"),
                    "month": time_assessment(unix_checkin_time, "month"),
                    "month_name": time_assessment(unix_checkin_time, "month_name"),
                    "year": time_assessment(unix_checkin_time, "year"),
                    "time": time_assessment(unix_checkin_time, "hour"),
                },
                "checkout": {
                    "day": time_assessment(unix_checkout_time, "day"),
                    "day_name": time_assessment(unix_checkout_time, "day_name"),
                    "month": time_assessment(unix_checkout_time, "month"),
                    "month_name": time_assessment(unix_checkout_time, "month_name"),
                    "year": time_assessment(unix_checkout_time, "year"),
                    "time": time_assessment(unix_checkout_time, "hour"),
                }
            }
            return guest_info


# Parses time, returns multiple formats
def time_assessment(unix_timestamp, format):
    valid_formats = ["hour", "day", "day_name", "month", "month_name", "year"]

    # Error handling
    if unix_timestamp is None or format is None:
        raise ValueError("Missing required argument(s)")

    try:
        time = datetime.datetime.fromtimestamp(unix_timestamp)

    except ValueError:

        raise ValueError("Invalid Unix timestamp")

    if format not in valid_formats:
        raise ValueError("Invalid format")

    hour = time.strftime("%I:00 %p")
    day_of_week = time.strftime("%A")
    day = time.day
    month = time.month
    month_name = time.strftime("%B")
    year = time.year

    if format == "hour":
        return hour
    elif format == "day":
        return day

    elif format == "day_name":

        return day_of_week

    elif format == "month":

        return month

    elif format == "month_name":

        return month_name

    elif format == "year":

        return year

    else:

        return None
