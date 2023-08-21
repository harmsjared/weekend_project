import json
import datetime
import guests
import users

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


def get_message(specific_guest, company_info):
    hour, minute, time_salutation, am_pm = users.get_current_time()
    print("\nOkay, which message would you like to send?")

    # prints existing messages
    show_messages()

    # accept message_id as integer
    existing_message = int(input())

    new_message = validate_message(existing_message)

    template = new_message.get('message')
    formatted_message = (template.format
        (
        first_name=specific_guest.get("first_name"),
        last_name=specific_guest.get("last_name"),
        time_salutation=time_salutation,
        company_name=company_info.get('company_name'),
        company_city=company_info.get('company_city'),

        checkin_hour=specific_guest.get("checkin").get("time"),
        checkin_day=specific_guest.get("checkin").get("day"),
        checkin_day_name=specific_guest.get("checkin").get("day_name"),
        checkin_month=specific_guest.get("checkin").get("month"),
        checkin_month_name=specific_guest.get("checkin").get("month_name"),
        checkin_year=specific_guest.get("checkin").get("year"),

        checkout_hour=specific_guest.get("checkout").get("time"),
        checkout_day=specific_guest.get("checkout").get("day"),
        checkout_day_name=specific_guest.get("checkout").get("day_name"),
        checkout_month=specific_guest.get("checkout").get("month"),
        checkout_month_name=specific_guest.get("checkout").get("month_name"),
        checkout_year=specific_guest.get("checkout").get("year")
    )
    )

    print(formatted_message)


def custom_message(specific_guest, company_info):
    print("\nGreat, let's type a custom message.")
    custom_message = input("\nWhat would you like your new message to say?\n")

    print(
        f"\nGreat, we'll send this message to {specific_guest.get('first_name')}, staying at {company_info.get('company_name')}.\n")
    print(f"Message: {custom_message}")
