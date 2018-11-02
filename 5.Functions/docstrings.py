def my_function():
    """Documentation for my function"""
    print("Hi")


print(my_function.__doc__)  # Documentation for my function

print([1, 2, 3].pop.__doc__)
# Remove and return item at index (default last).
# Raises IndexError if list is empty or index is out of range.

help(print)
