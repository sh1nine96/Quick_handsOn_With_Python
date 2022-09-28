# python allow us to use negative indexing to retrieve values from the end of an indexable object

scores = [4.5, 5, 7, 4, 3.5, 4]
latest = scores[-1]
print(latest)

# negative indexing means that we can retrieve an element from the rightmost side of a list. we use the - symbol
# to indicate a negative index

users = ["shubham", "raja", "karan", "ankita", "hina"]
last = users[-1]
print(last)

# we can use any negative value up to the length of list which would return the first element

ratings = [4, 5, 1, 2, 3, 7]
print(ratings[-6])

# we can also modify list items in given position

users = ["shubham", "shiny", "kunal", "haryy", "ashu"]
users[-3] = "john"
print(users)

# tuples are ordered data structure and valus can be retrieved but they're immutable
# will throw error => 'tuple' object does not support item assignment

# info = ("graz", "Austria", "Europe", "World")
# info[-4] = "vienna"

# we will encounter error if we try to retrieve a value outside the object's range
# will throw error => list index out of range

# results = ["win", "loss", "draw"]
# results[-5]

# the del keyword allow us to delete any object or item in data struture such as dictionary, lists, sets

winners = ["john", "helen", "dianna", "olaf", "daniel"]
# it will delete dianna
del winners[-2]
print(winners)
