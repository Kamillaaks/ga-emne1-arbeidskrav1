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


def sort_dates(date_list):
    for date in date_list:
        if text_to_date(date) is None:
            return None

    return sorted(date_list, key=text_to_date)


handle_date_input()