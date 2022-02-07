#Initialize!!!
import sys
import time
import threading
import numpy
sys.path.insert(0, '../Secret')
import Location

#### Control Modules ####
import pyautogui
from pynput.mouse import Button, Controller
from pynput import keyboard

#### Image Modules ####
from PIL import Image, ImageGrab
#import cv2
import pytesseract

def on_press(key):
    if key == keyboard.Key.esc:
        print('esc pressed!')
        storyText.close()
        grandmaText.close()
        newsText.close()
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
    global lastStory, lastNews, storyText, grandmaText, newsText
    storyText = open('story.txt', 'a')
    grandmaText = open('grandma.txt', 'a+')
    newsText = open('news.txt', 'a')
    lastStory = ""
    lastNews = ""

#1. Click Big Cookie
def clickCookie():
    while(True):
        mouse.position = cookiePos
        mouse.click(Button.left)
        time.sleep(0.1)


#2. Click Golden Cookie 
#3. Buy Upgrades
def buyUpgrade():
    Screen = ImageGrab.grab()
    cropTop = 112
    cropLeft = 2240
    Screen = Screen.crop((cropLeft, cropTop, 2540, 1430))
    
    pixels = [i for i in Screen.getdata()]
    try :
        pyautogui.click('Upgrade.PNG')
    except:
        if (102, 255, 102) in pixels : #True if exists, False if it doesn't
            upgrades = numpy.argwhere((numpy.array(Screen)==[102, 255, 102]).all(axis=2))
            index = numpy.argmax(upgrades, axis=0)[1]
            mouse.position = (cropLeft + upgrades[index][1], cropTop + upgrades[index][0])
            mouse.click(Button.left)

#4. Read Text
def readStory():
    global lastStory, lastNews
    Screen = ImageGrab.grab()
    Screen = Screen.crop((890, 112, 2100, 200))
    pixels = [i for i in Screen.getdata()]

    if (245, 246, 247) in pixels: #True if pure white text, False if shifting text
        text = pytesseract.image_to_string(Screen, config='-c page_separator="" --psm 7')
        if text[0] == "\"" :
            if text not in grandmaText.readlines() :
                grandmaText.write(text)
        elif text not in (lastStory, lastNews) :
            if text.startswith("News") :
                newsText.write(text)
                lastNews = text
            else :
                print(text.replace("\n", " "))
                storyText.write(text)
                lastStory = text

Initalize()

cookieClicker = threading.Thread(target=clickCookie, daemon=True)
cookieClicker.start()

while(True):
    buyUpgrade()
    readStory()

storyText.close()