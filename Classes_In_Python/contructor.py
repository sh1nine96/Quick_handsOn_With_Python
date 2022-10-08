class Virtual_Pet:
    def __init__(self, color, legs):
        self.color = color
        self.legs = legs


rocky = Virtual_Pet("brown", 4)
benny = Virtual_Pet("black", 8)

print(rocky.color)
print(benny.color)
print(rocky.legs)
