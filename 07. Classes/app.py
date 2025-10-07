
# * Classes
# Classes are blueprints for creating new objects
# an object is an instance of a class

# Class: Human
# Object: John, Mary, Jack etc

# numbers = [1, 2]
# numbers.

# x = 1
# print(type(x))  # <class 'int'>

# * Creating Classes

# class Point:
#     def draw(self):
#         print("draw")


# point = Point()
# print(type(point))  # <class '__main__.Point'>
# print(isinstance(point, Point))  # True

# * Constructors

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def draw(self):
#         print(f"Point ({self.x}, {self.y})")


# point = Point(1, 2)
# # print(point.x)
# point.draw()

# * Class vs Instance Attributes

# class Point:
#     default_color = "red"  # Class level attribute, shared across all instances

#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def draw(self):
#         print(f"Point ({self.x}, {self.y})")


# point = Point(1, 2)
# Point.default_color = "yellow"  # Class attribute
# point.default_color = "blue"  # Instance attribute
# print(Point.default_color)  # Class attribute
# print(point.default_color)  # Instance attribute
# # point.z = 10
# point.draw()

# another = Point(3, 4)
# another.draw()

# * Class vs Instance Methods

# class Point:
#     def __init__(self, x, y):  # Instance method
#         self.x = x
#         self.y = y

#     @classmethod  # 3. & use @classmethod to make it a class method
#     def zero(cls):  # Which does the same as 1. anyway
#         return cls(0, 0)

#     def draw(self):  # Instance method
#         print(f"Point ({self.x}, {self.y})")


# # point = Point(0, 0) # 1. Instead of this
# point = Point.zero()  # 2. We can call this
# point.draw()

# * Magic Methods

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __str__(self):
#         return f"({self.x}, {self.y})"

#     def draw(self):
#         print(f"Point ({self.x}, {self.y})")


# point = Point(1, 2)
# print(point)

# * Comparing Objects

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y


# point = Point(1, 2)
point = Point(10, 20)
other = Point(1, 2)

# False because it compares the references or addresses in memory
# True if we have defined __eq__ within Point
print(point == other)

print(point > other)

print()
