
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

items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
]

# Instead of doing this:
# prices = []
# for item in items:
#     prices.append(item[1])
# print(prices)

# You can do this
prices = list(map(lambda item: item[1], items))
print(prices)
