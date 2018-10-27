"""
  List:
  - a collection which is ordered and changeable
  - written with square brackets
"""

# creating lists

fruits = ['apples', 'oranges', 'bananas']

r = range(1, 11)
l = list(r)
print(l)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# list length

print(len(fruits))  # 3

# accessing items

print(fruits[0])  # 'apples'
print(fruits[1])  # 'oranges'
print(fruits[2])  # 'bananas'

print(fruits[-1])  # 'bananas'
print(fruits[-2])  # 'oranges'
print(fruits[-3])  # 'apples'

# checking if item exists

print('apples' in fruits)  # True
print('watermelons' in fruits)  # False

# looping through a list

for fruit in fruits:
    print(fruit)

i = 0
while i < len(fruits):
    print(f"{i}: {fruits[i]}")
    i += 1
