class Counter:
    def __init__(self, low, high):
        self.current = low
        self.high = high

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.high:
            n = self.current
            self.current += 1
            return n
        raise StopIteration


for i in Counter(1, 10):
    print(i)  # 1 - 9


class Fibbonaci:
    def __init__(self):
        self.previous = 0
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        val = self.current
        self.current += self.previous
        self.previous = val
        return val


f = Fibbonaci()
print(next(f))  # 1
print(next(f))  # 1
print(next(f))  # 2
print(next(f))  # 3
print(next(f))  # 5
