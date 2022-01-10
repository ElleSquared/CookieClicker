#Initialize!!!
import sys
import time

#### Control Modules ####
import pyautogui
from pynput.mouse import Button, Controller
from pynput import keyboard

#### Image Modules ####
from PIL import Image



def on_press(key):
    if key == keyboard.Key.esc:
         print('esc pressed!')
         sys.exit()
         return False # Stop listener

listener = keyboard.Listener(on_press=on_press)
mouse = Controller()

input('Press Enter to Continue!')
listener.start()
#1. Click Big Cookie
cookie=Image.open('Cookie.PNG')

## Find Cookie Location
pyautogui.click('Cookie.PNG')
cookiePos = pyautogui.position()

while(True):
    ## Click Cookie
    mouse.position = cookiePos
    mouse.click(Button.left)


#2. Click Golden Cookie 
#3. Buy Upgrades
#4. Read Text