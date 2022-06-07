import json
import subFiles.classes as cl
import subFiles.input_functions as IFC
import os
import math as m


with open('./text.json') as f:
    text = json.load(f)




# this is the first function i wrote an it will calculate lengths using a**2 + b**2 = c **2
def pythagoras(a,b,c):
        if type(a)==int and type(b)==int:
            c = (a**2 + b**2)**0.5
        if type(c)==int and type(b)==int:
            a = (c**2 - b**2)**0.5
        if type(a)==int and type(c)==int:
            b = (a**2 + c**2)**0.5
        return [a,b,c]


def angle_sum(a,b,c):
        if type(a)==int and type(b)==int:
            c = (180 - a - b)
        if type(c)==int and type(b)==int:
            a = (180 - c - b)
        if type(a)==int and type(c)==int:
            b = (180 - a - c)
        return [a,b,c]

def sin_rule(tri):
    ...


def calculate_triangle(tri):
    for i in range(20):
        values = pythagoras(tri.a, tri.b, tri.c)
        tri.a, tri.b, tri.c = values[0], values[1], values[2]
        
        values = angle_sum(tri.A, tri.B, tri.C)
        tri.A, tri.B, tri.C = values[0], values[1], values[2]


def tri_input():
    print(text["triangle_diagram"])

    triangle = cl.Triangle(
        IFC.text_to_int(input("A (deg): ")),
        IFC.text_to_int(input("B (deg): ")),
        IFC.text_to_int(input("C (deg): ")),
        IFC.text_to_int(input("a (length): ")),
        IFC.text_to_int(input("b: (length): ")),
        IFC.text_to_int(input("c: (length): "))
    )
    
    
    if type(triangle.A) == type(triangle.B) == type(triangle.C) == int and round(triangle.A + triangle.B + triangle.C, 4) != 180:
        os.system("cls")
        input("invalid angles")
        return

    calculate_triangle(triangle)
    triangle.plot()
