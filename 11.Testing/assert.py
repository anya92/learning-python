# assert statement has a condition or expression which is supposed to be always true. If the condition is false assert halts the program and gives an AssertionError

# assert <condition>
# assert <condition>,<error message>


def add_two_positive_numbers(x, y):
    assert x > 0 and y > 0, "Both numbers must be positive"
    return x + y


# print(add_two_positive_numbers(-2, 3))
# AssertionError: Both numbers must be positive

print(add_two_positive_numbers(2, 3))  # 5

# if a Python file is run with the -O flag, assertions will not be evaluated
# > python -O assert.py
# print(add_two_positive_numbers(-2, 3)) -> 1


def avg(marks):
    assert len(marks) > 0, "List is empty."
    return sum(marks) / len(marks)


marks = []
# print(avg(marks))  # AssertionError: List is empty.

marks = [56, 78, 91, 84]
print(avg(marks))  # 77.25
