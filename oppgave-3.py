from datetime import datetime, timedelta


def text_to_date(date):
    try:
        date_object = datetime.strptime(date, "%d.%m.%Y").date()
        return date_object
    except ValueError:
        return None


def handle_date_input():
    while True:
        input_date = input("Please enter a date (dd.mm.yyyy): ")
        parsed_date = text_to_date(input_date)

        if parsed_date is None:
            print("Error: The date entered is invalid.")
        else:
            print(f"Valid date: {parsed_date}")
            break


def get_end_time(start_time_str, minutes):
    try:
        start_time = datetime.strptime(start_time_str, "%H:%M")

        if minutes <= 0:
            return None

        stop_time = start_time + timedelta(minutes=minutes)
        return stop_time.strftime("%H:%M")
    except ValueError:
        return None


def handle_end_time():
    while True:
        start_time = input("Please enter start time (hh:mm): ")

        try:
            duration_minutes = int(input("Enter duration in minutes: "))

            if duration_minutes <= 0:
                print("Error: Please enter a positive number.")
                continue

            end_time = get_end_time(start_time, duration_minutes)
            if end_time is None:
                print("Error: Invalid start time. Please use hh:mm format.")
            else:
                print(f"Valid end time: {end_time}")
                break
        except ValueError:
            print("Error: The duration entered is invalid.")


def days_between(date1, date2):
    if not date1 or not date2:
        return None

    date_format = "%d.%m.%Y"

    try:
        parsed_date1 = datetime.strptime(date1, date_format)
        parsed_date2 = datetime.strptime(date2, date_format)

        return abs(parsed_date2 - parsed_date1).days

    except ValueError:
        return None


def handle_days_between():
    while True:
        first_date = input("Please enter first date (dd.mm.yyyy): ")
        second_date = input("Please enter second date (dd.mm.yyyy): ")

        days = days_between(first_date, second_date)

        if days is None:
            print("Error: The date entered is invalid.")
        else:
            print(f"Days between dates: {days}")
            break


def sort_dates(date_list):
    for date in date_list:
        if text_to_date(date) is None:
            return None

    return sorted(date_list, key=text_to_date)


def handle_date_sorting():
    date_list = []
    print("Please enter a date (dd.mm.yyyy): ")
    print("When you are done entering your dates, please enter 'Done' to quit.")
    while True:
        dates = input("Date: ")

        if dates.lower() == "done":
            if not date_list:
                print("Error: Please enter at least one date.")
                continue
            break

        check_dates = text_to_date(dates)
        if check_dates is None:
            print("Error: The date entered is invalid.")
            continue

        date_list.append(dates)

    finished_list = sort_dates(date_list)

    print(f"List of dates {finished_list}")


def menu():
    while True:
        print("What would you like to do?")
        print("1. Validate a date")
        print("2. Calculate end time")
        print("3. Calculate days between dates")
        print("4. Sort dates chronologically")
        print("5. Exit")

        try:
            choice = int(input("Your choice: "))

            if choice == 1:
                handle_date_input()
            elif choice == 2:
                handle_end_time()
            elif choice == 3:
                handle_days_between()
            elif choice == 4:
                handle_date_sorting()
            elif choice == 5:
                print("Goodbye!")
                break
            else:
                print("Error: The number must be between 1 and 5.")
        except ValueError:
            print("Error: Please enter a valid integer (numbers only).")


menu()
