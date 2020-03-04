# -*- coding: utf-8 -*-
import random
import time

import pyautogui
from pyautogui import FailSafeException

pyautogui.PAUSE = 1


def start():
    try:
        print('请在倒计时内选中需要保持活动的窗口')
        for i in range(5):
            print(5 - i)
            time.sleep(1)
        print('移动鼠标到屏幕边角以退出程序')
        while True:
            try:
                key = random.choice(['up', 'down'])
                print('Press', key)
                pyautogui.press(key)
            except FailSafeException:
                print('Show confirm box')
                if pyautogui.confirm(text='Are you sure you want to exit?', title='Confirm Exit',
                                     buttons=['Keep Working!', 'Exit']) == 'Exit':
                    print('Quit by FailSafeCheck')
                    break
    except KeyboardInterrupt:
        print('Quit by KeyboardInterrupt')
