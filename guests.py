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
            guest_info = {
                "firstName": guest['firstName'],
                "lastName": guest['lastName'],
                "roomNumber": guest['reservation']['roomNumber'],
                "checkin": {
                    "day": time_assessment(room_number, "checkin_day"),
                    "month": time_assessment(room_number, "checkin_month"),
                    "year": time_assessment(room_number, "checkin_year"),
                    "checkinDayOfWeek": time_assessment(room_number, "checkin_day_of_week"),
                    "checkinTime": time_assessment(room_number, "hour_proximate_checkin"),
                },
                "checkout": {
                    "day": time_assessment(room_number, "checkout_day"),
                    "month": time_assessment(room_number, "checkout_month"),
                    "year": time_assessment(room_number, "checkout_year"),
                    "checkoutDayOfWeek": time_assessment(room_number, "checkout_day_of_week"),
                    "checkoutTime": time_assessment(room_number, "hour_proximate_checkout"),
                }
            }

            return guest_info


def time_assessment(room_reservation, format):
    # global checkin_time_salutation
    for guest in guests:
        if room_reservation == guest['reservation']['roomNumber']:
            unix_checkin_time = guest['reservation']['startTimestamp']
            unix_checkout_time = guest['reservation']['endTimestamp']



            #Check-In Information
            checkin_time = datetime.datetime.fromtimestamp(unix_checkin_time).time()
            checkin_hour = datetime.datetime.fromtimestamp(unix_checkin_time).strftime("%I:00 %p")
            checkin_day_of_week = datetime.datetime.fromtimestamp(unix_checkin_time).strftime("%A")
            checkin_day = datetime.datetime.fromtimestamp(unix_checkin_time).day
            checkin_month = datetime.datetime.fromtimestamp(unix_checkin_time).month
            checkin_year = datetime.datetime.fromtimestamp(unix_checkin_time).year

            #Check-Out Information
            checkout_time = datetime.datetime.fromtimestamp(unix_checkout_time).time()
            checkout_hour = datetime.datetime.fromtimestamp(unix_checkout_time).strftime("%I:00 %p")
            checkout_day_of_week = datetime.datetime.fromtimestamp(unix_checkout_time).strftime("%A")
            checkout_day = datetime.datetime.fromtimestamp(unix_checkout_time).day
            checkout_month = datetime.datetime.fromtimestamp(unix_checkout_time).month
            checkout_year = datetime.datetime.fromtimestamp(unix_checkout_time).year




            morning_start = datetime.time(6, 0, 0)
            afternoon_start = datetime.time(12, 0, 0)
            evening_start = datetime.time(18, 0, 0)

            if checkin_time < morning_start:
                checkin_time_salutation = "night"
            elif checkin_time < afternoon_start:
                checkin_time_salutation = "morning"
            elif checkin_time < evening_start:
                checkin_time_salutation = "afternoon"
            else:
                checkin_time_salutation = "evening"

            if checkout_time < morning_start:
                checkout_time_salutation = "night"
            elif checkout_time < afternoon_start:
                checkout_time_salutation = "morning"
            elif checkout_time < evening_start:
                checkout_time_salutation = "afternoon"
            else:
                checkout_time_salutation = "evening"


            if format == "checkin_time_salutation":
                return checkin_time_salutation
            elif format == "checkout_time_salutation":
                return checkout_time_salutation
            elif format == "hour_proximate_checkin":
                return checkin_hour
            elif format == "hour_proximate_checkout":
                return checkout_hour
            elif format == "checkin_day_of_week":
                return checkin_day_of_week
            elif format == "checkout_day_of_week":
                return checkout_day_of_week
            elif format == "checkin_year":
                return checkin_year
            elif format == "checkout_year":
                return checkout_year
            elif format == "checkin_month":
                return checkin_month
            elif format == "checkout_month":
                return checkout_month
            elif format == "checkin_day":
                return checkin_day
            elif format == "checkout_day":
                return checkout_day
            else:
                return "Hi! :)"
