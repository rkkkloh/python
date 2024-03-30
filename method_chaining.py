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
    def __init__(self,make,model,year,color):
        self.make = make    #instance variable
        self.model = model  #instance variable
        self.year = year    #instance variable
        self.color = color  #instance variable
        
    
    def accelerate(self):
        print("The car is accelerating")
        return self

    def drive(self):
        print("This car is driving")
        return self

    def stop(self):
        print("This car is stopped")
        return self

car = Car("Tesla","xx-24",2024,"white")
car.drive().accelerate().stop()