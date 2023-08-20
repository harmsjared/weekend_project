import json
import datetime

# Import guests.json, save as guests
with open("guests.json", "r") as guest_data:
    guests = json.load(guest_data)


def get_room_number(guests):
    return guests['reservation']['roomNumber']


# I could have sorted this dict however, but seeing room_number(s)
# in order made the most sense to me
guests = sorted(guests, key=get_room_number)


# print(guests)
def show_guests():
    print('\nGuests:')
    for guest in guests:
        room_number = guest['reservation']['roomNumber']
        first_name = guest['firstName']
        last_name = guest['lastName']
        check_in_time = datetime.datetime.fromtimestamp(guest['reservation']['startTimestamp']).strftime("%I:%M %p")
        check_out_time = datetime.datetime.fromtimestamp(guest['reservation']['endTimestamp']).strftime("%I:%M %p")
        print(f"{room_number}: {first_name} {last_name}")
    print(" ")


def select_guest(choice):
    for guest in guests:
        room_number = guest['reservation']['roomNumber']
        if choice == room_number:
            unix_checkin_time = guest['reservation']['startTimestamp']
            unix_checkout_time = guest['reservation']['endTimestamp']

            guest_info = {
                "firstName": guest['firstName'],
                "lastName": guest['lastName'],
                "roomNumber": guest['reservation']['roomNumber'],
                "checkin": {
                    "day": time_assessment(unix_checkin_time, "day"),
                    "month": time_assessment(unix_checkin_time, "month"),
                    "year": time_assessment(unix_checkin_time, "year"),
                    "checkinDayOfWeek": time_assessment(unix_checkin_time, "day_of_week"),
                    "checkinTime": time_assessment(unix_checkin_time, "hour"),
                },
                "checkout": {
                    "day": time_assessment(unix_checkout_time, "day"),
                    "month": time_assessment(unix_checkout_time, "month"),
                    "year": time_assessment(unix_checkout_time, "year"),
                    "checkoutDayOfWeek": time_assessment(unix_checkout_time, "day_of_week"),
                    "checkoutTime": time_assessment(unix_checkout_time, "hour"),
                }
            }
            return guest_info


def time_assessment(unix_timestamp, format):

    valid_formats = ["hour", "day_of_week", "day", "month", "year"]

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
    year = time.year

    if format == "hour":
        return hour
    elif format == "day_of_week":
        return day_of_week
    elif format == "day":
        return day
    elif format == "month":
        return month
    elif format == "year":
        return year
    else:
        return None
