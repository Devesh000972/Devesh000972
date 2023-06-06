import pyautogui
import time

# Open web browser and navigate to website
pyautogui.press('winleft')
pyautogui.write('chrome')
pyautogui.press('enter')
time.sleep(2)
pyautogui.write('https://www.example.com')
pyautogui.press('enter')
time.sleep(5)

# Click button on the webpage
button_pos = pyautogui.locateOnScreen('button.png')
button_center = pyautogui.center(button_pos)
pyautogui.click(button_center)
