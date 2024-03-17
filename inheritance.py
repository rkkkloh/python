class animal:
    isAlive = True
    def eat(self):
        print(self.species + " is eating")
    def sleep(self):
        print(self.species + " is sleeping")

class Rabit(animal):
    species = "rabbit"

class Snake(animal):
    species = "snake"

class Hawk(animal):
    species = "hawk"

rabbit = Rabit()
snake = Snake()
hawk = Hawk()

print(rabbit.isAlive)
snake.eat()
hawk.sleep()

