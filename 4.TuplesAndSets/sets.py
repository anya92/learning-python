"""
  Sets:
  - collections which are unordered and unindexed
  - items will appear in a random order
  - are written with curly brackets
"""

# creating sets

s = set({1, 2, 4})
print(s)  # {1, 2, 4}

s2 = {1, 5, 2, 1, 4, 5}
print(s2)  # {1, 2, 4, 5}

# accessing items - you cannot access items in a set by referring to an index, since sets are unordered the items has no index

# checking if item exists

print(4 in s)  # True
print(0 in s2)  # False

# set methods

# add - adds an element to the set

s.add(5)
print(s)  # {1, 2, 4, 5}
s.add(2)
print(s)  # {1, 2, 4, 5}

# remove - removes the specified element, KeyError if the element is not found

s.remove(1)
print(s)  # {2, 4, 5}
# s.remove(10) # KeyError

# discard - removes the specified item, no error if the item does not exists

s.discard(2)
print(s)  # {4, 5}
s.discard(10)
print(s)  # {4, 5}

# copy - returns a copy of the set

s3 = s2.copy()
print(s3 == s2)  # True
print(s3 is s2)  # False

# clear - removes all the elements from the set

s2.clear()
print(s2)  # set()
