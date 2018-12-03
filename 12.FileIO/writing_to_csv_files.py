# using lists

from csv import reader, writer, DictReader, DictWriter

with open("people.csv", "w") as file:
    csv_writer = writer(file)
    csv_writer.writerow(["first name", "last name", "age"])
    csv_writer.writerow(["Tom", "Smith", 34])
    csv_writer.writerow(["Jenny", "Olsen", 28])

with open("countries.csv") as file:
    csv_reader = reader(file)
    with open("country_codes.csv", "w") as file:
        csv_writer = writer(file)
        for row in csv_reader:
            csv_writer.writerow([row[3], row[0]])

# using DictWriter

with open("animals.csv", "w") as file:
    headers = ["Name", "Type", "Age"]
    csv_writer = DictWriter(file, fieldnames=headers)
    csv_writer.writeheader()
    csv_writer.writerow({
        "Name": "Mr Puppy",
        "Type": "Dog",
        "Age": 2
    })

with open("countries.csv") as file:
    csv_reader = DictReader(file)
    with open("country_coords.csv", "w") as file:
        headers = ["Country Name", "Lat", "Lon"]
        csv_writer = DictWriter(file, fieldnames=headers)
        csv_writer.writeheader()
        for row in csv_reader:
            csv_writer.writerow({
                "Country Name": row["country"],
                "Lat": row["latitude"],
                "Lon": row["longitude"]
            })
