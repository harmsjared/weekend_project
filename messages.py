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


def get_message(message_type, specific_guest):
    if message_type == 1:
        print("\nOkay, which message would you like to send?")

        # prints existing messages
        messages.show_messages()

        # accept message_id as integer
        existing_message = int(input())

        new_message = messages.validate_message(existing_message)

        template = new_message.get('message')
        formatted_message = template.format(first_name=first_name, last_name=last_name,
                                            time_salutation=time_salutation, checkin_month_name=checkin_month_name,
                                            company_name=company_name, company_city=company_city,
                                            checkin_hour=checkin_hour,
                                            checkin_day=checkin_day, checkin_day_name=checkin_day_name,
                                            checkin_month=checkin_month, checkin_year=checkin_year,
                                            checkout_hour=checkout_hour, checkout_day=checkout_day,
                                            checkout_day_name=checkout_day_name, checkout_month=checkout_month,
                                            checkout_year=checkout_year, checkout_month_name=checkout_month_name)
        print(formatted_message)


    elif message_type == 2:
        print("\nGreat, let's type a custom message.")
        custom_message = input("\nWhat would you like your new message to say?\n")

        print(f"\nGreat, we'll send this message to {first_name}, staying at {company_name}.\n")
        print(custom_message)

# def print_messages():
#     message_info = guests.guest_checkin_time(141)
#
#     first_name = message_info.get('firstName')
#     checkin_time = datetime.datetime.fromtimestamp(message_info['check_in_time']).time()
#     checkin_hour = datetime.datetime.fromtimestamp(message_info['check_in_time']).strftime("%I:00 %p")
#
#     morning_start = datetime.time(6, 0, 0)
#     afternoon_start = datetime.time(12, 0, 0)
#     evening_start = datetime.time(18, 0, 0)
#
#     if checkin_time < morning_start:
#         time_salutation = "night"
#     elif checkin_time < afternoon_start:
#         time_salutation = "morning"
#     elif checkin_time < evening_start:
#         time_salutation = "afternoon"
#     else:
#         time_salutation = "evening"
#
#     print(checkin_time)
#     print(f"Good {time_salutation} {first_name}, your room at [company] will be ready at... {checkin_hour}!")
