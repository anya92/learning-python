def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def is_prime(num):
    if num in (0, 1):
        return False

    if num < 0:
        return False

    for n in range(2, num):
        if num % n == 0:
            return False

    return True
