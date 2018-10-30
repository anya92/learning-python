"""
  Tuples:
  - collections which are ordered and unchangeable
  - are written with round brackets
"""

# creating tuples

coordinates = (3, 5)  # or
alphabet = tuple(('A', 'B', 'C', 'D'))

print(type(coordinates))  # <class 'tuple'>
print(coordinates[0])  # 3
print(5 in coordinates)  # True

# coordinates[0] = 4 -> TypeError: 'tuple' object does not support item assignment

# tuples are commonly used for unchanging data

days = ('Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday', 'Saturday', 'Sunday')

print(days[0])  # 'Monday'
print(days[-1])  # 'Sunday'

# tuples can be used as keys in dictionaries

locations = {
    (51.5098, -0.1180): 'London',
    (52.3702,	4.8951): 'Amsterdam',
    (59.9114,	10.7579): 'Oslo'
}

print(locations[(52.3702,	4.8951)])  # 'Amsterdam

# some dictionary methods return a list of tuples, e.g. items()

d = {'name': 'Jerry', 'age': 1, 'friend': 'Tom'}

print(d.items())
# dict_items([('name', 'Jerry'), ('age', 1), ('friend', 'Tom')])

# looping through a tuple

for day in days:
    print(day)

i = len(days) - 1
while i >= 0:
    print(days[i])
    i -= 1
