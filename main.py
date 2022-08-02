import subFiles.triangle as T
import os
import json
import subFiles.input_functions as IFC
import subFiles.circle as CIR
import sys
from termcolor import colored


with open('./text.json') as f:
    text = json.load(f)


# |---------------------- main menu -----------------------|

# a dict that adds each number input to its own function, for readability. 
# I could have used if statements to do the same thing, but it would be harder to understand and would look messy
calculations = {
    # "index": [function, "description"]
    "1":[T.tri_input, "Right angle triangle calculations"],
    "2": [CIR.circle_input, "Circle calculations"],
    "3":[quit, "Quit"]
}

# here is a almost finished user interface, it uses lists and dicts in order to make it easy
# to add more features and commands, for example if a wanted to add a circle calculator,
# i could simply add it to the dict without having to add code to this loop
# this is to allow for an agile 

def test_equal(x, y, name):
    if x == y:
        print(colored("passed ", "green")+f": {name}")
    else:
        print(colored("failed : ", "red")+f"{name}")

def unittest():
    print("Unit Testing\n==================")
    test_equal(IFC.clean_int_input("3 fdk 4j"), "34", "clean_int_input")
    test_equal(IFC.guaranty_int("123f"), 123, "guaranty int (valid)")
    test_equal(IFC.guaranty_int("e"), 10, "guaranty int (invalid)")
    test_equal(IFC.text_to_int("12k"), 12, "test to int")
    test_equal(IFC.text_to_int("k"), " ? ", "test to int (invalid)")
    test_equal(IFC.text_to_int("9999999999999999999999999999999"), "number too large", "test to int (number too large)")


    quit()


while True:
    if __name__ == '__main__':
        os.system("cls")
        if str(sys.argv).find("test") != -1:
            unittest()
        print(text["intro"])
        for i in calculations.keys():
            print(f"{i}). {calculations[i][1]}")

        index = str(IFC.text_to_int(input("-----|")))
        index.replace("\"", "")

        
        IFC.clean_int_input(index)
        if index in calculations.keys():
            os.system("cls")
            calculations[index][0]()

        else:
            os.system("cls")
            input(text["invalid_index"])
    else:
        quit()

