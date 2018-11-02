name = "Jenny"  # global variable


def say_name():
    print(f"Hello, {name}")


say_name()  # "Hello, Jenny"
print(name)  # "Jenny"


def say_full_name():
    last_name = "Smith"  # local variable
    print(f"Hello, {name} {last_name}")


say_full_name()  # "Hello, Jenny Smith"
# print(last_name)  # NameError: name 'last_name' is not defined

total = 0


def print_total():
    print(total)


print_total()  # 0


def increment():
    total += 1
    print(total)

# increment()  # UnboundLocalError: local variable 'total' referenced before assignment


def increment_with_global():
    global total
    total += 1
    print(total)


increment_with_global()  # 1


def outer():
    total = 20

    def inner():
        total += 1
        return total
    return inner()


# outer()  # UnboundLocalError: local variable 'total' referenced before assignment


def outer_with_nonlocal():
    total = 20

    def inner():
        nonlocal total
        total += 1
        return total

    return inner()


print(outer_with_nonlocal())  # 21
