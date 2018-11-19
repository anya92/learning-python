# decorators wrap a function, modifying its behavior


def my_decorator(fn):
    def wrapper():
        print("Before the function is called.")
        fn()
        print("After the function is called.")
    return wrapper


def say_hello():
    print("Hello!")


print(say_hello)  # <function say_hello at 0x00D1D4B0>

say_hello = my_decorator(say_hello)

print(say_hello)  # <function my_decorator.<locals>.wrapper at 0x00DBD4F8>

say_hello()
# Before the function is called.
# Hello!
# After the function is called.

# with the @ symbol


@my_decorator
def say_goodbye():
    print("Goodbye!")


print(say_goodbye)  # <function my_decorator.<locals>.wrapper at 0x0095D588>

say_goodbye()
# Before the function is called.
# Goodbye!
# After the function is called.

# decorators with multiple arguments -> use *args and **kwargs in the inner wrapper function


def my_decor(fn):
    def wrapper(name):
        return fn(name).upper()
    return wrapper


@my_decor
def hello(name):
    return f"Hello, {name}."


print(hello("world"))  # HELLO, WORLD.


@my_decor
def full_name(first, last):
    return f"My name is {first} {last}."


# print(full_name("Stephen", "King"))
# TypeError: wrapper() takes 1 positional argument but 2 were given


def my_decor_2(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, ** kwargs).upper()
    return wrapper


@my_decor_2
def full_name_2(first, last):
    return f"My name is {first} {last}."


print(full_name_2("Stephen", "King"))  # MY NAME IS STEPHEN KING.
