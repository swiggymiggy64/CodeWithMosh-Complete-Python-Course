
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
