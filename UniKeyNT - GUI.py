import PySimpleGUI as sg
import keyboard
import mouse
import pydirectinput
import time
import subprocess

nutbam = ""
toado = []  
status = False
bg = "red"

def toggle_status():
    global status
    status = not status
    if status:
        subprocess.Popen(["autoclick.exe", str(toado)])
        subprocess.Popen(["autopress.exe", nutbam])
    else:
        list_task = subprocess.run("tasklist", capture_output=True, text=True)
        if "autoclick.exe" in list_task.stdout:
            print("Đã tắt autoclick")
            subprocess.run("taskkill /F /IM autoclick.exe")
        if "autopress.exe" in list_task.stdout:
            print("Đã tắt autopress")
            subprocess.run("taskkill /F /IM autopress.exe")
        


layout = [  
        [sg.Text(text="ẤN F6 ĐỂ BẬT/TẮT", text_color='black', justification='center')],
        [sg.Text("ĐANG TẮT", key='-STATUS-', background_color=bg)],    
        [sg.Text("Vị trí chuột:"), sg.Text(str(toado), key='-MOUSE-', size=(10, None))],
        [sg.Text("Nút bấm:"), sg.Text("", key='-NUT-')],
        [sg.Button("CÀI CHUỘT", key='-CHUOT-'), sg.Button("XÓA", key='-XOACHUOT-'), ],
        [sg.Button('CÀI NÚT', key='-NUTBAM-'), sg.Button("XÓA", key='-XOANUT-')],
        [sg.Button('THOÁT TOOL', key='Cancel')]
] 

# Create the Window
window = sg.Window('TOOL GHẺ', layout, no_titlebar=True, grab_anywhere=True, keep_on_top=True)

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read(timeout=100)
    if keyboard.is_pressed('f6'):
        toggle_status()
        time.sleep(0.5)
        if status:
            bg = "green"
            window['-STATUS-'].update("ĐANG CHẠY", background_color=bg)
        else:
            bg = "red"
            window['-STATUS-'].update("ĐANG TẮT", background_color=bg)            
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
    if event == '-NUTBAM-':
        key_pressed = keyboard.read_event(suppress=True)
        if key_pressed.event_type == keyboard.KEY_DOWN:
            nutbam = key_pressed.name
            window['-NUT-'].update(nutbam)
    if event == '-XOANUT-':
        nutbam = ""
        window['-NUT-'].update(nutbam)
    if event == '-CHUOT-':
        mouse.wait(button="left", target_types=("down",))
        toadomoi = (mouse.get_position()[0], mouse.get_position()[1])
        toado.append(toadomoi)
        print(toado)
        window['-MOUSE-'].update(toado)
    if event == '-XOACHUOT-':
        toado = []
        window['-MOUSE-'].update(toado)

window.close()
