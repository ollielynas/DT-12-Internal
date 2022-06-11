import subFiles.triangle as T
import os
import sys
import unit_tests as ut
import json
import subFiles.input_functions as IFC

with open('./text.json') as f:
    text = json.load(f)





# |---------------------- main menu -----------------------|

# a dict that adds each number input to its own function, for readability. 
# I could have used if statements to do the same thing, but it would be harder to understand and would look messy
calculations = {
    # "index": [function, "description"]
    "1":[T.tri_input, "Right angle triangle calculations"],
}


# here is a almost finished user interface, it uses lists and dicts in order to make it easy
# to add more features and commands, for example if a wanted to add a circle calculator,
# i could simply add it to the dict without having to add code to this loop

while True:
    if __name__ == '__main__':
        os.system("cls")
        print(text["intro"])
        for i in calculations.keys():
            print(f"{i}). {calculations[i][1]}")

        index = input("-----|")
        index.replace("\"", "")
        if index.lower().replace(" ","") == "q":
            quit()
        
        IFC.clean_int_input(index)
        if index in calculations.keys():
            os.system("cls")
            calculations[index][0]()

        else:
            input(text["invalid_index"])
    else:
        print(f"invalid args {__name__}")
        quit()