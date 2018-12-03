import pickle

l = [12, 65, 32, 65]

# Write a pickled representation of obj to the object file
with open("list.pickle", "wb") as file:
    pickle.dump(l, file)

# Read a pickled object representation from the object file
with open("list.pickle", "rb") as file:
    pickled_list = pickle.load(file)
    print(pickled_list)  # [12, 65, 32, 65]
