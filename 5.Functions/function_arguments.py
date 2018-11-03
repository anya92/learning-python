# *args - syntax that lets you pass a variable number of arguments to a function


def sum_all_numbers(*nums):
    print(nums)  # (1, 4, 5, 2, 3) - tuple
    total = 0
    for num in nums:
        total += num
    return total


print(sum_all_numbers(1, 4, 5, 2, 3))  # 15

# **kwargs - the arguments are passed as a dictionary and these arguments make a dictionary inside function


def favorite_colors(**people):
    print(people)  # {'Ben': 'red', 'Jenny': 'blue', 'Chris': 'purple'}
    for person, color in people.items():
        print(f"{person}'s favorite color is {color}.")


favorite_colors(Ben="red", Jenny="blue", Chris="purple")
# Ben's favorite color is red.
# Jenny's favorite color is blue.
# Chris's favorite color is purple.

# parameter ordering:
# 1. parameters
# 2. *args
# 3. default parameters
# 4. **kwargs


def my_func(a, b, *args, name="Ted", **kwargs):
    return [a, b, args, name, kwargs]


print(my_func('a', 2, 3.14, fav_color="purple", city="London"))
# ['a', 2, (3.14,), 'Ted', {'fav_color': 'purple', 'city': 'London'}]

# (3.14,) - one item tuple

# unpacking arguments - tuples

numbers = [1, 5, 2, 5, 6, 3]  # or (1, 5, 2, 5, 6, 3)
print(sum_all_numbers(*numbers))  # 22

# unpacking arguments - dictionaries

people = {
    'Ben': 'red',
    'Jenny': 'blue',
    'Chris': 'purple'
}

print(favorite_colors(**people))
