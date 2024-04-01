# zip(*iterable) = aggregte elements from two or more iterables (lists,tuples,sets,etc)
#                  creates a zip object with period elements stored in tuples for each element

username = ["Dude","Bro","Mister"]
password = ("p@ssword","abc123","guest")

users = dict(zip(username,password))
#print(users)
#users = zip(username,password)
#print(type(users))
for i in users.items():
    print(i)

for i in users:
    print(i)

for key,value in users.items():
    print(key,value)