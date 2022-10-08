class Virtual_Pet:
    def __init__(self, color, legs):
        self.color = color
        self.legs = legs


rocky = Virtual_Pet("brown", 4)
benny = Virtual_Pet("black", 8)

print(rocky.color)
print(benny.color)
print(rocky.legs)


class Pie:
    def __init__(self, flavor, ingredients):
        self.flavor = flavor
        self.ingredients = ingredients

    def print_ingredients(self):
        for i in self.ingredients:
            print(i)


applePie = Pie('apple', ['flour', 'eggs', 'apples', 'butter'])

print(applePie.flavor)
applePie.print_ingredients()
