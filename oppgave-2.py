study_sessions = [
    {"topic": "Mathematics", "duration_minutes": 90, "status": "Planned"},
    {"topic": "English", "duration_minutes": 45, "status": "Planned"},
    {"topic": "Physics", "duration_minutes": 75, "status": "Completed"},
    {"topic": "Science", "duration_minutes": 90, "status": "Completed"},
    {"topic": "Arts", "duration_minutes": 45, "status": "Planned"},
]


def register_study_session():
    print("Register a new study session:")

    while True:
        topic = input("Topic: ").strip()
        if topic == "":
            print("Error: Please fill in the subject.")
        else:
            break

    while True:
        try:
            duration_minutes = int(input("Duration: "))
            if duration_minutes <= 0:
                print("Error: The duration must be a positive integer (greater than 0).")
            else:
                break
        except ValueError:
            print("Error: Please enter a valid number.")

    valid_status = ["Planned", "Completed"]
    while True:
        status = input("Status: ")

        if status in valid_status:
            break
        else:
            print("Error: Invalid status. You MUST enter either 'Planned' or 'Completed'.")

    new_study_session = {
        "topic": topic,
        "duration_minutes": duration_minutes,
        "status": status,
    }

    study_sessions.append(new_study_session)


def show_all_study_sessions():
    for sessions in study_sessions:
        print(sessions)


def show_finished_study_sessions():
    for status in study_sessions:
        if status.get("status") == "Completed":
            print(status)


def search_for_word():
    input_word = input("Search for word: ").casefold()
    match_found = False

    for content in study_sessions:
        if any(input_word in str(value).casefold() for value in content.values()):
            print(content)
            match_found = True

    if not match_found:
        print(f"No result matched your search for '{input_word}'. Please try again.")


def sort_sessions():
    sort_high_to_low = sorted(study_sessions, key=lambda i: i['duration_minutes'], reverse = True)
    print(sort_high_to_low)


def show_total_and_average():
    total_minutes_completed = 0
    average = 0
    completed_count = 0

    for total in study_sessions:
        if total.get("status") == "Completed":
            total_minutes_completed += total['duration_minutes']
    print(f"Total minutes studied: {total_minutes_completed}")

    for minutes in study_sessions:
        if minutes.get("status") == "Completed":
            average += minutes['duration_minutes']
            completed_count += 1

    if completed_count > 0:
        average_duration = average / completed_count
    else:
        average_duration = 0

    print(f"Average duration: {average_duration}")


def menu():
    while True:

        print("What would you like to do? Please enter a number between 1 and 7.")
        print("1. Register study session")
        print("2. Show all study sessions")
        print("3. Show only completed study sessions")
        print("4. Search for a word within the topic")
        print("5. Sort the sessions by duration, longest first")
        print("6. Show total and average duration for completed sessions")
        print("7. Exit the program")

        try:
            choice = int(input("Your choice: "))

            if choice == 1:
                register_study_session()
            elif choice == 2:
                show_all_study_sessions()
            elif choice == 3:
                show_finished_study_sessions()
            elif choice == 4:
                search_for_word()
            elif choice == 5:
                sort_sessions()
            elif choice == 6:
                show_total_and_average()
            elif choice == 7:
                print("Exiting program.")
                break
            else:
                print("Error: The number must be between 1 and 7.")

        except ValueError:
            print("Error: Please enter a valid integer (numbers only).")

menu()
