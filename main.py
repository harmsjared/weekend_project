import json
import datetime
import users
import guests
import messages
import companies


class Telegraph:
    # Greet user
    print(f"\nWelcome to Telegraph, {users.get_user()}.\n")

    # Ask which guest they need to contact
    print("What can I help you with?\n")

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
        specific_guest = guests.select_guest()

        # specify guest details
        first_name = specific_guest['firstName']
        last_name = specific_guest['lastName']
        room_number = specific_guest['roomNumber']
        check_in_hour = specific_guest['checkInTime']
        check_out_hour = specific_guest['checkOutTime']

        print(f"\nYou selected {first_name} {last_name}, staying in room: {room_number}.\n")

        print(f"Where is {first_name} staying?")

        companies.show_locations()

        selected_company = companies.validate_company()

        company_id = selected_company['id']
        company_name = selected_company['company']
        company_city = selected_company['city']
        company_zone = selected_company['timezone']

        # print(company_name)

        print(f"You selected {company_name}, located in {company_city}.\n")

        message_type = int(input(f"Would you like to send a pre-existing message to {first_name}, or type your own?\n"
                                 "1: Pre-Existing Message\n"
                                 "2: Custom Message\n"))

        if message_type == 1:
            print("\nOkay, which message would you like to send?")
            messages.show_messages()
            existing_message = int(input())


            if existing_message in messages:
                print(existing_message['id'])

        elif message_type == 2:
            print("\nGreat, let's type a custom message.")
            custom_message = input("\nWhat would you like your new message to say?\n")

            print(f"\nGreat, we'll send this message to {first_name}, staying at {company_name}.\n")
            print(custom_message)

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
