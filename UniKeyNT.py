import pyautogui
import pydirectinput
import keyboard
import time
import os

os.system("mode con: cols=30 lines=8")  # Set console size for better visibility
toado = "" #Toa do mac dinh cua chuot"
nutbam = "" #Nut bam mac dinh

def luachonchuot():
    global toado
    os.system ("cls")
    print ("- Ấn X và Enter để chọn\n- Ấn luôn Enter để hủy.")
    xacnhan = input()
    if xacnhan == "x":
        toado = pyautogui.position()
        khoidong()
    if xacnhan == "":
        toado = ""
        khoidong()
    else:
        luachonchuot()
    

def luachonnutbam():
    os.system ("cls")
    global nutbam
    print("- Ấn chữ và Enter để chọn.\n- Ấn luôn Enter để hủy.")
    xacnhan = input()
    if xacnhan == "":
        nutbam = ""
        khoidong()
    if xacnhan == " ":
        nutbam = "space"
        khoidong()
    else:
        nutbam = xacnhan
        khoidong()
    

def khoichay():
    global toado, nutbam
    os.system ("cls")
    print("Click tại:", toado)
    print("Bấm nút:", nutbam)
    print("Ấn ESC để tắt...")
    while True:
        if toado != "":
            pydirectinput.click(toado[0], toado[1])
        if nutbam != "":
            pydirectinput.keyDown(nutbam)
        time.sleep(1)
        if keyboard.is_pressed('esc'):
            print("Đã dừng.")
            khoidong()

def khoidong():
    os.system ("cls")
    print("TOOL GHẺ LỞ CHO A.HƯNG")
    print("Chuột:",toado)
    print("Nút bấm:",nutbam)
    print("1. Đổi vị trí chuột")
    print("2. Đổi nút bấm")
    print("3. Chạy")
    print("Nhập lựa chọn")
    luachon = input()
    if luachon == "1":
        luachonchuot()
    if luachon == "2":
        luachonnutbam()
    if luachon == "3":
        khoichay()
    else:
        khoidong()

khoidong()