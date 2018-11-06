# SyntaxError - arises when the Python parser is unable to understand a line of code


def func  # SyntaxError: invalid syntax


None = 2  # SyntaxError: can't assign to keyword

return  # SyntaxError: 'return' outside function


# NameError - arises when a local or global name is not found

print(person)  # NameError: name 'person' is not defined


# TypeError - arises when an operation or function is applied to an object of inappropriate type

len(14)  # TypeError: object of type 'int' has no len()

print("Hello" + 12)  # TypeError: can only concatenate str (not "int") to str


# IndexError - arises when a sequence subscript is out of range

print([1, 2, 3][5])  # IndexError: list index out of range

(3, 5)[-4]  # IndexError: tuple index out of range


# ValueError - arises when an operation or function receives an argument that has the right type but an inappropriate value

int('eleven')  # ValueError: invalid literal for int() with base 10: 'eleven'


# KeyError - arises when a dictionary key is not found in the set of existing keys

dictionary = {}
print(dictionary['name'])  # KeyError: 'name'


# AttributeError - arises when an attribute reference or assignment fails

"hello".say()  # AttributeError: 'str' object has no attribute 'say'
