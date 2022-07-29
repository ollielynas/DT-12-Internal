import subFiles.classes as cl
import subFiles.input_functions as IFC
import os
from math import pi, sqrt

# find circumference of circle


def circumference_calculator(c):
    c.radius = c.circumference/(2*pi)
    c.area = pi*(c.radius**2)
    return c

# find area of a circle


def area_calculator(c):
    c.radius = sqrt(c.area/pi)
    c.area = pi*(c.radius**2)
    return c

# find radius using circumference and area


def radius_calculator(c):
    c.area = c.radius**2 * pi
    c.circumference = c.radius*2*pi
    return c

# input known values for circle


def circle_input():
    os.system("cls")
    print("if you do not know a value simply leave it blank")
    c = cl.Circle(
        radius=IFC.text_to_int(input("radius :")),
        circumference=IFC.text_to_int(input("circumference :")),
        area=IFC.text_to_int(input("area :"))
    )

    # checks if the inputted values can be used to make a valid circle
    if type(c.radius) != str and type(c.area) != str:
        if c.area != pi*c.radius**2:
            os.system("cls")
            input("conflicting info")
            return

    if type(c.radius) != str and type(c.circumference) != str:
        if c.area != pi*c.radius*2:
            os.system("cls")
            input("conflicting info")
            return

    if type(c.area) != str and type(c.circumference) != str:
        if c.area != pi*(c.circumference/pi/2)**2:
            os.system("cls")
            input("conflicting info")
            return

    for _ in range(6):

        if type(c.circumference) != str:
            c = circumference_calculator(c)
        if type(c.area) != str:
            c = area_calculator(c)
        if type(c.radius) != str:
            c = radius_calculator(c)
    os.system("cls")
    c.print()
    input()
