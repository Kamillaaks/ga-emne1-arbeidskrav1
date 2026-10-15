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


 # Task 4.2 - Analyze valid requests

total_requests = len(valid_requests)
category_counts = {}

for request in valid_requests:
    category = request["category"]
    if category in category_counts:
        category_counts[category] += 1
    else:
        category_counts[category] = 1

total_minutes = 0

for request in valid_requests:
    total_minutes += request["minutes"]

average_time_spent = total_minutes / total_requests

resolved_count = 0
unresolved_count = 0

for request in valid_requests:
    if request["is_resolved"] == "yes":
        resolved_count += 1
    else:
        unresolved_count += 1

most_common_category = max(category_counts.items(), key=lambda item: item[1])


unresolved_requests = []
for request in valid_requests:
    if request["is_resolved"] == "no":
        unresolved_requests.append(request)

sorted_requests = sorted(unresolved_requests, key=lambda item: item["minutes"], reverse=True)


# Task 4.3 -

with open("support-rapport.txt", "w", encoding="utf-8") as file:
    file.write("Support Report\n")
    file.write(f"Total requests: {total_requests}\n")
    file.write(f"Number of requests per category: \n")
    for category, count in category_counts.items():
        file.write(f"{category}: {count}\n")
    file.write(f"Total minutes used: {total_minutes}\n")
    file.write(f"Average time spent per request: {average_time_spent:.1f}\n")
    file.write(f"Resolved requests: {resolved_count}\n")
    file.write(f"Unresolved requests: {unresolved_count}\n")
    file.write(f"Most common category: {most_common_category[0]} ({most_common_category[1]} requests)\n")
    file.write("Unresolved requests, sorted by time used:\n")
    for request in sorted_requests:
        file.write(f"ID: {request["id"]} - Category: {request["category"]} - Minutes: {request["minutes"]}\n")