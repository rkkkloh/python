class Organism:
    isAlive = True

class Animal(Organism):
    def eat(self):
        print("This animal is eating")

class Dog(Animal):
    def bark(self):
        print("The dog is barking")

dog = Dog()
print(dog.isAlive)
dog.eat()