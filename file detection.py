import os

path = "/Users/ruikangloh//Desktop/python"

if os.path.exists(path):
    print("That location exist!")
    if os.path.isfile(path):
        print("That is a file!")
    elif os.path.isdir(path):
        print("That is a directory!")
else:
    print("That location doesn't exist!")