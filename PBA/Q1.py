import json
import csv

with open("students.json", "r") as f:
    data = json.load(f)

with open("students.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=data[0].keys())
    writer.writeheader()
    writer.writerows(data)

print("JSON converted to CSV successfully!")
