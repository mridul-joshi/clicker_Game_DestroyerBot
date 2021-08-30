import pyautogui as pg
from win32gui import FindWindow, GetWindowRect
window_handle = FindWindow(None, "Kick Ya Chop - Google Chrome")
window_rect = GetWindowRect(window_handle)

# print(window_rect)
x_right = 400 + window_rect[0]
y_right = 500 + window_rect[1]

x_left = window_rect[0]+200
y_left = 500 + window_rect[1]

x = 0
flag = 1
while x < 10:
    if flag == 1:
        pg.moveTo(x_left, y_left, 0)
        flag = 0
    else:
        pg.moveTo(x_right, y_right, 0)
        flag = 1
    pg.click(clicks=5)
    x = x+1
# left click position Point(x=1503, y=579)
# right click position Point(x=1655, y=520)
