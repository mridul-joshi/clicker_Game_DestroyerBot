import numpy as np
import cv2 as cv
from time import time
from windowcapture import WindowCapture
from visionTest import Vision1
import pyautogui as pg
from win32gui import FindWindow, GetWindowRect

# testing for fast mouse click to improve the bot
import mouse
from pynput.mouse import Controller, Button
mouse = Controller()

# getting window position  ---   Kick ya chop
window_handle = FindWindow(None, "Kick Ya Chop - Google Chrome")
window_rect = GetWindowRect(window_handle)


# cliclking  positions right
x_right = 400 + window_rect[0]
y_right = 500 + window_rect[1]

# clicking positions left
x_left = window_rect[0]+200
y_left = 500 + window_rect[1]


# creating instance of the WindowCapture class
# WindowCapture.list_window_names()
wincap = WindowCapture('Kick Ya Chop - Google Chrome')  # nod defined
needleLeft = 'leftHat.jpg'
needleRight = 'rightHat.jpg'
vis = Vision1()
loop_time = time()
flag = []
needle = needleLeft
pg.moveTo(x_left, y_left)
switch = 'l'
x = 0

quit = 0
while True:

    screenshot = wincap.getScreenshot()

    # if window name is same like ( frames in our case ) the window will be updated
    #cv.imshow('Frames', screenshot)
    flag = vis.find(screenshot, needle, 0.90, 'points')

    if len(flag):
        quit = 0
        if switch == 'l':
            print('found left needle .........')
            pg.moveTo(x_right, y_right, 0)
            mouse.click(Button.left)
            needle = needleRight
            switch = 'r'
        else:
            print('Found right needle ........')
            pg.moveTo(x_left, y_left, 0)
            mouse.click(Button.left)
            needle = needleLeft
            switch = 'l'

        continue

    else:
        quit = quit + 1
        if quit == 400:
            break

    x = (x+1) % 11
    if x == 10:
        mouse.click(Button.left)
    # calculatinf time of screenshot changing per second
    print('FPS {}' .format(1/(time()-loop_time)))
    loop_time = time()

    # frames per second will be decided by waitkey() parameter 1 means frame will change after 1ms
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break

print('Processed')
