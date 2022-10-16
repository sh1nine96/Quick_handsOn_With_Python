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


# class Parent:
#     def __init__(self) -> None:
#         self.eyes = "green"


# here we can see that Child is inheriting the Parent class bcz it's inside parethesis after the class name


# class Child(Parent):
#     def __init__(self) -> None:
#         super().__init__()
#         self.age = "7"


# through this we are able to have properties of parent class in child class

# child = Child()
# print(child.eyes)
# print(child.age)

#-------------------------------------------------------#


# class Greetings:
#     def greet(self):
#         print("Hi!")


# class Person(Greetings):
#     name = "George"


# p = Person()
# p.greet()


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

#--------------------------------------------------------#
# classes contain a method called as constructor that sets the properties of new objects, known as instances


class Person:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def greet(self):
        print("Hi!")


class Nurse(Person):
    def __init__(self, name, age) -> None:
        super().__init__("Nurse " + name, age)

    def intro(self):
        print(f"Hi, I am {self.name}")


class Student(Person):
    def __init__(self, name, age, major) -> None:
        super().__init__(name, age)
        self.major = major


class Parent(Person):
    def __init__(self, name, age, kids):
        super().__init__(name, age)
        self.kids = kids

# we can now create objects that own properties and inherit methods from both Student and Person

# sam = Person("Sam", 25)
# print(sam.name, sam.age)


person1 = Nurse("Sam", 30)
person2 = Nurse("Tom", 34)

person1.intro()
person2.greet()

student = Student("Simon", 22, "chemistry")
print(student.major)
student.greet()

parent = Parent("Adam", 45, 3)
print(parent.name, parent.age, parent.kids)
