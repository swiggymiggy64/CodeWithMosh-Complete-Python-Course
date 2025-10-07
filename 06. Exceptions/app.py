
# * Exceptions

# numbers = [1, 2]
# print(numbers[3])  # Error: IndexError: list index out of range

# age = int(input("Age"))  # The user needs to type an int, if they type "a"
# they get: ValueError: invalid literal for int() with base 10: 'a'

# * Handling Exceptions

# try:
#     age = int(input("Age: "))
# except ValueError as ex:
#     print("You didn't enter a valid age.")
#     print(ex)
#     print(type(ex))
# else:  # Only executed if try didnt break
#     print("No exceptions were thrown.")
# print("Execution continues.")

# * Handling Different Exceptions

# try:
#     age = int(input("Age: "))
#     xfactor = 10 / age
# except (ValueError, ZeroDivisionError):
#     print("You didn't enter a valid age.")
# else:
#     print("No exceptions were thrown.")

# * Cleaning up

# try:
#     file = open("app.py")
#     age = int(input("Age: "))
#     xfactor = 10 / age
# except (ValueError, ZeroDivisionError):
#     print("You didn't enter a valid age.")
# else:
#     print("No exceptions were thrown.")
# finally:
#     file.close()

# * The with Statement

# try:
#     with open("app.py") as file:  # with will always run .close()
#         print("File opened.")
#         file.__
#     age = int(input("Age: "))
#     xfactor = 10 / age
# except (ValueError, ZeroDivisionError):
#     print("You didn't enter a valid age.")
# else:
#     print("No exceptions were thrown.")
# # finally: # this isnt needed anymore because of with
# #     file.close()

# * Raising Exceptions

# def calculate_xfactor(age):
#     if age <= 0:
#         raise ValueError("Age cannot be 0 or less")
#     return 10 / age


# try:
#     calculate_xfactor(-1)
# except ValueError as error:
#     print(error)

# * Cost of Raising Exceptions

from timeit import timeit


code1 = """
def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be 0 or less")
    return 10 / age


try:
    calculate_xfactor(-1)
except ValueError as error:
    pass
"""

code2 = """
def calculate_xfactor(age):
    if age <= 0:
        return None
    return 10 / age


xfactor = calculate_xfactor(-1)
if xfactor == None: 
  pass
"""

print("first code=", timeit(code1, number=10000))
print("second code=", timeit(code2, number=10000))
