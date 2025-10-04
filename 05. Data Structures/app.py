
# * Lists
# letters = ["a", "b", "c"]
# matrix = [[0, 1], [2, 3]]  # matrix = 2 dimensional list

# # if I wanted a list of 100 0, instead of doing it manually:
# # [0, 0, 0.....]
# # Do this:
# zeros = [0] * 5
# # print(zeros)

# combined = zeros + letters  # concatinates 2 lists
# # print(combined)

# numbers = list(range(20))
# # print(numbers)

# chars = list("Hello World!")
# # print(chars)
# print(len(chars))

# * Accessing Items
# letters = ["a", "b", "c", "d"]
# letters[0] = "A"
# print(letters[0])
# print(letters[-1])
# print(letters)
# print(letters[0:3])
# print(letters[:3])
# print(letters[0:])
# print(letters[:])
# print(letters[::2])

# numbers = list(range(20))
# print(numbers)
# print(numbers[::2])  # every x number in the list
# print(numbers[::-1])  # all items in reverse

# * List Unpacking

# numbers = [1, 2, 3]
# doing this:
# first = numbers[0]
# second = numbers[1]
# third = numbers[2]

# is the same as this:
# first, second, third = numbers

# Doing it this way must have the same number of variable names as there are items in the list, so this wont work:
# first, second = numbers  # ValueError: too many values to unpack (expected 2)

# BUT you can grab the first 2 list values inside variables & pack the rest like so:
# numbers = [1, 2, 3, 4, 5]
# first, second, *other = numbers
# first, *other, last = numbers

# print(first)
# # print(second)
# print(other)
# print(last)

# * Looping over lists

# letters = ["a", "b", "c"]
# # items = [0, "a"]  # List
# # items = (0, "a")  # Touple
# # index, letter = items
# for index, letter in enumerate(letters):
#     # print(letter)
#     # print(letter[0], letter[1])
#     print(index, letter)

# * Adding or Removing Items

# letters = ["a", "b", "c"]

# # Add

# letters.append("d")  # Adds to the end of the list
# letters.insert(0, "1")  # Specify the index & then item to add

# # Remove
# letters.pop()  # Remove the last item in the list
# letters.pop(0)  # Or remove at specific index
# letters.remove("b")  # Removes the 1st occurance of argument found in list
# del letters[0:1]  # Remove a range of items
# letters.clear()  # Remove ALL items from list

# print(letters)

# * Finding Items

# letters = ["a", "b", "c"]

# a = letters.index("a")
# print(a)

# # d = letters.index("d")
# # print(d)  # This causes an error: ValueError: 'd' is not in list.

# # So we can instead check if "d" exists first like this:
# if "d" in letters:
#     d = letters.index("d")
#     print(d)

# d_count = letters.count("d")

# * Sorting Lists

# numbers = [3, 51, 2, 8, 6]
# # numbers.sort()
# # numbers.sort(reverse=True)
# sorted_numbers = sorted(numbers)
# print(numbers)
# print(sorted_numbers)

# items = [
#     ("Product1", 10),
#     ("Product2", 9),
#     ("Product3", 12),
# ]


# def sort_item(item):
#     return item[1]


# items.sort(key=sort_item)
# print(items)

# * Lambda Functions
# In the above code we can use Lambda Function or Lambda Expression to make the code cleaner

# items = [
#     ("Product1", 10),
#     ("Product2", 9),
#     ("Product3", 12),
# ]

# # Instead of using this function
# # def sort_item(item):
# #     return item[1]

# # We can tell sort() to use an lambda/anonymous function & then do the following "parameters:expression"
# items.sort(key=lambda item: item[1])
# print(items)

# * Map Functions

# items = [
#     ("Product1", 10),
#     ("Product2", 9),
#     ("Product3", 12),
# ]

# # Instead of doing this:
# # prices = []
# # for item in items:
# #     prices.append(item[1])
# # print(prices)

# # You can do this
# prices = list(map(lambda item: item[1], items))
# print(prices)

# * Filter Functions

# items = [
#     ("Product1", 10),
#     ("Product2", 9),
#     ("Product3", 12),
# ]

# x = list(filter(lambda item: item[1] >= 10, items))
# print(x)

# * List Comprehensions

# items = [
#     ("Product1", 10),
#     ("Product2", 9),
#     ("Product3", 12),
# ]

# prices = list(map(lambda item: item[1], items))
# # [expression for item in items]
# # List comprehension, does the same as "prices" of above
# prices = [item[1] for item in items]


