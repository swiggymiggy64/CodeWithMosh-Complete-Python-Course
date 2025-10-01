
# * Comparison Operators

# print(10 > 3)  # true
# print(10 >= 3)  # true
# print(10 < 20)  # true
# print(10 <= 20)  # true
# print(10 == 10)  # true == equality operator
# print(10 == "10")  # false differnt type
# print(10 != "10")  # true


# print("bag" > "apple")  # true, compares alphabetically
# print("bag" == "BAG")  # false
# print(ord("b"))  # 98
# print(ord("B"))  # 66

# * Conditional Statements

# temperature = 22

# if temperature > 30:
#     # This is indented to indicate it is within the block scope of the if temperature > 30:
#     print("It's too hot!")
# elif temperature > 20:
#     print("It's nice temperature!")
# else:
#     print("It's cold!")
# print("Done")  # always executed due to indentation returned to normal

# * Ternery Operator

# age = 22

# instead of this:
# if age >= 18:
#     message = "Eligible"
# else:
#     message = "Not eligible"
# print(message)

# do this:
# message = "Eligible" if age >= 18 else "Not eligible"
# print(message)

# * Logical Operators
# and
# or
# not

# high_income = True
# good_credit = True
# student = True

# if (high_income or good_credit) and not student:
#     print("Eligible")
# else:
#     print("Not eligible")

# * Short-circuit Evaluation

# high_income = False
# good_credit = True
# student = True

# # This if statement is checked from left value to the right, so if high_income is false, then it fails & doesnt check the other two
# if high_income and good_credit and not student:
#     print("Eligible")
# else:
#     print("Not eligible")

# * Chaining Comparison Operators

# age should be between 18 & 65

# age = 22
# # if age >= 18 and age < 65:  # This normal way of writing out an if statement
# # Is the same for this mathematical way of writing it out.
# if 18 >= age < 65:
#     print("Eligible")

# * For Loops

# instead of this:
# print("Sending a message")
# print("Sending a message")
# print("Sending a message")

# You can do this:
# for num in range(3):
#     print("Sending a message", num + 1, (num + 1) * ".")

# Also rather then adding + 1 you can do this:
# for num in range(1, 4):
#     print("Sending a message", num, num * ".")

# You can add a step as an arguement like this:
# for num in range(1, 10, 2):
#     print("Sending a message", num, num * ".")

# * For Else
# successful = False
# for num in range(3):
#     print("Attempt")
#     if successful:
#         print("Successful")
#         break  # This will stop the loop
# else:  # This else block runs if there is no break out of the loop
#     print("Attempted 3 times & failed")

# * Nested loops

# for x in range(5):
#     for y in range(3):
#         print(f"(x: {x}, y: {y})")

# * Iterables

# print(type(5))  # <class 'int'>
# print(type(range(5)))  # <class 'range'>

# # Iterates x as int
# for x in range(5):
#     print(f"x: {x}")

# # Iterates x as a string
# for x in "Python":
#     print(f"x: {x}")

# # Iterates x as a list
# for x in [1, 2, 3, 4]:
#     print(f"x: {x}")

# * While Loops

# x = 1
# while x < 10:
#     print("x is less than 10!")
#     x += 1  # Dont forget to iterate the variable used to avoid a infinite loop

# * Infinite Loops

# while True:  # This kills the crab
#     print("x is less than 10!")

# * Exercise
# Way 1
# x_num = 0
# for num in range(2, 10, 2):
#     x_num += 1
#     print(num)
#     if num >= 8:
#         print(f"We have {x_num} numbers")

# Way 2
x_num = 0
for num in range(1, 10):
    if not num % 2:
        x_num += 1
        print(num)
print(f"We have {x_num} numbers")
