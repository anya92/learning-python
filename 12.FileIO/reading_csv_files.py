from csv import reader, DictReader

# reader

with open('countries.csv') as file:
    csv_data = reader(file)  # iterator (next())
    print(csv_data)  # <_csv.reader object at 0x002A8D70>
    for row in csv_data:
        print(row)  # each row is a list
        # ['country', 'latitude', 'longitude', 'name']
        # ['AD', '42.546245', '1.601554', 'Andorra'] ...

# DictReader

with open('countries.csv') as file:
    csv_data = DictReader(file)  # iterator (next())
    print(csv_data)  # <_csv.reader object at 0x002A8D70>
    for row in csv_data:
        # print(row)  # each row is an OrderedDict object
        # OrderedDict([('country', 'AD'), ('latitude', '42.546245'), ('longitude', '1.601554'), ('name', 'Andorra')])
        print(row['name'])
        # Andorra
        # United Arab Emirates
