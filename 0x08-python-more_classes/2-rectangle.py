#!/usr/bin/python3
Rectangle = __import__('2-rectangle')Rectangle

my_rectangle = rectangle(2, 4)
print("Area: {} - perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))

print("--")

my_rectangle.width = 10 
my_rectangle.height = 3
print("Area: {} - perimeter: {}.format(my_rectangle.area(), my rectangle.perimeter()))
