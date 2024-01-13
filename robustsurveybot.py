import time
import pyautogui
import random

def botmenu():
    print("1. T420 2. Desktop")
    userInt = input(":")
    
    if userInt == "1":
        print("opening firefox")
        click_at_position(85, 745)
        pyautogui.press('f11')  # Press F11 after the first click
        time.sleep(6)
        click_at_position(454, 65)
        print("opening surveyjunkie")
        time.sleep(6)
        keyboard_input = "https://www.surveyjunkie.com/member#!cp"
        type_keyboard_input(keyboard_input)
        time.sleep(6)
        click_at_position(853, 268)
        time.sleep(6)
        click_at_position(1312, 15)
        time.sleep(6)
        click_at_position(619, 393)
        time.sleep(6)
        userInt = input("Press Y when ready to start random clicking")
        # Click randomly in a loop
    loopStart = True
    if userInt == "y":
        while loopStart ==True:
            click_randomly()
    elif userInt =="N":
        while loopStart ==False:
            click_randomly()

def click_at_position(x, y):
    pyautogui.click(x, y)
    time.sleep(1)

def type_keyboard_input(text):
    pyautogui.typewrite(text)
    time.sleep(0.5)
    pyautogui.press('enter')
    time.sleep(1)

def click_randomly():
    start_x, start_y = 100, 490
    click_interval = 0.5

    x = start_x + random.randint(0, 3) * 300
    y = start_y + random.randint(0, 10) * 300
    y = max(100, min(y, 600))
    click_at_position(x, y)
    time.sleep(click_interval)

if __name__ == "__main__":
    botmenu()