import sys
import pydirectinput
import time

s = sys.argv[1]

if s != "":
    while True:
        pydirectinput.keyDown(s)