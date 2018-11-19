import time
from functools import wraps


def speed_test(fn):
    @wraps(fn)  # Without the use of this decorator factory, the name of the inner function would have been 'wrapper', and the docstring of the original inner function would have been lost
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = fn(*args, **kwargs)
        end_time = time.time()
        print(
            f"Finished {fn.__name__!r} in {(end_time - start_time):.4f}s")
        return result
    return wrapper


@speed_test
def sum_nums_gen():
    return sum(x for x in range(10000000))


@speed_test
def sum_nums_list():
    return sum([x for x in range(10000000)])


print(sum_nums_gen())
# Finished 'sum_nums_gen' in 1.9080s
# 49999995000000

print(sum_nums_list())
# Finished 'sum_nums_list' in 2.4441s
# 49999995000000
