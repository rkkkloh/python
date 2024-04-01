# sort() method = used with list (built-in method for list only)
# sorted() function = used with iterables

students1 = ["rk","rz","my","jx","ch"]
students2 = ("rk","rz","my","jx","ch")
  
sorted_students2 = sorted(students2,reverse = True)
sorted_students1 = sorted(students1)
#students.sort(reverse = True)

print(sorted_students1)
print(sorted_students2)
students1.sort(reverse = True)
print(students1)

students = [("Spongebob","A",20),
            ("Mr.Krabs","D",55),
            ("Sandy","B",23),
            ("Patrick","F",21),
            ("Squidward","C",20)]

grades = lambda grade:grade[1]
students.sort(key=grades)

for i in students:
    print(i)

students3 = (("Spongebob","A",20),
            ("Mr.Krabs","D",55),
            ("Sandy","B",23),
            ("Patrick","F",21),
            ("Squidward","C",20))
print()
ages = lambda age:age[2]

sorted_students3 = sorted(students3,key=ages)

for i in sorted_students3:
    print(i)