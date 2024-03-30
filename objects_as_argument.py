class Car:
    color = None

class Motorcycle:
    color = None

def change_color(object,color):
    object.color = color
    return object

car_1 = Car()
car_2 = Car()
car_3 = Car()
bike_1 = Motorcycle()

print(change_color(car_1,"red").color)
print(change_color(car_2,"white").color)
print(change_color(car_3,"green").color)
print(change_color(bike_1,"black").color)