import requests
import csv
URL = "http://127.0.0.1:8000/items"
insertions = 0

with open("MOCK_DATA(1).csv") as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        response = requests.post(URL, json=row)
        if response.status_code == 200:
            insertions += 1
        else:
            print(row, response.status_code)

print(f"Total insertions: {insertions}")