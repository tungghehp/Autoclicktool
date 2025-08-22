import sys
import pydirectinput
import time
import ast

s = sys.argv[1]

if s != []:
    a = ast.literal_eval(s)  # Convert string representation of list to actual list
    while True:
        for (x,y) in a:
            pydirectinput.click(x, y)
            time.sleep(0.5)