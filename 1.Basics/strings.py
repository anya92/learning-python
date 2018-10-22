# Strings:
# are surrounded by either single quotation marks, or double quotation marks  'hello' is the same as "hello"

x = 'hello' # or
y = "hello"

# Indicies
x = 'hello'
x[0] # 'h'
x[1:3] # 'el'
x[-1] # 'o'
x[-5] # 'h'

# Formatting Strings
# Python 3.6+ 
age = 26
print(f"I'm {age} years old")

# Python 2 -> Python 3.5
print("I'm {} years old".format(age))

# String Methods

# string length
len('hello') # 5

# strip - removing whitespaces from the beggining and the end
' hello '.strip() # 'hello'

# lower and upper case
'hello'.upper() # 'HELLO'
'Hello'.lower() # 'hello'

# replace - replacing a string with another string
'hello'.replace('h', 'z') # 'zello

# split - splitting the string into substrings based of the separator
'hello, world'.split(',')  # ['hello', ' world']
