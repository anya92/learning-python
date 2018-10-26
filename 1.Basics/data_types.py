"""
  Data types:
    - strings (str) - sequences of unicode characters, surrounded by either single quotation marks, or double quotation marks, e.g. 'Hello'.
    - numbers:
      - integers (int) - whole numbers, positive or negative, without decimals, e.g. 2, -10
      - floats (float) - numbers, positive or negative, containing one or more decimals, e.g. 0.5, -13.43
    - booleans (bool) - may have one of two values, True or False
    - lists (list) - collections which are ordered and changeable,  written with square brackets, e.g. [1, 2, 3],
    - dictionaries (dict) - collections of key-values pairs, written with curly brackets, e.g. { "first_name": "Andy", "age": 28 }
    - tuples (tuple) - collections which are ordered and unchangeable, written with round brackets, e.g. ("red", "black", "blue")
    - sets (set) - collections which are unordered and unindexed, written with curly brackets, e.g. { "Tokyo", "Berlin", "Dallas" }
"""

# Python is dynamically typed - the type is associated with run-time values and not named variables.
# Python is highly flexible about reassigning variables to different types.

x = 'hello'
type(x)  # <class 'str'>
x = 13
type(x)  # <class 'int'>
x = True
type(x)  # <class 'bool'>
x = ['a', 'b', 'c']
type(x)  # <class 'list'>
x = None
type(x)  # <class 'NoneType'> -> used to represent the absence of a value

# Types conversion
int(3.74)  # 3
int('ff', 16)  # 255
float(12)  # 12.0
str(-12)  # '-12'
str([1, 2, 3])  # '[1, 2, 3]'
list('abcd')  # ['a', 'b', 'c', 'd']
