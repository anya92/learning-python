# https://docs.python.org/3/py-modindex.html

# random - to generate pseudo-random numbers with various common distributions

from string import ascii_lowercase as lowercase
import random

print(random.choice(['red', 'blue', 'green', 'purple', 'yellow']))

numbers = [1, 4, 3, 2, 6]
random.shuffle(numbers)

print(numbers)  # e.g. [3, 1, 4, 6, 2]


# string - common string operations

print(lowercase)  # abcdefghijklmnopqrstuvwxyz

print("int: {0:d}, bin: {0:b}, hex: {0:x}".format(255))
# int: 255, bin: 11111111, hex: ff
