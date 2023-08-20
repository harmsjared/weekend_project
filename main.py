import json
import datetime
import users
import guests
import messages
import companies



class Telegraph:
    # Greet user
    print(f"\nWelcome to Telegraph, {users.get_user().title()}.")

    current_day, current_month, current_year, current_date = users.get_current_date()
    # day, month, year = users.get_current_date()
    # print(current_day, current_month, current_year, current_date)

    # print(f"The time is {users.show_time()}")
    print(f"Today is {current_day}, {current_month} {current_date}, {current_year}.")
    hour, minute, time_salutation, am_pm = users.get_current_time()
    print(f"The time is {hour}:{minute} {am_pm}.\n")

    # Ask which guest they need to contact
    print("Main Menu")
    print("---------")
    print("What can I help you with today?")

    # Show command options
    print("1. Show Guests\n"
          "2. Contact Guest\n")

    # Take input as room_number of guest
    selected_action = int(input())

    if selected_action == 1:
        # Show list of guests
        guests.show_guests()

    elif selected_action == 2:
        print("\nWhich guest would you like to contact?")
        guests.show_guests()
        choice = int(input("Please enter the corresponding room number:\n> "))

        # Select guest
        specific_guest = guests.select_guest(choice)

        # specify guest details
        first_name = specific_guest.get("firstName")
        last_name = specific_guest.get("lastName")
        room_number = specific_guest.get("roomNumber")

        # Check-In
        checkin_day = specific_guest.get("checkin").get("day")
        checkin_month = specific_guest.get("checkin").get("month")
        checkin_year = specific_guest.get("checkin").get("year")
        checkin_hour = specific_guest.get("checkin").get("checkinTime")

        # Check-Out
        checkout_day = specific_guest.get("checkout").get("day")
        checkout_month = specific_guest.get("checkout").get("month")
        checkout_year = specific_guest.get("checkout").get("year")
        checkout_hour = specific_guest.get("checkout").get("checkoutTime")

        # print(first_name, last_name, room_number, checkin_day, checkin_hour, checkin_year, checkin_hour)
        # print(checkout_day, checkout_hour, checkout_year, checkout_month)

        print(f"\nWhere is {first_name} staying?")

        companies.get_companies()

        choice = int(input("\nPlease select the corresponding company number:\n"))

        # company_info_list = companies.get_company_details()
        #
        # print(company_info_list)
        #
        # print(f"You selected {company_name}, located in {company_city}.\n")
        #
        # message_type = int(input(f"Would you like to send a pre-existing message to {first_name}, or type your own?\n"
        #                          "1: Pre-Existing Message\n"
        #                          "2: Custom Message\n"))
        #
        # if message_type == 1:
        #     print("\nOkay, which message would you like to send?")
        #     messages.show_messages()
        #     existing_message = int(input())
        #
        #     if existing_message in messages:
        #         print(existing_message['message'])
        #
        # elif message_type == 2:
        #     print("\nGreat, let's type a custom message.")
        #     custom_message = input("\nWhat would you like your new message to say?\n")
        #
        #     print(f"\nGreat, we'll send this message to {first_name}, staying at {company_name}.\n")
        #     print(custom_message)

        # print("Which message would you like to send?\n")
        # messages.show_messages()
        #
        # specific_message = int(input())
        #
        # specific_message = messages.validate_message(specific_message)
        #
        # message_id = specific_message['id']
        # message_text = specific_message['message']
        # message_memo = specific_message['memo']
        #
        # print(f"{message_text}")

    # guests.validate_room()

    # if selected_room in guests['reservation']['roomNumber']:
    #     print("that guest is here")
    # else:
    #     print("no guest here in that room")
