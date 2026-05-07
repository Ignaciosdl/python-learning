# Exercise: Demonstrate polymorphism using shapes.
# Create a base class Shape with an area() method that returns 0.
# Create Circle class (inherits from Shape) that calculates area with π * radius²
# Create Rectangle class (inherits from Shape) that calculates area with width * height
# Create a list with instances of both classes and loop through it calling area() on each.

# Exercise: Demonstrate polymorphism using shapes.
# Create a base class Shape with an area() method that returns 0.
# Create Circle class (inherits from Shape) that calculates area with π * radius²
# Create Rectangle class (inherits from Shape) that calculates area with width * height
# Create a list with instances of both classes and loop through it calling area() on each.

import math # math library for π constant

class Shape: # base class — defines the interface all shapes must implement
    def area(self):
        pass # overridden by each subclass

class Circle(Shape): # inherits from Shape
    def __init__(self, radius):
        self.radius = radius
    
    def area(self): # override Shape.area() with circle formula
        return math.pi * self.radius ** 2
    
    def __str__(self): # string representation of the object
        return f"Circle(radius:{self.radius})" 

class Rectangle(Shape): # inherits from Shape
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self): # override Shape.area() with rectangle formula
        return self.width * self.height

    def __str__(self): # string representation of the object
        return f"Rectangle(width:{self.width}, height:{self.height})"

rectangle = Rectangle(2, 4)
circle = Circle(4)

shapes = [rectangle, circle] # polymorphism — different objects, same interface

for shape in shapes:
    print(f"The area of {shape} is {shape.area():.2f}") # each object responds differently to area()