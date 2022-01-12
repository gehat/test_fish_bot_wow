import time
import numpy as np
import pyautogui
from PIL import ImageGrab
import cv2
average = [0, ]
flag = 0
## изображение таргета пополовка
target = cv2.imread('/Users/jamem/Desktop/bot/1.png', 0)
width, height = target.shape[::-1]
# Скиншот окна игры
for i in range(80):
    screen = ImageGrab.grab(bbox=(0, 0, 1200, 950))
    screen.save('/Users/jamem/Desktop/bot/screenshot.png')
    ##Преобразование пнг картинки в формат читаемый библиотекой CV2
    image_rgb = cv2.imread('/Users/jamem/Desktop/bot/screenshot.png')
    image_gray = cv2.cvtColor(image_rgb, cv2.COLOR_BGR2GRAY)
    # Поиск координат шаблона на базовом скрине c погрешностью 0.7
    res = cv2.matchTemplate(image_gray, target, cv2.TM_CCOEFF_NORMED)
    location = np.where(res >= 0.6)
    for i in range(40):
        for poz in zip(*location[::-1]):
            x = int(poz[0])
            y = int(poz[1])
            clean_screen = ImageGrab.grab(bbox=(x, y, x + width, y + height))
            mean = np.mean(clean_screen)
            diff = average[-1] - mean
            print(average[-1] - mean)
            average.append(mean)
            if diff >= 3:
                print("Поплавок найден")
                pyautogui.moveTo(x + 15, y + 15)
                pyautogui.rightClick()
                average = [0, ]
                flag = 1
                del (x)
                del (y)
                pyautogui.press('q')
                pyautogui.moveTo(200,200)
                time.sleep(1)
                break
            del (x)
            del (y)
            time.sleep(0.3)
        if flag == 1:
            flag=0
            time.sleep(1)
            break

    average = [0, ]
