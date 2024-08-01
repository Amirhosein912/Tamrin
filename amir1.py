
"""
class Animal:
    name = "tiger"
    color = "yellow"
    speed = "120"
    
    def move():
        print("the animal is moving...")
    
    def sleep():
        print("the animal is sleeping...")

mytiger = Animal
print (mytiger.color)
mytiger.name = "irani"
mytiger.sleep()

print(mytiger.name)

mycat = Animal
mycat.name = "cat"

print(mycat.name)
mycat.move()

print(mytiger.name)
"""

class Car:
    counter = 0
    
    def __init__(self, name, model, color):
        self.__name = name
        self.__model = model
        self.__color = color
        Car.counter += 1

    def getName(self):
        return self.__name
    def setName(self, name):
        self.__name = name

pride = Car("141", "1400", "white")

print(Car.counter)

print(pride.getName())
pride.setName("142")
print(pride.getName())

peguet = Car ("206","1392","blue")

peguet.setName("207")
print(peguet.getName())

print(pride.getName())
print(peguet.counter)