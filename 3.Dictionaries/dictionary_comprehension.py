# Dictionary comprehension is a method for transforming one dictionary into another dictionary.

# [ key:value expression() for key, value in list]

person = {
    'first_name': 'ted',
    'second_name': 'thomas',
    'city': 'london'
}

print({k: v.capitalize() for k, v in person.items()})
# {'first_name': 'Ted', 'second_name': 'Thomas', 'city': 'London'}

fruits = ['apple', 'banana', 'kiwi', 'orange', 'watermelon']

print({k: len(k) for k in fruits})
# {'apple': 5, 'banana': 6, 'kiwi': 4, 'orange': 6, 'watermelon': 10}

print({code: chr(code) for code in range(97, 123)})

# {97: 'a', 98: 'b', 99: 'c', 100: 'd', 101: 'e', 102: 'f', 103: 'g', 104: 'h', 105: 'i', 106: 'j', 107: 'k', 108: 'l', 109: 'm', 110:
# 'n', 111: 'o', 112: 'p', 113: 'q', 114: 'r', 115: 's', 116: 't', 117: 'u', 118: 'v', 119: 'w', 120: 'x', 121: 'y', 122: 'z'}

# dictionary comprehension with Conditional Logic

print({num: ('even' if num % 2 == 0 else 'odd') for num in range(1, 11)})
# {1: 'odd', 2: 'even', 3: 'odd', 4: 'even', 5: 'odd', 6: 'even', 7: 'odd', 8: 'even', 9: 'odd', 10: 'even'}
