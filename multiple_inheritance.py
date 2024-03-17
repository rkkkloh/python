# multiple inheritance = when a child class is derived from more than one parent class

class Prey:
    def flee(self):
        print("This animal is fleeing")

class Predator:
    def hunt(self):
        print("This animal is hunting")

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey,Predator):
    pass

fish = Fish()
rabbit = Rabbit()
hawk = Hawk()

rabbit.flee()
hawk.hunt()
fish.flee()
fish.hunt()