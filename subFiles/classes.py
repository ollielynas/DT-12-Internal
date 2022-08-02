import json

import matplotlib.pyplot as mat

with open('./text.json') as f:
    text = json.load(f)
import subFiles.input_functions as IFC

# stores all the relevant data for a triangle
class Triangle:
    def __init__(self, A, B, C, a, b, c):
        self.A = A  # length
        self.B = B  # length
        self.C = C  # length
        self.a = a  # angle
        self.b = b  # angle
        self.c = c  # angle

    def print_self(self):
        d = text["triangle_diagram"]
        d = d.replace("a", "\r|"+str(self.a))
        d = d.replace("b", "\r"+" "*4+str(self.b))
        d = d.replace(" \\ c", str(self.c))
        d = d.replace("A", "\r|"+str(self.A))
        d = d.replace("B", "\r|"+str(self.B))
        d = d.replace("C\\", ""+str(self.C))
        print(d)
        print(f"A:{self.A} B:{self.B} C:{self.C} a:{self.a} b:{self.b} c: {self.c}")

    def plot(self):

        # x = IFC.guaranty_int(self.b) /4
        # y = IFC.guaranty_int(self.a) / 4

        x = 10
        y = 10

        mat.xlim([0, x*6])
        mat.ylim([0, y*7])

        print("float")
        if type(self.a) == float:
            self.a = round(self.a, 4)
        if type(self.b) == float:
            self.b = round(self.b, 2)
        if type(self.c) == float:
            self.c = round(self.c, 2)
        if type(self.A) == float:
            self.A = round(self.A, 2)
        if type(self.B) == float:
            self.B = round(self.B, 2)
        if type(self.C) == float:
            self.C = round(self.C, 2)

        mat.text(x*5, y*3 - 1, str(self.a))
        mat.text(x*3, y-1, str(self.b))
        mat.text(x*3, y*3 + 1, str(self.c))
        mat.text(x*5, y*5, str(self.A))
        mat.text(x*5, y*1, str(self.B))
        mat.text(x*1, y*1-1, str(self.C))

        mat.plot([x, x+4*x], [y, y+4*y])
        mat.plot([x, x+4*x], [y, y])
        mat.plot([x+4*x, x+(4*x)], [y, y+(4*y)])
        mat.show()

# stores the relevant data for a circle
class Circle:
    def __init__(self, radius, circumference, area):
        self.radius = radius
        self.circumference = circumference
        self.area = area

    def print(self):
        print(
            f"radius : {self.radius} \ncircumference : {self.circumference}\narea : {self.area}")
