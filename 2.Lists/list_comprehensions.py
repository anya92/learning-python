# List comprehensions provide a concise way to create lists.

# [ expression() for item in old_list ]

data = [1, 2, 3, 4, 5]

new_data = [x ** 2 for x in data]
print(new_data)  # [1, 4, 9, 16, 25]

# examples:

print([letter.upper() for letter in 'Bob'])  # ['B', 'O', 'B']

print([x for x in range(10)])  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print([bool(val) for val in [0, '', []]])  # [False, False, False]


# List comprehensions with Conditional Logic

# [ expression() for item in old_list if conditional ]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

evens = [num for num in numbers if num % 2 == 0]
odds = [num for num in numbers if num % 2 != 0]

print(evens)  # [2, 4, 6, 8, 10]
print(odds)  # [1, 3, 5, 7, 9]

print([num ** 2 if num % 2 == 0 else num / 2 for num in numbers])
# [0.5, 4, 1.5, 16, 2.5, 36, 3.5, 64, 4.5, 100]
