
# * Functions & Arguements

# def greet(string, str2=""):
#     print(string)


# greet("Hello!")

# * Types of Functions

# 1 - Perform a task
# print("")
# 2 - Return a value
# round(1.9)

# def get_greeting(name):
#     return f"Hi {name}"


# message = get_greeting("Mig")
# print(message)

#  * Keyword Arguments

# def increment(num, by):
#     return num + by


# result = increment(2, 1)
# print(result)
# print(increment(2, 1))
# print(increment(num=2, by=1))

#  * Default Arguments

# def increment(num=1, by=1):
#     return num + by


# print(increment())

#  * *args, wait, what?

# def multiply(x, y):
#     return x*y


# def multiply(*numbers):
#     # print(numbers)
#     total = 1
#     for number in numbers:
#         # print(number)
#         total *= number
#     print(total)
#     return total


# multiply(2, 3, 4, 5)

# **args

# def save_user(**user):
#     # print(user)
#     print(user["name"])


# save_user(id=1, name="John", age=32)

# * Scope

# message = "a"


# def greet(name):
#     # global message
#     message = "b"


# def send_email(name):
#     message = "b"

# These are local variables to greet() & send_email
# print(name)  # Wont work name is within greet scope block
# print(message)  # Wont work message is within greet scope block


# Now however this is a global variable & can be used anywhere in this file:
# message = "a"
# print(message)

# greet("Mig")

# print(message)

# * Debugging

# def multiply(*numbers):
#     total = 1
#     for number in numbers:
#         total *= number
#         # return total  # Were indenting this to create a bug
#     return total


# print("Start")
# print(multiply(1, 2, 3))

# * Exercise
# Rules
# If the input is divisible by 3, return "Fizz"
# If the input is divisible by 5, return "Buzz"
# If the input is divisible by 3 AND 5, return "FizzBuzz"
# For any other numbers it will return the same input, ie FB(7) returns 7


def fizz_buzz(input):
    if (input % 3 == 0) and (input % 5 == 0):
        return "FizzBuzz"
    elif input % 5 == 0:
        return "Buzz"
    elif input % 3 == 0:
        return "Fizz"
    return input


print(fizz_buzz(3))
print(fizz_buzz(5))
print(fizz_buzz(15))
print(fizz_buzz(7))
