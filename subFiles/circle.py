import json
import subFiles.classes as cl
import subFiles.input_functions as IFC
import os
import math as m
from math import degrees, sin, asin, radians, pi, sqrt


def circumference_calculator(c):
    c.radius = c.circumference/(2*pi)
    c.area = pi*(c.radius**2)
    return c

def area_calculator(c):
    c.radius = sqrt(c.area/pi)
    c.area = pi*(c.radius**2)
    return c

def radius_calculator(c):
    c.area = c.radius**2 * pi
    c.circumference = c.radius*2*pi
    return c

def circle_input():
    os.system("cls")
    c = cl.Circle(
        radius= IFC.text_to_int(input("radius :")),
        circumference=IFC.text_to_int(input("circumference :")),
        area=IFC.text_to_int(input("area :"))
    )

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
    c.print()
    input()
