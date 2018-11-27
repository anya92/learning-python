import doctest

# doctest is a test framework that comes prepackaged with Python


def multiply(a, b):
    """
    Multiplies two numbers
    >>> multiply(1, 3)
    3
    >>> multiply(-2, 4)
    -8
    """

    return a + b


if __name__ == "__main__":
    doctest.testmod()

# **********************************************************************
# File "doctests.py", line 9, in __main__.multiply
# Failed example:
#     multiply(1, 3)
# Expected:
#     3
# Got:
#     4
# **********************************************************************
# File "doctests.py", line 11, in __main__.multiply
# Failed example:
#     multiply(-2, 4)
# Expected:
#     -8
# Got:
#     2
# **********************************************************************
# 1 items had failures:
#    2 of   2 in __main__.multiply
# ***Test Failed*** 2 failures.


# or in console: > py -m doctest -v doctests.py
