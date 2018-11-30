# To write to an existing file, you must add a parameter to the open() function:
# "a" => will append to the end of the file
# "w" => will overwrite any existing content

# "w" also creates a new file if it does not exist

with open('hello_darkness.txt', "w") as f:
    f.write("Hello darkness, my old friend\n")
    f.write("I've come to talk with you again\n")


with open('hello_darkness.txt', "a") as f:
    f.write("Because a vision softly creeping\n")
    f.write("Left its seeds while I was sleeping\n")
