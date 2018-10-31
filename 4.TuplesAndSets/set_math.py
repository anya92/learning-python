# Union of two sets
# The union of two sets A and B, denoted by A ∪ B, is the set of elements which are in A, in B, or in both A and B.

A = {1, 2, 3}
B = {2, 3, 4}

print(A | B)  # {1, 2, 3, 4} or
print(A.union(B))  # {1, 2, 3, 4}

# Intersection of two sets
# The intersection of two sets A and B, denoted by A ∩ B, is the set of all objects that are members of both the sets A and B.

print(A & B)  # {2, 3} or
print(A.intersection(B))  # {2, 3}

# Symetric difference of two sets
# The symetric difference of two sets is the set of elements which are in either of the sets and not in their intersection

print(A ^ B)  # {1, 4} or
print(A.symmetric_difference(B))  # {1, 4}


# Difference (complement)
# The returned set contains items that exist only in the first set, and not in both sets

print(A - B)  # {1} or
print(A.difference(B))  # {1}
print(B - A)  # {4}