# filtered = list(filter(lambda item: item[1] >= 10, items))
# # Does same as above, with less & is more performant
# filtered = [item for item in items if item[1] >= 10]

# * Zip Function

# list1 = [1, 2, 3]
# list2 = [10, 20, 30]

# # [(1, 10), (2, 20), (3, 30)] # How do we do this list?

# # list3 = list(zip(list1, list2))
# list3 = list(zip("abc", list1, list2))
# print(list3)

# * Stacks
# LIFO = Last In - First Out

# browsing_session = []
# browsing_session.append(1)
# browsing_session.append(2)
# browsing_session.append(3)
# print("First browse", browsing_session)

# last = browsing_session.pop()
# print(last)
# print("First back", browsing_session)
# print("redirect", browsing_session[-1])

# # browsing_session.pop()
# # browsing_session.pop()
# if not browsing_session:
#     print("back button disabled")

# * Queues
# FIFO = First In - First Out

# from collections import deque
# queue = deque([])
# queue.append(1)
# queue.append(2)
# queue.append(3)

# queue.popleft()
# print(queue)
# # queue.popleft()
# # queue.popleft()
# if not queue:
#     print("empty")

# * Tuples

# point = 1, 2  # Tuple doesnt need () & python will know it is a tuple
# point = 1, # Also if you want a Tuple with a single item, add the trailing comma , otherwise python will think it is an int or other primitive type.
# point = () # & if you want an empty Tuple use empty ().
# print(type(point))

# point = (1, 2) + (3, 4)  # You can concatinate tuples
# point = (1, 2) * 3  # You can multiply to repeat = (1, 2, 1, 2, 1, 2)
# point = tuple([1, 2])  # You can convert lists into tuples
# print(point)

# point = (1, 2, 3)
# print(point[0])
# print(point[0:2])

# x, y, z = point
# if 10 in point:
#     print("Exists")

# point[0] = 10

# * Swapping Variables

# x = 10
# y = 11
# print(x)
# print(y)

# # z = x
# # x = y
# # y = z

# x, y = y, x  # This one line does what the other 3 lines do!
# print(x)
# print(y)

# * Arrays

# from array import array

# numbers = array("i", [1, 2, 3])
# numbers.append(4)
# print(numbers)

# * Sets

# numbers = [1, 1, 2, 3, 4]
# first = set(numbers)
# second = {1, 5}
# # print(first)
# x = first | second
# # print(x)
# print(first & second)  # Shows numbers in both sets
# print(first - second)  # Shows the difference between two sets
# print(first ^ second)  # Shows the items either in the 1st or 2nd set but not both

# # print(first[0]) # TypeError: 'set' object is not subscriptable
# if 1 in first:
#     print("Yes")

# * Dictionaries

# # point = {"x": 1, "y": 2}  # This is one way
# point = dict(x=1, y=2)  # This way doesn't need strings & is cleaner
# # print(point[0])  # Doesn't work, need to specify the key
# # print(point["x"])  # This is how to get a value
# point["x"] = 10  # Reassigning key values
# point["z"] = 20  # Asigning a new key value pair
# # print(point)

# # If you try to search a key which doesnt exist you get an error
# # print(point["a"])  # KeyError: 'a'

# # So you can check for it in an if statement:
# # if "a" in point:
# #     print(point["a"])

# # OR you can use the .get() method like this:
# print(point.get("a"))  # Is much cleaner & will return "None" instead of an error
# # Is much cleaner & will return "None" instead of an error
# # You can even specify a return value if it didnt find the 1st arguement
# print(point.get("a", "Oopsie Daisy!"))

# del point["x"]
# # print(point)

# for key in point:
#     print("Way 1:", key, point[key])

# for x in point.items():
#     print("Way 2:", x)

# for key, value in point.items():
#     print("Way 3:", key, value)

# * Dictionary Comprehensions

# These 3 lines below:
# values = []
# for x in range(5):
#     values.append(x * 2)

# Are the same as this single line:
# values = [x * 2 for x in range(5)]  # List
# values = {x * 2 for x in range(5)}  # Set: [] to {} =  List to Set
# The difference between a Set & a Dictionary is that Sets just have values:
# {1, 2, 3}
# But Dictionaries have key value pairs which are separated by a colon:
# {"x": 1, "y": 2, "z": 3} # OR
# {1: "a", 2: "b", 3: "c"}

# So going back to this:
# values = {x * 2 for x in range(5)}  # Set
# We can change it into a dictionary like this:
# values = {x: x * 2 for x in range(5)}
# print(values)

# We can use tuples as well
# values = (x * 2 for x in range(5))
# print(values)

# * Generator Expressions
