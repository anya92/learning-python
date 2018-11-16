# generator function - allow you to declare a function that behaves like an iterator:
# - contains one or more yield statement
# - __iter__() and __next__() methoods are implemented automatically
# - once the function yields, the function is paused and the control is transferred to the caller
# - local variables and their states are remembered between successive calls
# - when the function terminates, StopIteration is raised automatically on further calls


def count_up_to(max):
    count = 1
    while count <= max:
        yield count
        count += 1


counter = count_up_to(5)
print(counter)  # <generator object count_up_to at 0x00238F70>

print(next(counter))  # 1
print(next(counter))  # 2
print(next(counter))  # 3
print(next(counter))  # 4
print(next(counter))  # 5
