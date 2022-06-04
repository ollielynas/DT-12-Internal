

#    |\
#    | \
#    |A \
#    |   \
#    |    \
#   a|     \ c
#    |      \
#    |       \
#    | B    C \
#    |---------\
#         b

from dataclasses import replace
import json
with open('./text.json') as f:
    text = json.load(f)



class Triangle:
    def __init__(self, A, B, C, a, b, c):
        self.A = A
        self.B = B
        self.C = C
        self.a = a
        self.b = b
        self.c = c
    
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
