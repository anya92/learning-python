# Dictionaries:
# - collections which are unordered, changeable and indexed
# - are written with curly brackets, and they have keys and values.

# creating dictionaries

person = {
    'name': 'Tom',
    'age': 31,
    'have_cats': False
}
print(person)  # {'name': 'Tom', 'age': 31, 'have_cats': False}

person2 = dict(name='Jenny', age=28, have_cats=True)
print(person2)  # {'name': 'Jenny', 'age': 28, 'have_cats': True}

# accessing data

print(person['name'])  # 'Tom'
print(person2['age'])  # 28

print(person.get('age'))  # 31
print(person2.get('have_cats'))  # True

# looping through a dictionary

# values

for val in person.values():
    print(val)  # 'Tom', 31, False

# keys

for key in person2.keys():
    print(key)  # 'name', 'age', 'have_cats'

# both keys and values - items

print(person.items())
# dict_items([('name', 'Tom'), ('age', 31), ('have_cats', False)]) -> list of tuples

for key, value in person.items():
    print(key, value)
    # name Tom
    # age 31
    # have_cats False

# checking if key exists

print('name' in person)  # True
print('have_dogs' in person2)  # False

# value

print('Tom' in person.values())  # True
