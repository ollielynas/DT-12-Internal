import json
import subFiles.classes as cl
import subFiles.input_functions as IFC
import os
import math as m
from math import degrees, sin, asin, radians


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

def sin_rule(t):
    la = [t.A, t.B, t.C, t.A, t.B, t.C] # angle list
    ld = [t.a, t.b, t.c, t.a, t.b, t.c] # length list
    for x in la:
        if type(x) == int:
            x = radians(x)
            print(x)
    
    for i in range(0,3):
        a = ld[i]
        b = ld[i+1]
        c = ld[i+2]
        A = la[i]
        B = la[i+1]
        C = la[i+2]
        
        if type(b) == type(A) == type(B):
            a = b*(sin(A)/sin(B))
            print(a)

    # for x in la:
    #     if type(x) == int:
    #         print("deg:",x,degrees(x))
    #         la[la.index(x)] = degrees(x)
            
        
    print(la,ld)
    return t


def calculate_triangle(tri):
    for _ in range(20):
        values = pythagoras(tri.a, tri.b, tri.c)
        tri.a, tri.b, tri.c = values[0], values[1], values[2]
        
        values = angle_sum(tri.A, tri.B, tri.C)
        tri.A, tri.B, tri.C = values[0], values[1], values[2]
        
        tri = sin_rule(tri)


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
