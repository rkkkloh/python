# list comprehension = a way to create a new list with less syntax
#                      can mimic certain lambda functions, easier to read
#                      list = [expression for item in iterable]
#                      list = [expression for item in iterable if conditional]


square = []
for i in range(1,11):
    square.append(i*i)
print(square)

print(square2 := [i*i for i in range(1,11)])

students = [100,90,80,70,60,50,40,30,0]

#passed_student = list(filter(lambda x:x>=60,students))
#passed_student = [i for i in students if i >= 60]
passed_student = [i if i >= 60 else "failed" for i in students]

print(passed_student)



