# Oppgave 1.1

def write_error_msg(message):
    while True:
        try:
            message_from_user = int(input(message))

            if message_from_user > 0:
                return message_from_user
            else:
                print("Vennligst skriv inn et positivt heltall.")

        except ValueError:
            print("Vennligst skriv inn et positivt heltall.")


def calculate_hours(sessions, minutes):
    total_minutes = sessions * minutes

    hours = total_minutes // 60
    rest_minutes = total_minutes % 60

    print(f"Du har studert i {hours} timer og {rest_minutes} minutter.")


def process_time():
    study_sessions = write_error_msg("Antall studieøkter: ")
    minutes_per_session = write_error_msg("Antall minutter brukt per økt: ")

    calculate_hours(study_sessions, minutes_per_session)


#Oppgave 1.2

def check_errors(input_string):
    while True:
        message = input(input_string)

        if message.strip():
            return message
        else:
            print("Du kan ikke sende inn en tom tekst eller bare mellomrom. Vennligst skriv inn din tekst.")


def count_spaces(text):
    space_count = 0

    for spaces in text:
        if spaces == " ":
            space_count +=1

    print(f"Antall mellomrom: {space_count}")


def count_letters(text):
    letter_count = 0

    alphabet =[
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
            'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'æ',
            'ø', 'å'
        ]

    for letters in text:
        if letters in alphabet:
            letter_count += 1

    print(f"Antall bokstaver: {letter_count}")


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
        print("Teksten din inneholder ordet 'Python'")
    elif "python" in string:
        print("Teksten din inneholder ordet 'Python'")
    else:
        print("Teksten din inneholder ikke ordet 'Python'")


def process_text():
    user_text = check_errors("Skriv inn din tekst for analyse: ")
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
                print("Vennligst skriv inn et positivt heltall.")
        except ValueError:
            print("Vennligst skriv inn et positivt heltall.")


def get_valid_interval():
    while True:
        start = error_check("Skriv inn det første tallet: ")
        end = error_check("Skriv inn det andre tallet: ")

        if start <= end:
            return start, end

        print("Feil: Det første tallet kan ikke være større enn det andre tallet. ")


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
    print("Skriv inn et tallintervall!")

    start, end = get_valid_interval()

    check_if_even(start, end)
    divide_by_three(start, end)
    sum_of_interval(start, end)

