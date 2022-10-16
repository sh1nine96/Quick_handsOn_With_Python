# In OOP, we group together related data and fuctions in the same object. We call this encapsulation

# In OOP, we identify which methods and properties belong together and should be added to our project


class Cat:
    color = 'orange'

    def meow(self):
        print('Meow')


class Car:
    color = "gray"

    def drive(self):
        print("accelerating....")


# With encapsulation, we also have methods that use the other properties that belong to the object, like in this example eat accesses hungry

class Dog:
    name = 'Fido'
    hungry = False

    def eat(self):
        self.hungry = True

# lets make a class rectangle which calculate it area


class Rectangle:
    base = 3
    height = 4

    def getArea(self):
        return self.base * self.height


rect = Rectangle()
area = rect.getArea()
print(area)
