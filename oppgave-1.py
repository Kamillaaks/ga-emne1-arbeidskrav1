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
