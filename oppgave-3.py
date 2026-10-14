from datetime import datetime, timedelta


def text_to_date(date):
    try:
        date_object = datetime.strptime(date, "%d.%m.%Y").date()
        return date_object
    except ValueError:
         return None

def get_end_time(start_time_str, minutes):
    try:
        start_time = datetime.strptime(start_time_str, "%H:%M")

        if minutes <= 0:
            return None

        stop_time = start_time + timedelta(minutes=minutes)
        return stop_time.strftime("%H:%M")
    except ValueError:
        return None

def days_between():
    print()

def sort_dates():
    print()


def main():
