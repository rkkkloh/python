# lambda function = function written in 1 line using lamda keyword
#                  accepts any number of arguments, but only has one expression.
#                  (think of it as a shortcut)
#                  (useful if needed for a short period of time, throw- away)
#
# lambda parameters:expression

double = lambda x:x*2
print(double(5))
multiply = lambda x,y:x*y
print(multiply(5,6))
add = lambda x,y,z:x+y+z
print(add(3,4,5))
full_name = lambda first_name,last_name:first_name + " " + last_name
print(full_name("Rui Kang","Loh"))
age_check = lambda x:True if x >= 18 else False
print(age_check(18))
