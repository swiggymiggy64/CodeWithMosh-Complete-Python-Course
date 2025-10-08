
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

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __eq__(self, other):
#         return self.x == other.x and self.y == other.y

#     def __gt__(self, other):
#         return self.x > other.x and self.y > other.y


# # point = Point(1, 2)
# point = Point(10, 20)
# other = Point(1, 2)

# # False because it compares the references or addresses in memory
# # True if we have defined __eq__ within Point
# print(point == other)
# print(point > other)


# * Performing Arithmatic Operations

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __add__(self, other):
#         return Point(self.x + other.x, self.y + other.y)


# point = Point(10, 20)
# other = Point(1, 2)
# combined = point + other
# print(combined.x)


# * Making Custom Containers

# class TagCloud:
#     def __init__(self):
#         self.tags = {}

#     def add(self, tag):
#         self.tags[tag.lower()] = self.tags.get(tag.lower(), 0) + 1

#     def __getitem__(self, tag):
#         return self.tags.get(tag.lower(), 0)

#     def __setitem__(self, tag, count):
#         self.tags[tag.lower()] = count

#     def __len__(self):
#         return len(self.tags)

#     def __iter__(self):
#         return iter(self.tags)


# cloud = TagCloud()
# cloud["python"] = 10
# len(cloud)
# cloud.add("Python")
# cloud.add("pyThon")
# cloud.add("pythOn")
# print(cloud.tags)


# * Private Members

# class TagCloud:
#     def __init__(self):
#         self.__tags = {}

#     def add(self, tag):
#         self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1

#     def __getitem__(self, tag):
#         return self.__tags.get(tag.lower(), 0)

#     def __setitem__(self, tag, count):
#         self.__tags[tag.lower()] = count

#     def __len__(self):
#         return len(self.__tags)

#     def __iter__(self):
#         return iter(self.__tags)


# cloud = TagCloud()
# print(cloud.__dict__)
# print(cloud._TagCloud__tags)


# * Properties

# class Product:
#     def __init__(self, price):
#         # self.__price = price
#         # self.set_price(price)
#         self.price = price

#     @property
#     def price(self):
#         return self.__price

#     @price.setter
#     def price(self, value):
#         if value < 0:
#             raise ValueError("Price cannot be negative.")
#         self.__price = value

#     # price = property(get_price, set_price)


# # product = Product(-50)
# product = Product(10)
# # product.price = -1
# print(product.price)


# * Inheritance

# class Animal:
#     def __init__(self):
#         self.age = 1

#     def eat(self):
#         print("eat")


# class Mammal(Animal):
#     def walk(self):
#         print("walk")


# class Fish(Animal):
#     def swim(self):
#         print("swim")


# m = Mammal()
# m.eat()

# print(m.age)


# * The Object Class

# # class Animal(object): # All classes are derived from object class
# class Animal:
#     def __init__(self):
#         self.age = 1

#     def eat(self):
#         print("eat")


# class Mammal(Animal):
#     def walk(self):
#         print("walk")


# m = Mammal()
# print(isinstance(m, Mammal))
# print(isinstance(m, Animal))
# print(isinstance(m, object))
# o = object()
# print(issubclass(Mammal, Animal))
# print(issubclass(Mammal, object))


# * Method Overriding

# class Animal:
#     def __init__(self):
#         print("Animal Constructor")
#         self.age = 1

#     def eat(self):
#         print("eat")


# class Mammal(Animal):
#     def __init__(self):
#         print("Mammal Constructor")
#         self.weight = 2
#         super().__init__()

#     def walk(self):
#         print("walk")


# m = Mammal()
# print(m.age)
# print(m.weight)


# * Multi-level Inheritance

# class Animal:
#     def eat(self):
#         print("eat")


# class Bird(Animal):
#     def fly(self):
#         print("fly")


# class Chicken(Bird):  # But a chicken cant fly
#     pass


# * Multiple Inheritance

# # Bad Inheritance
# class Employee:
#     def greet(self):
#         print("Employee Greet")


# class Person:
#     def greet(self):
#         print("Person Greet")


# class Manager(Employee, Person):
#     pass


# manager = Manager()
# manager.greet()

# # Good Inheritance


# class Flyer:
#     def fly(self):
#         pass


# class Swimmer:
#     def swim(self):
#         pass


# class FlyingFish(Flyer, Swimmer):
#     pass


# * A Good Example of Inheritance

# class InvalidOperationError(Exception):
#     pass


# class Stream:
#     def __init__(self):
#         self.opened = False

#     def open(self):
#         if self.opened:
#             raise InvalidOperationError("Stream is already open.")
#         self.opened = True

#     def close(self):
#         if not self.opened:
#             raise InvalidOperationError("Stream is already closed.")
#         self.opened = False


# class FileStream(Stream):
#     def read(self):
#         print("Reading data from a file.")


# class NetworkStream(Stream):
#     def read(self):
#         print("Reading data from a network.")


# * Abstract Base Classes

from abc import ABC, abstractmethod


class InvalidOperationError(Exception):
    pass


class Stream(ABC):
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOperationError("Stream is already open.")
        self.opened = True

    def close(self):
        if not self.opened:
            raise InvalidOperationError("Stream is already closed.")
        self.opened = False

    @abstractmethod
    def read(self):
        pass


class FileStream(Stream):
    def read(self):
        print("Reading data from a file.")


class NetworkStream(Stream):
    def read(self):
        print("Reading data from a network.")


class MemoryStream(Stream):  # This now requires the read method
    def read(self):
        print("Reading data from a memory stream.")


# stream = Stream()  # Stream shoud only be an abstract base class
# stream = open()
stream = MemoryStream()
