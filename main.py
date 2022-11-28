import pyautogui
import winsound
import time
from pynput.keyboard import Listener
import os


FOLDER = "C:\\users\\hp\\Desktop\\Screenshot"
if not os.path.exists(FOLDER):
    print("screenshot folder created.")
    os.mkdir(FOLDER)

start = False
shift = False


def beep():
    frequency = 1000  # Set Frequency To 2500 HertzPP
    duration = 100  # Set Duration To 1000 ms == 1 secondPPP
    winsound.Beep(frequency, duration)


def on_press(key):
    global shift, start
    key_press = None
    try:
        shift_key = key.name
        if shift_key == 'shift_r':
            shift = True
    except:
        pass

    try:
        key_press = key.char.lower()
    except:
        pass

    try:
        key = key.vk
    except:
        pass

    if shift and key_press == 'p':
        if not start:
            print("screenshot taker on..........")
            beep()
            start = True
        else:
            start = False
            print("screenshot taker off.")
            beep()
            beep()
    if start:
        if key == 192:
            im=pyautogui.screenshot()
            filename = '\\' + str(time.strftime("%H_%M_%S")) + '.png'
            im.save(FOLDER+filename)


def on_release(key):
    global shift
    try:
        shift_key = key.name
        if shift_key == 'shift_r':
            shift = False
    except:
        pass

with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
