# using lists

from csv import reader, writer

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
