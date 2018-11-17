def fib_list(length):  # list
    nums = []
    a, b = 0, 1
    while len(nums) < length:
        nums.append(b)
        a, b = b, a + b
    return nums


def fib_gen(length):  # generator
    a, b = 0, 1
    count = 0
    while count < length:
        yield b
        a, b = b, a + b
        count += 1


for n in fib_gen(100):
    print(n)

# the generator yields one item at a time — thus it is more memory efficient than a list
