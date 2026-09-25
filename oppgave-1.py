# Oppgave 1.1

def write_error_msg(message):
    while True:
        try:
            message_from_user = int(input(message))

            if message_from_user > 0:
                return message_from_user
            else:
                print("Please enter a positive integer.")

        except ValueError:
            print("Please enter a positive integer.")


def calculate_hours(sessions, minutes):
    total_minutes = sessions * minutes

    hours = total_minutes // 60
    rest_minutes = total_minutes % 60

    print(f"You have studied for {hours} hours and {rest_minutes} minutes.")


def process_time():
    study_sessions = write_error_msg("Number of study sessions: ")
    minutes_per_session = write_error_msg("Number of minutes spent per session: ")

    calculate_hours(study_sessions, minutes_per_session)


#Oppgave 1.2

def check_errors(input_string):
    while True:
        message = input(input_string)

        if message.strip():
            return message
        else:
            print("You cannot submit empty text or just spaces. Please enter your text.")


def count_spaces(text):
    space_count = 0

    for spaces in text:
        if spaces == " ":
            space_count +=1

    print(f"Number of spaces: {space_count}")


def count_letters(text):
    letter_count = 0
    text = text.casefold()

    alphabet =[
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
            'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
        ]

    for letters in text:
        if letters in alphabet:
            letter_count += 1

    print(f"Number of letters: {letter_count}")


def write_lowercase(text):
    lowercase = text.lower()
    print(lowercase)


def write_backwards(text):
    backwards = text

    for backwards in reversed(backwards):
        print(backwards)


def check_for_python(text):
    string = text
    if "Python" in string:
        print("Your text contains the word 'Python'")
    elif "python" in string:
        print("Your text contains the word 'Python'")
    else:
        print("Your text does not contain the word 'Python'")


def process_text():
    user_text = check_errors("Enter your text for analysis: ")
    count_letters(user_text)
    count_spaces(user_text)
    write_lowercase(user_text)
    write_backwards(user_text)
    check_for_python(user_text)

# Oppgave 1.3

def error_check(message):
    while True:
        try:
            user_input = int(input(message))

            if user_input > 0:
                return user_input
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Please enter a positive integer.")


def get_valid_interval():
    while True:
        start = error_check("Enter the first number: ")
        end = error_check("Enter the second number: ")

        if start <= end:
            return start, end

        print("Error: The first number cannot be greater than the second number.")


def check_if_even(start, end):
    even_numbers = 0

    for num in range(start, end + 1):
        if num % 2 == 0:
            even_numbers += 1

    print(even_numbers)


def divide_by_three(start, end):
    divisible_by_three = 0

    for num in range(start, end + 1):
        if num % 3 == 0:
            divisible_by_three += 1

    print(divisible_by_three)


def sum_of_interval(start, end):
    total_sum = 0

    for num in range(start, end + 1):
        total_sum += num

    print(total_sum)


def process_numbers():
    print("Enter a number range!")

    start, end = get_valid_interval()

    check_if_even(start, end)
    divide_by_three(start, end)
    sum_of_interval(start, end)

# Oppgave 1.4

def menu():
    while True:
        print("Estimate the time required")
        print("Analyze text")
        print("Analyze numerical intervals")
        print("4. Exit")

        try:
            choice = int(input("Your choice: "))

            if choice == 1:
                process_time()
            elif choice == 2:
                process_text()
            elif choice == 3:
                process_numbers()
            elif choice == 4:
                print("Ending the program. Have a nice day!")
                break
            else:
                print("Invalid choice. Please select a number between 1 and 4.")

        except ValueError:
            print("Error: You must enter an integer between 1 and 4.")
menu()