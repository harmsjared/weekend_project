# import users
# import guests
# import messages
# import companies
#
#
# class Telegraph:
#     # Greet user, accept name as input
#     print(f"\nWelcome to Telegraph, {users.get_user().title()}.")
#
#     # Get date data
#     current_day, current_month, current_year, current_date = users.get_current_date()
#     print(f"Today is {current_day}, {current_month} {current_date}, {current_year}.")
#
#     # Get time data
#     hour, minute, time_salutation, am_pm = users.get_current_time()
#     print(f"The time is {hour}:{minute} {am_pm}.\n")
#
#     print("Main Menu")
#     print("---------")
#     print("What can I help you with today?")
#
#     # Show command options
#     print("1. Show Guests\n"
#           "2. Contact Guest\n")
#
#     # Take input as room_number of guest
#     selected_action = int(input())
#
#     if selected_action == 1:
#         # Show list of guests
#         guests.show_guests()
#
#     elif selected_action == 2:
#         print("\nWhich guest would you like to contact?")
#         # Show list of guests
#         guests.show_guests()
#         choice = int(input("Please enter the corresponding room number:\n> "))
#
#         # Select guest
#         specific_guest = guests.select_guest(choice)
#
#         # specify guest details
#         first_name = specific_guest.get("first_name")
#         last_name = specific_guest.get("last_name")
#         room_number = specific_guest.get("room_number")
#
#         # Check-In
#         checkin_hour = specific_guest.get("checkin").get("time")
#         checkin_day = specific_guest.get("checkin").get("day")
#         checkin_day_name = specific_guest.get("checkin").get("day_name")
#         checkin_month = specific_guest.get("checkin").get("month")
#         checkin_month_name = specific_guest.get("checkin").get("month_name")
#         checkin_year = specific_guest.get("checkin").get("year")
#
#         # Check-Out
#         checkout_hour = specific_guest.get("checkout").get("time")
#         checkout_day = specific_guest.get("checkout").get("day")
#         checkout_day_name = specific_guest.get("checkout").get("day_name")
#         checkout_month = specific_guest.get("checkout").get("month")
#         checkout_month_name = specific_guest.get("checkout").get("month_name")
#         checkout_year = specific_guest.get("checkout").get("year")
#
#         print(f"\nWhere is {first_name} staying?")
#
#         companies.get_companies()
#
#         choice = int(input("\nPlease select the corresponding company number:\n"))
#
#         company_info = companies.get_company_details(choice)
#         company_name = company_info.get('company_name')
#         company_city = company_info.get('company_city')
#         company_zone = company_info.get('city_timezone')
#
#         print(f"You selected {company_name}, located in {company_city}, {company_zone} time.\n")
#
#         message_type = int(input(f"Would you like to send a pre-existing message to {first_name}, or type your own?\n"
#                                  "1: Pre-Existing Message\n"
#                                  "2: Custom Message\n"))
#
#         if message_type == 1:
#             messages.get_message(specific_guest, company_info)
#         elif message_type == 2:
#             messages.custom_message(specific_guest, company_info)
import users
import guests
import messages
import companies


class Telegraph:
    # Greet user, accept name as input
    print(f"\nWelcome to Telegraph, {users.get_user().title()}.")

    # Get date data,
    current_day, current_month, current_year, current_date = users.get_current_date()
    print(f"Today is {current_day}, {current_month} {current_date}, {current_year}.")

    hour, minute, time_salutation, am_pm = users.get_current_time()
    print(f"The time is {hour}:{minute} {am_pm}.\n")

    # Ask which guest they need to contact
    def main_menu():
        print("Main Menu")
        print("---------")
        print("What can I help you with today?")

    def show_commands():  # Show command options
        print("\nCommands:\n"
              "1. Show Guests\n"
              "2. Contact Guest\n"
              "3. Exit\n")

    main_menu()
    while True:
        show_commands()
        try:
            selected_action = int(input())
        except ValueError:
            print("Invalid input. Please enter an integer.")
        while selected_action == 1 or 2:

            if selected_action == 1:
                # Show list of guests
                guests.show_guests()

            elif selected_action == 2:
                print("\nWhich guest would you like to contact?")
                guests.show_guests()
                choice = int(input("Please enter the corresponding room number:\n> "))

                # Select guest
                specific_guest = guests.select_guest(choice)

                # Guest variables
                first_name = specific_guest.get("first_name")
                last_name = specific_guest.get("last_name")
                room_number = specific_guest.get("room_number")

                # Check-In
                checkin_hour = specific_guest.get("checkin").get("time")
                checkin_day = specific_guest.get("checkin").get("day")
                checkin_day_name = specific_guest.get("checkin").get("day_name")
                checkin_month = specific_guest.get("checkin").get("month")
                checkin_month_name = specific_guest.get("checkin").get("month_name")
                checkin_year = specific_guest.get("checkin").get("year")

                # Check-Out
                checkout_hour = specific_guest.get("checkout").get("time")
                checkout_day = specific_guest.get("checkout").get("day")
                checkout_day_name = specific_guest.get("checkout").get("day_name")
                checkout_month = specific_guest.get("checkout").get("month")
                checkout_month_name = specific_guest.get("checkout").get("month_name")
                checkout_year = specific_guest.get("checkout").get("year")

                print(f"\nWhere is {first_name} staying?")
                companies.get_companies()

                choice = int(input("\nPlease select the corresponding company number:\n"))

                company_info = companies.get_company_details(choice)
                company_name = company_info.get('company_name')
                company_city = company_info.get('company_city')
                company_zone = company_info.get('city_timezone')
                print(f"You selected {company_name}, located in {company_city}, {company_zone} time.\n")

                message_type = int(
                    input(f"Would you like to send a pre-existing message to {first_name}, or type your own?\n"
                          "1: Pre-Existing Message\n"
                          "2: Custom Message\n"))
                if message_type == 1:
                    messages.get_message(specific_guest, company_info, time_salutation)
                elif message_type == 2:
                    messages.custom_message(specific_guest, company_info)
            break

        if selected_action == 3:
            print("Logging off.")
            break

