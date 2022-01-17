#Initialize!!!
import sys
import time
sys.path.insert(0, '../Secret')
import Location

#### Control Modules ####
import pyautogui
from pynput.mouse import Button, Controller
from pynput import keyboard

#### Image Modules ####
from PIL import Image, ImageGrab
import pytesseract

def on_press(key):
    if key == keyboard.Key.esc:
        print('esc pressed!')
        storyText.close()
        sys.exit()
        return False # Stop listener

def Initalize():
    listener = keyboard.Listener(on_press=on_press)
    global mouse
    mouse = Controller()

    input('Press Enter to Continue!')
    listener.start()

    ## Find Cookie Location
    cookie = Image.open('Cookie.PNG')
    pyautogui.click('Cookie.PNG')
    global cookiePos
    cookiePos = pyautogui.position()

    ##Initalize
    global lastText, storyText
    storyText = open('story.txt', 'a')
    lastText = ""

#1. Click Big Cookie
def clickCookie():
    mouse.position = cookiePos
    mouse.click(Button.left)


#2. Click Golden Cookie 
#3. Buy Upgrades
#4. Read Text
def readStory():
    global lastText
    Screen = ImageGrab.grab()
    Screen = Screen.crop((890, 112, 2100, 200))
    pixels = [i for i in Screen.getdata()]

    if (245, 246, 247) in pixels: #True if exists, False if it doesn't
        text = pytesseract.image_to_string(Screen, config='-c page_separator="" --psm 7')
        if text != lastText :
            print(text.replace("\n", " "))
            storyText.write(text)
            lastText = text

Initalize()

while(True):
    clickCookie()
    readStory()

storyText.close()