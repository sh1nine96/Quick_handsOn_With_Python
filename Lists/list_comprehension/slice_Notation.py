#  if we want to retrieve multiple values from a list, we can do it using slicing

items = ["eggs", "floor", "sugar", "salt"]
# will print from start(first arg) upto end(last arg) exluding end item
print(items[0: 2])

# value left to the colon(:) is start, indexing starts from 0

letters = ["a", "b", "c", "d", "e"]
print(letters[4:])
print(letters[1:])

# start value can be positive, negative or omitted,
# negative means start this many elements from back, 0 means same as omitted
users = ["Alan", "John", "Ken", "Peter", "Paul"]
print(users[0:])
print(users[:])
print(users[-2:])

# range outside the length will print empty list not error
print(users[7:])

# values after the colon represents where slice should stop or end
print(users[1:4])

# we can omit start value or put it as 0 both means same
print(users[:3])
print(users[0:3])

# start index > end index will result in empty list not error
print(users[3:1])

# we can use format with 2 colons, [start:stop:step], where step determines how python steps
# between start and end

alphabets = ["a", "b", "c", "d", "e", "f",
             "g", "h", "i", "j", "k", "l", "m", "n"]
print(alphabets[2:12])
print(alphabets[2:12:3])
# step value 2 => return every 2nd value, 2 => return every 3rd value instead of every value
print(alphabets[0:12:2])

# we can omit start and end, by default it will start from 0 and stop and end
print(alphabets[:: 2])

# step can be negative, it will allow us to have start > end
# order will be reversed this time
print(alphabets[6:0:-1])
# empty list will be returned if we put start < end for negative step value
# because the step always works from the start value
print(alphabets[0:6:-1])
