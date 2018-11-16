# iterable - any object that can return an iterator, when iter() is called on it (e.g. str, list)
# iterator - a stateful helper object that will produce the next value when you call next() on it

x = [1, 2, 3]

# x.next()  # AttributeError: 'list' object has no attribute 'next'

it = iter(x)

print(it)  # <list_iterator object at 0x00C4AE30>

print(next(it))  # 1
print(next(it))  # 2
print(next(it))  # 3

# custom for loop


def my_for_loop(iterable, func):
    iterator = iter(iterable)
    while True:
        try:
            i = next(iterator)
        except StopIteration:
            break
        else:
            func(i)


my_for_loop("Hello", print)


def square(x):
    print(x ** 2)


my_for_loop([1, 2, 3], square)
