class Car:
    make = "toyota" #class variable
    #model = None    #class variable
    year = None     #class variable
    color = None    #class variable

    #def __init__(self):
    #        self.make
    #        self.model
    #        self.year
    #        self.color

    # only one constructor is allowed
    def __init__(self,model,year,color):
        #self.make = make    #instance variable
        self.model = model  #instance variable
        self.year = year    #instance variable
        self.color = color  #instance variable
    
    def accelerate():
        print("The car is accelerating")

    def drive(self):
        print("This car is driving")

    def stop(self):
        print("This car is stopped")

car_1 = Car("x-17",2004,"red")
#car_2 = Car()
print(car_1.model)
print(car_1.make)
#print(car_2.make)

#car_1.make = "Honda"
#car_2.make = "Mitsubitshi"
#print(car_1.make)
#print(car_2.make)

#car_1.drive()
#car_1.stop()

#Car.make = "Proton"

#print(car_1.make)
#print(car_2.make)
print(Car.make)
Car.accelerate()