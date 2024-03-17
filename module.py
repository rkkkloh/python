# module = a file containing python code. May contain functions, classes, etc.
# used with modular programming, which is to separate a program into parts

import import_module as mdl
# from import-module import hello,bye
# from import_module import *
# hello()
# bye()

try:
    mdl.hello()
    mdl.bye()
except NameError:
    print("Check the alias of the import module")

# help("modules")