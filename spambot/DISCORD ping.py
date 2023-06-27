import pyautogui , time

name = input("enter annoying person:")

time.sleep(5)

g = True
while g is True:
    pyautogui.typewrite(name)
    pyautogui.press("enter")
    pyautogui.press("enter")
    time.sleep(3)
    pyautogui.press('up')
    pyautogui.press( "backspace")
    pyautogui.press("enter")
    pyautogui.press("enter")
    time.sleep(5)