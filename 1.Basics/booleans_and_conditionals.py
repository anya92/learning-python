# Boolean values

type(True)  # 'bool'
type(False)  # 'bool'

# falsy values: None, False, 0 (int/float), "", {}, [], ()

# Conditional statements

"""
  if BOOLEAN_EXPRESSION:
    STATEMENT_1
  elif BOOLEAN_EXPRESSION:
    STATEMENT_2
  else:
    STATEMENT_3  
"""

# Comparison operators

a = 10
b = 12

a == b  # False
a != b  # True
a > b  # False
a < b  # True
a >= b  # False
a <= b  # True
"a" == "A"  # False
"a" < "A"  # False
"b" > "a"  # True

# is vs '=='

x = 3
y = 3
x == y  # True
x is y  # True

x = [1, 2, 3]
y = [1, 2, 3]
x == y  # True -> '==' compares the values of both the operands and checks for value equality
x is y  # False -> 'is' checks whether both the operands refer to the same object in memory or not
x = y
x is y  # True

# Logical Operators
x = True
y = False

# and - True if both x and y are True, False otherwise
x and y  # False

# or - True if either x or y is True, False otherwise
x or y  # True

# not - True if x is False, False if x is True
not x  # False
not y  # True
