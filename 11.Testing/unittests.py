import unittest  # a unit testing framework
from functions import fib, is_prime


class FibbonaciTest(unittest.TestCase):
    def test_calculation(self):
        self.assertEqual(fib(0), 0)
        self.assertEqual(fib(1), 1)
        self.assertNotEqual(fib(5), 6)
        self.assertEqual(fib(10), 55)


class PrimeTests(unittest.TestCase):
    def test_is_seven_prime(self):
        """7 should be determined to be prime"""
        self.assertTrue(is_prime(7), msg="7 is prime")

    def test_is_nine_not_prime(self):
        """9 should not be determined to be prime"""
        self.assertFalse(is_prime(9), msg="9 is not prime")

    def test_are_zero_and_one_not_prime(self):
        """0 and 1 should not be determined to be prime"""
        self.assertFalse(is_prime(0), msg="0 is not prime")
        self.assertFalse(is_prime(1), msg="1 is not prime")

    def test_negative_numbers(self):
        """Negative numbers should not be determined to be prime"""
        for n in range(-1, -10, -1):
            self.assertFalse(is_prime(n), msg=f"{n} is not prime")


if __name__ == "__main__":
    unittest.main()

# > py unittests.py - v

# if error:

# test_calculation (__main__.FibbonaciTest) ... FAIL
# test_are_zero_and_one_not_prime (__main__.PrimeTests)
# 0 and 1 should not be determined to be prime ... ok
# test_is_nine_not_prime (__main__.PrimeTests)
# 9 should not be determined to be prime ... ok
# test_is_seven_prime (__main__.PrimeTests)
# 7 should be determined to be prime ... ok
# test_negative_numbers (__main__.PrimeTests)
# Negative numbers should not be determined to be prime ... ok

# ======================================================================
# FAIL: test_calculation (__main__.FibbonaciTest)
# ----------------------------------------------------------------------
# Traceback (most recent call last):
#   File "unittests.py", line 7, in test_calculation
#     self.assertEqual(fib(0), 0)
# AssertionError: 1 != 0

# ----------------------------------------------------------------------
# Ran 5 tests in 0.006s

# FAILED (failures=1)

# if no error:

# test_calculation(__main__.FibbonaciTest) ... ok
# test_are_zero_and_one_not_prime(__main__.PrimeTests)
# 0 and 1 should not be determined to be prime ... ok
# test_is_nine_not_prime(__main__.PrimeTests)
# 9 should not be determined to be prime ... ok
# test_is_seven_prime(__main__.PrimeTests)
# 7 should be determined to be prime ... ok
# test_negative_numbers(__main__.PrimeTests)
# Negative numbers should not be determined to be prime ... ok

# ----------------------------------------------------------------------
# Ran 5 tests in 0.006s

# OK
