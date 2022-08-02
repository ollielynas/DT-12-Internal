import json
import subFiles.classes as cl
import subFiles.input_functions as IFC
import os
from math import sin, acos, pi

# loads json file
with open('./text.json') as f:
    text = json.load(f)


def angle(a, b, c):
    return(acos((c**2 - b**2 - a**2)/(-2.0 * a * b)))


# this is the first function I wrote an it will calculate lengths using a**2 + b**2 = c **2
def pythagoras(a, b, c):
    if type(a) != str and type(b) != str and type(c) == str:
        c = (a**2 + b**2)**0.5
    if type(c) != str and type(b) != str and type(a) == str:
        a = (c**2 - b**2)**0.5
    if type(a) != str and type(c) != str and type(b) == str:
        b = (c**2 - a**2)**0.5
    return [a, b, c]

# finds missing angles by knowing that all angles must sum to pi


def angle_sum(a, b, c):
    if type(a) != str and type(b) != str:
        c = (pi - a - b)
    if type(c) != str and type(b) != str:
        a = (pi - c - b)
    if type(a) != str and type(c) != str:
        b = (pi - a - c)
    return [a, b, c]


# uses the sin rule to solve for missing sides
def sin_rule(t):
    # return t
    la = [t.A, t.B, t.C, t.A, t.B, t.C]  # angle list
    ld = [t.a, t.b, t.c, t.a, t.b, t.c]  # length list

    # this loop is the equivalent of rotating the triangle
    for i in range(0, 3):
        a = ld[i]
        b = ld[i+1]
        c = ld[i+2]
        A = la[i]
        B = la[i+1]
        C = la[i+2]
        if type(b) != str and type(A) != str and type(B) != str and type((b*sin(A))/sin(B)) != complex:
            e = (b*sin(A))/sin(B)
            if i == 0:
                t.a = e
            elif i == 1:
                t.b = e
            elif i == 2:
                t.c = e

    return t

# call all the relevant function to calculate the triangle


def calculate_triangle(tri):
    for _ in range(10):
        values = pythagoras(tri.a, tri.b, tri.c)
        tri.a, tri.b, tri.c = values[0], values[1], values[2]

        values = angle_sum(tri.A, tri.B, tri.C)
        tri.A, tri.B, tri.C = values[0], values[1], values[2]

        tri = sin_rule(tri)
        if type(tri.b) != str and type(tri.a) != str and type(tri.c) != str:
            try:
                tri.A = angle(tri.a, tri.b, tri.c)
                tri.B = angle(tri.b, tri.c, tri.a)
                tri.C = angle(tri.c, tri.a, tri.b)
            except:
                ...


def tri_input():
    print(text["triangle_diagram"])

    triangle = cl.Triangle(
        IFC.text_to_int(input("A (rad): ")),
        IFC.text_to_int(input("B (rad): ")),
        IFC.text_to_int(input("C (rad): ")),
        IFC.text_to_int(input("a (length): ")),
        IFC.text_to_int(input("b: (length): ")),
        IFC.text_to_int(input("c: (length): "))
    )

    if type(triangle.A) == type(triangle.B) == type(triangle.C) and type(triangle.C) != str and round(triangle.A + triangle.B + triangle.C, 4) >= pi:
        os.system("cls")
        input("invalid angles")
        return


    # the next three statements check that all inputted angles are < pi
    if type(triangle.A) != str:
        if triangle.A > pi or triangle.A <= 0:
            os.system("cls")
            input("invalid angles")
            return

    if type(triangle.B) != str:
        if triangle.B > pi or triangle.B <= 0:
            os.system("cls")
            input("invalid angles")
            return

    if type(triangle.C) != str:
        if triangle.C > pi or triangle.C <= 0:
            os.system("cls")
            input("invalid angles")
            return

    calculate_triangle(triangle)
    triangle.plot()
