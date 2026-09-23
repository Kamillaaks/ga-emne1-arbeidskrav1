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