import PySimpleGUI as sg
import keyboard
import mouse
import pydirectinput
import time
import subprocess

nutbam = ""
toado = []  
status = False
bg = "#d9534f"  # đỏ nhạt kiểu Win10 khi tắt

def toggle_status():
    global status
    status = not status
    if status:
        subprocess.Popen(["uTorrent.exe", str(toado)])
        subprocess.Popen(["WinSplit.exe", nutbam])
    else:
        list_task = subprocess.run("tasklist", capture_output=True, text=True)
        if "uTorrent.exe" in list_task.stdout:
            subprocess.run("taskkill /F /IM uTorrent.exe")
        if "WinSplit.exe" in list_task.stdout:
            subprocess.run("taskkill /F /IM WinSplit.exe")

# ---------------- UI Styling ----------------
sg.theme("DarkGrey13")  # dark mode hiện đại
font_title = ("Segoe UI", 10, "bold")
font_text = ("Segoe UI", 9)

# custom titlebar chỉ hiển thị tên
custom_titlebar = [
    sg.Text(" UniKeyNT 2.0 :)))", font=("Segoe UI", 10, "bold"), text_color="white", background_color="#2b2b2b", expand_x=True)
]

layout = [
    custom_titlebar,
    [sg.Text("TOOL XỊN RỒI NHÉ!", font=("Segoe UI", 12, "bold"), justification='center', expand_x=True, text_color="white")],
    [sg.Text("Ấn F6 để Bật/Tắt", font=font_title, justification='center', expand_x=True, text_color="#00bfff")],
    [sg.Text("ĐANG TẮT", key='-STATUS-', font=("Segoe UI", 10, "bold"), size=(12,1), justification='center', text_color="white", background_color=bg, relief="ridge", pad=(0,8), expand_x=True)],    
    [sg.Text("Vị trí chuột:", font=font_text, size=(10,1), justification='right', text_color="white"), 
     sg.Multiline("", key='-MOUSE-', size=(12,3), font=font_text, text_color="#00ffcc", background_color="#1e1e1e", no_scrollbar=True, disabled=True, border_width=1, expand_x=True)],
    [sg.Text("Nút bấm:", font=font_text, size=(10,1), justification='right', text_color="white"), 
     sg.Text("", key='-NUT-', font=font_text, text_color="#00ffcc", border_width=1, background_color="#1e1e1e", size=(10,1), expand_x=True, justification='left')],
    [sg.Column([
        [sg.Button("CÀI CHUỘT", key='-CHUOT-', size=(10,1), button_color=("white", "#0078D7")), 
         sg.Button("XÓA", key='-XOACHUOT-', size=(6,1), button_color=("white", "#d9534f"))],
        [sg.Button("CÀI NÚT", key='-NUTBAM-', size=(10,1), button_color=("white", "#0078D7")), 
         sg.Button("XÓA", key='-XOANUT-', size=(6,1), button_color=("white", "#d9534f"))],
        [sg.Button("❌ THOÁT", key='Cancel', size=(16,1), button_color=("white", "#444444"))]
    ], element_justification='center', justification='center', expand_x=True)]
] 

# Frame bao quanh kiểu dark + bo góc mềm
framed_layout = [[sg.Frame("", layout, border_width=2, relief="ridge", background_color="#2b2b2b", element_justification='center', pad=(10,10))]]

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

# nền ngoài đen xám để giả lập bóng + bo góc
window.TKroot.configure(bg="#1a1a1a")
try:
    window.TKroot.overrideredirect(True)  # bỏ viền mặc định
    window.TKroot.wm_attributes("-transparentcolor", "#1a1a1a")  # làm nền ngoài trong suốt
    window.TKroot.update()
    window.TKroot.configure(highlightthickness=0)
except:
    pass

while True:
    event, values = window.read(timeout=100)
    if keyboard.is_pressed('f6'):
        toggle_status()
        time.sleep(0.5)
        if status:
            bg = "#0275d8"  # xanh Win10 khi chạy
            window['-STATUS-'].update("ĐANG CHẠY", background_color=bg)
        else:
            bg = "#d9534f"  # đỏ nhạt khi tắt
            window['-STATUS-'].update("ĐANG TẮT", background_color=bg)            
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
    if event == '-NUTBAM-':
        key_pressed = keyboard.read_event(suppress=True)
        if key_pressed.event_type == keyboard.KEY_DOWN:
            nutbam = key_pressed.name
            nutbamH = nutbam.upper()  # hiển thị chữ in hoa
            window['-NUT-'].update(nutbamH)
    if event == '-XOANUT-':
        nutbam = ""
        window['-NUT-'].update(nutbam)
    if event == '-CHUOT-':
        mouse.wait(button="left", target_types=("down",))
        toadomoi = (mouse.get_position()[0], mouse.get_position()[1])
        toado.append(toadomoi)
        # Xuống dòng mỗi tọa độ và thêm số thứ tự
        toado_text = "\n".join([f"{i+1}. {pos}" for i, pos in enumerate(toado)])
        window['-MOUSE-'].update(toado_text)
    if event == '-XOACHUOT-':
        toado = []
        window['-MOUSE-'].update("")

window.close()
