import pyautogui
num = int(input())


for i in range(num):
    pyautogui.typewrite('#' * (i + 1))
    pyautogui.press('enter')
