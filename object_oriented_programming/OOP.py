# In object oriented pragramming(OOP), we group data and functionality as properties and methods inside objects, like Virutal_Pet here

class Virtual_Pet:
    def __init__(self, color, name) -> None:
        self.color = color
        self.name = name


rocky = Virtual_Pet("brown", "rocky")

print(rocky.color)
print(rocky.name)

# OOP is useful for modelling objects, real life or not. Objects have properties and methods that we treat as one thing, like car here


class Car:
    mileage = 12000

    def drive(self, miles):
        self.mileage += miles


tesla = Car()
tesla.drive(900)
print(tesla.mileage)

# In OOP, we use methods to update existing values of an object, like here where we use eat() to update the value of hungry


class Dog:
    hungry = True

    def eat(self):
        self.hungry = False


print(Dog.hungry)  # will return true

mini = Dog()
mini.eat()
print(mini.hungry)  # will return false


class Piggy:
    value = 0

    def addMoney(self, amount):
        self.value += amount


myPiggy = Piggy()
myPiggy.addMoney(100)
print(myPiggy.value)
