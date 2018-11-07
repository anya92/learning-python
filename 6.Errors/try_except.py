# raising errors


def concat(s, num):
    if type(s) is not str:
        raise TypeError("first argument must be a string")
    if type(num) is not int:
        raise TypeError("second argument must be an integer")
    return s + ' ' + str(num)


# print(concat(7, 13))  # TypeError: first argument must be a string
# print(concat('hello', '13'))  # TypeError: second argument must be an integer
print(concat('hello', 13))  # hello 13

# handling errors - try except

try:
    print(x)  # 'x' is not defined
except:
    print("An exception occurred")

# An exception occurred


def get_key(d, key):
    try:
        return d[key]
    except KeyError:
        return None


d = {'name': 'James'}

print(get_key(d, 'name'))  # 'James'
print(get_key(d, 'age'))  # None


# else - to define a block of code to be executed if no errors were raised
# finally - to execute code, regardless of the result of the try- and except blocks

def divide(a, b):
    try:
        result = a / b
    except (ZeroDivisionError, TypeError) as error:
        print('Something went wrong.')
        print(error)
    else:
        print(f"{a} divided by {b} is {result}")
    finally:
        print("The 'try except' is finished")


divide(2, 0)
# Something went wrong.
# division by zero
# The 'try except' is finished

divide('a', 2)
# Something went wrong.
# unsupported operand type(s) for /: 'str' and 'int'
# The 'try except' is finished

divide(1, 2)
# 1 divided by 2 is 0.5
# The 'try except' is finished
