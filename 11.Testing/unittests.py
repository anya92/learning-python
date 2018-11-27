import unittest

# unittest - a unit testing framework


def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


class FibbonaciTest(unittest.TestCase):
    def test_calculation(self):
        self.assertEqual(fib(0), 0)
        self.assertEqual(fib(1), 1)
        self.assertEqual(fib(5), 5)
        self.assertEqual(fib(10), 55)


if __name__ == "__main__":
    unittest.main()

# if error:

# F
# ======================================================================
# FAIL: test_fib (__main__.FibbonaciTest)
# ----------------------------------------------------------------------
# Traceback (most recent call last):
#   File "unittests.py", line 12, in test_fib
#     self.assertEqual(fib(0), 0)
# AssertionError: None != 0

# ----------------------------------------------------------------------
# Ran 1 test in 0.001s

# FAILED (failures=1)

# if no error:

# .
# ----------------------------------------------------------------------
# Ran 1 test in 0.023s

# OK
