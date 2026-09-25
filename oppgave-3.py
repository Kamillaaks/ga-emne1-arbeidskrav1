from datetime import  datetime



def text_to_date():
    while True:
        get_date = input("Enter your date (dd.mm.yyyy): ")
        try:
            date_object = datetime.strptime(get_date, "%d.%m.%Y").date()
            return date_object
        except ValueError:
            print("Invalid date. Please try again.")


def get_end_time():
    print()

def days_between():
    print()

def sort_dates():
    print()

