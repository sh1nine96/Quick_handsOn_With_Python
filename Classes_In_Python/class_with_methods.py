# classes can have functions too, which are known as methods when they are inside class


class Pet:
    color = "brown"
    legs = 4

# self is a special keyword that we need to use inside our class definition. We pass self
# as first parameter of all the methods we add

    def bark(self):
        print("woof woof!!")

 # we use self to access class variables like color and legs below:

    def display_color(self):
        print(f"I am a {self.color} dog")

    def display_legs(self):
        print(f"I have {self.legs} legs")


rocky = Pet()
rocky.bark()
rocky.display_color()
rocky.display_legs()


class Pokemon:
    name = "Pikachu"
    color = "yellow"
    hands = 2

    def introduce(self):
        print(f"Hi, I am {self.name}")

    def show_color(self):
        print(f"My color is {self.color}")


pikachu = Pokemon()
pikachu.introduce()
pikachu.show_color()

# we can access class variables as follows

piku_hands = pikachu.hands
print(f"I have {piku_hands} hands")
