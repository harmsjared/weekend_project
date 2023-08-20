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


def validate_guest_room():
    print("\nWhich guest would you like to contact?")
    show_guests()
    choice = int(input("Please enter the corresponding room number:\n> "))

    for guest in guests:
        room_number = guest['reservation']['roomNumber']
        if choice == room_number:
            guest_info = {
                "firstName": guest['firstName'],
                "lastName": guest['lastName'],
                "roomNumber": guest['reservation']['roomNumber'],
                "checkInTime": datetime.datetime.fromtimestamp(guest['reservation']['startTimestamp']).strftime("%I"
                                                                                                                ":%M "
                                                                                                                "%p"),
                "checkOutTime": datetime.datetime.fromtimestamp(guest['reservation']['endTimestamp']).strftime(
                    "%I:%M %p"),
            }

            return guest_info


def guest_checkin_time(room_number):
    for guest in guests:
        if room_number == guest['reservation']['roomNumber']:
            message_data = {
                "firstName": guest['firstName'],
                "check_in_time": guest['reservation']['startTimestamp']
            }

            return message_data
