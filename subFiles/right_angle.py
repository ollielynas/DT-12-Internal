import json
import subFiles.classes as cl
import subFiles.input_functions as IFC


with open('./text.json') as f:
    text = json.load(f)




# this is the first function i wrote an it will calculate lengths using a**2 + b**2 = c **2
def pythagoras(a,b,c):
        if type(a)==int and type(b)==int:
            c = (a**2 + b**2)**0.5
        if type(c)==int and type(b)==int:
            a = (c**2 - b**2)**0.5
        if type(a)==int and type(c)==int:
            b = (a**2 + b**2)**0.5
        return [a,b,c]


def tri_input():
    print(text["triangle_diagram"])

    triangle = cl.Triangle(
        IFC.text_to_int(input("A (deg): ")),
        90,
        IFC.text_to_int(input("C (deg):")),
        IFC.text_to_int(input("a (length): ")),
        IFC.text_to_int(input("b: (length)")),
        IFC.text_to_int(input("c: (length)"))
    )
    print(triangle.a)
    triangle.print_self()
    input()


def calculate(tri):
    
    lengths = lengths(tri.a, tri.b, tri.c)