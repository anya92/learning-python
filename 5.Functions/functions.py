"""
  Function:
  - a block of code which only runs when it is called.
"""

# defining a function


def name_of_function():
    print("This is a function.")

# calling a function


name_of_function()  # "This is a function."

# returning values


def square_of_nine():
    return 9 ** 2


print(square_of_nine())  # 81

# parameters


def say_hello(name):  # name is a parameter
    print(f"Hello, {name}!")


say_hello("Jenny")  # "Hello, Jenny!", 'Jenny' is an argument


def add(a, b):
    return a + b


print(add(2, 3))  # 5

# default parameters


def square(num, power=2):
    return num ** power


print(square(5, 3))  # 125
print(square(9))  # 81


# keyword (named) arguments

def full_name(first, last):
    print(f"Hello, my name is {first} {last}")


full_name("Tom", "Smith")  # "Hello, my name is Tom Smith"
full_name("Smith", "Tom")  # "Hello, my name is Smith Tom"

full_name(last="Smith", first="Tom")  # "Hello, my name is Tom Smith"
