import json
import datetime
import guests

# import messages.json, save as messages
with open("messages.json") as message_data:
    messages = json.load(message_data)


def show_messages():
    i = 1
    for message in messages:
        print(f"{message['id']}: {message['message']}")
        i += 1


def validate_message(specific_message):
    for message in messages:
        if specific_message == message['id']:
            return message


def print_messages():
    message_info = guests.guest_checkin_time(141)

    first_name = message_info.get('firstName')
    checkin_time = datetime.datetime.fromtimestamp(message_info['check_in_time']).time()
    checkin_hour = datetime.datetime.fromtimestamp(message_info['check_in_time']).strftime("%I:00 %p")

    morning_start = datetime.time(6, 0, 0)
    afternoon_start = datetime.time(12, 0, 0)
    evening_start = datetime.time(18, 0, 0)

    if checkin_time < morning_start:
        time_salutation = "night"
    elif checkin_time < afternoon_start:
        time_salutation = "morning"
    elif checkin_time < evening_start:
        time_salutation = "afternoon"
    else:
        time_salutation = "evening"

    print(checkin_time)
    print(f"Good {time_salutation} {first_name}, your room at [company] will be ready at... {checkin_hour}!")
