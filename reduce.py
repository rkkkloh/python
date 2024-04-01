# reduce = apply a function to an iterable and reduce it to a single cumulative value.
#          performs function on first two elements and repeats process until 1 value remains
#
# reduce(function, iterable)

import functools
letter = ["H","E","L","L","O"]
word = functools.reduce(lambda x,y,:x+y,letter)

print(word)

numbers = [5,4,3,2,1]
result = lambda number1,number2:number1*number2

print(functools.reduce(result,numbers))
