# Higher order fucntion = a function either:
#                         1. accepts a fucntion as an argument
#                            or
#                         2. returns a function
#                         (In python, functions are also treated as object)

# function to variable
def hi():
    print("fuck you jibai lanjiao")

greet = hi
hi()
greet()

# higher order function

def loud(text):
    return text.upper()

def quiet(text):
    return text.lower()

def hello(func):
    print(func("Hello"))

hello(loud)
hello(quiet)

def divisor(x):
    def divident(y):
        return y/x
    return divident

divide = divisor(2)
print(divide(10))
print(divisor(2)(10))