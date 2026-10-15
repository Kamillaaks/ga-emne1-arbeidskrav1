import csv

# Task 4.1 - read and validate CSV data
valid_requests = []

with open("supporthenvendelser.csv", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row_number, row in enumerate(reader, start=2):
        if not row["id"]:
            print(f"Error on row {row_number}: Missing ID.")
            continue
        try:
            row["id"] = int(row["id"])
            if row["id"] <= 0:
                print(f"Error on row {row_number}: ID must be greater than zero.")
                continue
        except ValueError:
            print(f"Error on row {row_number}: ID must be an integer.")
            continue

        if not row["minutes"]:
            print(f"Error on row {row_number}: Missing minutes.")
            continue
        try:
            row["minutes"] = int(row["minutes"])
            if row["minutes"] < 0:
                print(f"Error on row {row_number}: Minutes cannot be negative")
                continue
        except ValueError:
            print(f"Error on row {row_number}: Minutes must be an integer.")
            continue

        if not row["category"]:
            print(f"Error on row {row_number}: Missing category.")
            continue

        if row["is_resolved"] not in ("yes", "no"):
            print(f"Error on row {row_number}: is_resolved must be yes or no.")
            continue

        valid_requests.append(row)

