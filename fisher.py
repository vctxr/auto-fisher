import pyautogui            # pip install pyautogui
import win32api, win32con
import time
import keyboard             # pip install keyboard

# NOTE: ADJUST THESE 2 VALUES ACCORDING TO YOUR SETUP
# TO FIND OUT THIS VALUES UNCOMMENT THIS CODE TO CHECK THE BUTTON POSITION
# AND TRIGGER COLOR
button_pos = (784, 377) # XY position of the fishing button
trigger_color = (156, 209, 100) # RGB
color_range = 50

def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(.01) # delay the key up to ensure click is registered correctly
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

while not keyboard.is_pressed('q'):
    pixel = pyautogui.pixel(button_pos[0], button_pos[1])

    # RGB value checking in certain `acceptable` range
    if (pixel[0] in range(trigger_color[0] - color_range, trigger_color[0] + color_range) and 
        pixel[1] in range(trigger_color[1] - color_range, trigger_color[1] + color_range) and 
        pixel[2] in range(trigger_color[2] - color_range, trigger_color[2] + color_range)):

        click(button_pos[0], button_pos[1])
        time.sleep(4)   # delay to cast another fishing rod
        click(button_pos[0], button_pos[1])
