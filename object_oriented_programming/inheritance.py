# when we create objects one by one we run into the problem of having duplicate code. How many greet() methods are there? below


class Person1:
    name = "Sam"

    def greet(self):
        print("Hi")


class Person2:
    name = "Mike"

    def greet(self):
        print("Hi")


class Person3:
    name = "Jenny"

    def greet(self):
        print("Hi")

# to overcome this problem, we uses inheritance to make our code efficient. Through inheritance, classes recieve methods from other classes
# Inheritance lets us create classes that have different properties and behaviours without coding each one from scratch


class Parent:
    def __init__(self) -> None:
        self.eyes = "green"


# here we can see that Child is inheriting the Parent class bcz it's inside parethesis after the class name


class Child(Parent):
    def __init__(self) -> None:
        super().__init__()
        self.age = "7"


# through this we are able to have properties of parent class in child class

child = Child()
print(child.eyes)
print(child.age)


class Greetings:
    def greet(self):
        print("Hi!")


class Person(Greetings):
    name = "George"


p = Person()
p.greet()


# we can update how classes work by setting methods directly in the class. we will define "charge" method inside "Hybrid" class

class Car:
    def start_car(self):
        print("starting car")


class Hybrid(Car):
    def charge(self):
        print("using fuel to charge battery")


class Electric(Car):
    def fuel(self):
        print("No fuel required")


prius = Hybrid()
electric = Electric()


prius.start_car()
electric.start_car()

prius.charge()
electric.fuel()
