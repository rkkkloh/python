import random

x = random.randint(1,6)
y = random.random()

list = ['rock','scissors','paper']
z = random.choice(list)

cards = [1,2,3,4,5,6,7,8,9,"J","Q","K","A"]

random.shuffle(cards)
print(cards)
print(z)