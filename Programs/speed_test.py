import time
from functools import wraps


def speed_test(fn):
    @wraps(fn)  # Without the use of this decorator factory, the name of the inner function would have been 'wrapper', and the docstring of the original inner function would have been lost
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = fn(*args, **kwargs)
        end_time = time.time()
        print(f"Executing: {fn.__name__}")
        print(f"Time Elapsed: {end_time - start_time}")
        return result
    return wrapper


@speed_test
def sum_nums_gen():
    return sum(x for x in range(50000000))


@speed_test
def sum_nums_list():
    return sum([x for x in range(50000000)])


print(sum_nums_gen())
print(sum_nums_list())
