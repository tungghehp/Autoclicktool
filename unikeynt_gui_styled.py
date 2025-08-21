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
            subprocess.run("taskkill /F /IM autoclick.exe")
        if "autopress.exe" in list_task.stdout:
            subprocess.run("taskkill /F /IM autopress.exe")

# ---------------- UI Styling ----------------
sg.theme("DarkBlue3")  # chọn theme hiện đại
font_title = ("Segoe UI", 10, "bold")
font_text = ("Segoe UI", 9)

layout = [
    [sg.Text("TOOL TỰ ĐỘNG", font=("Segoe UI", 12, "bold"), justification='center', expand_x=True, text_color="white")],
    [sg.Text("Ấn F6 để Bật/Tắt", font=font_title, justification='center', expand_x=True, text_color="yellow")],
    [sg.Text("ĐANG TẮT", key='-STATUS-', font=("Segoe UI", 10, "bold"), size=(12,1), justification='center', text_color="white", background_color=bg, relief="ridge", pad=(0,8))],    
    [sg.Text("Vị trí chuột:", font=font_text, size=(10,1)), sg.Multiline(str(toado), key='-MOUSE-', size=(20,1), font=font_text, text_color="cyan", background_color="black", no_scrollbar=True, horizontal_scroll=True, disabled=True, border_width=1)],
    [sg.Text("Nút bấm:", font=font_text, size=(10,1)), sg.Text("", key='-NUT-', font=font_text, text_color="cyan", relief="solid", border_width=1, background_color="#1e1e1e", size=(10,1))],
    [sg.Button("CÀI CHUỘT", key='-CHUOT-', size=(10,1), button_color=("white", "#0078D7")), 
     sg.Button("XÓA", key='-XOACHUOT-', size=(6,1), button_color=("white", "#D70022"))],
    [sg.Button("CÀI NÚT", key='-NUTBAM-', size=(10,1), button_color=("white", "#0078D7")), 
     sg.Button("XÓA", key='-XOANUT-', size=(6,1), button_color=("white", "#D70022"))],
    [sg.Button("❌ THOÁT", key='Cancel', size=(16,1), button_color=("white", "#444444"))]
] 

# Thêm Frame bao quanh để tạo viền + hiệu ứng đổ bóng giả
framed_layout = [[sg.Frame("", layout, border_width=2, relief="ridge", background_color="#2b2b2b")]]

window = sg.Window(
    'Tool Autoclick', 
    framed_layout, 
    no_titlebar=True, 
    grab_anywhere=True, 
    keep_on_top=True,
    element_justification='center',
    finalize=True,
    margins=(5,5),
    use_custom_titlebar=False,
)

# Giả lập đổ bóng bằng cách đặt màu nền window hơi khác màu frame
window.TKroot.configure(bg="#1a1a1a")

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
        window['-MOUSE-'].update(str(toado))
    if event == '-XOACHUOT-':
        toado = []
        window['-MOUSE-'].update("")

window.close()
