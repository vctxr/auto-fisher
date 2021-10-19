import pyautogui            # pip install pyautogui
import win32api, win32con
import time
import keyboard             # pip install 
import random

# NOTE: ADJUST THESE 4 VALUES ACCORDING TO YOUR SETUP
# TO FIND OUT THIS VALUES UNCOMMENT THIS CODE TO CHECK THE BUTTON POSITION
# AND TRIGGER COLOR
# pyautogui.displayMousePosition()

width, height = 50, 50          # scan area
x_offset, y_offset = 680, 340   # offset from the top left corner
trigger_color = (172, 231, 92)  # RGB color
color_range = 15                # acceptable color range

def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(.01) # delay the key up to ensure click is registered correctly
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

print('AUTO FISHER STARTED')
print('>> PRESS Q TO STOP')

def find_color(pixel_color, acceptable_range, picture, width, height):
    for x in range(0, width):
        for y in range(0, height):
            r, g, b = picture.getpixel((x, y))

            # RGB value checking in certain `acceptable` range
            if (r in range(pixel_color[0] - acceptable_range, pixel_color[0] + acceptable_range) and 
                g in range(pixel_color[1] - acceptable_range, pixel_color[1] + acceptable_range) and 
                b in range(pixel_color[2] - acceptable_range, pixel_color[2] + acceptable_range)):
                    return x, y

    # iterated through all the pixels and no matching color found
    return None, None

iteration = 0
last_x = None
last_y = None

while not keyboard.is_pressed('q'):
    iteration = (iteration + 1) % 1000
    picture = pyautogui.screenshot(region=(x_offset, y_offset, width, height))

    # returns true if the given trigger color exists in the given picture
    x, y = find_color(trigger_color, color_range, picture, width, height)

    if x != None and y != None:
        print(f'Button found at ({x}, {y}), iteration = {iteration}')
        iteration = 0
        last_x, last_y = x, y

        time.sleep(random.uniform(0, 0.3)) # introduce a delay to remove any repetitive patterns that the game may detect.
        click(x_offset + x + random.randint(20, 50), y_offset + random.randint(20, 50))
        time.sleep(3.5 + random.uniform(0, 2))   # delay to cast another fishing rod
        click(x_offset + x + random.randint(20, 50), y_offset + y + random.randint(20, 50))

    # fallback if target color not found
    if iteration > 200 and last_x != None and last_y != None:
        iteration = 0
        print("Fallback triggered!")
        click(x_offset + last_x, y_offset + last_y)
