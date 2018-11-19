from functools import wraps


def ensure_first_arg_is(val):
    def inner(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            if args and args[0] != val:
                return f"First argument must be {val}"
            return fn(*args, **kwargs)
        return wrapper
    return inner


@ensure_first_arg_is(2)
def add_to_two(num1, num2):
    return num1 + num2


print(add_to_two(2, 5))  # 7
print(add_to_two(3, 5))  # 'First argument must be 2'


def enforce_types(*types):
    def inner(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            new_args = []
            for (arg, t) in zip(args, types):
                new_args.append(t(arg))
            return fn(*new_args, **kwargs)
        return wrapper
    return inner


@enforce_types(str, int)
def repeat_msg(msg, times):
    for _ in range(times):
        print(msg)


repeat_msg("Hello, world!", 3)
# Hello, world!
# Hello, world!
# Hello, world!

repeat_msg("Decorators!!!", '2')
# w/o @enforce_types -> TypeError: 'str' object cannot be interpreted as an integer

# Decorators!!!
# Decorators!!!
