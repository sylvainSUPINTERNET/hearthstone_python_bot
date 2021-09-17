# python3

import datetime  # работа с датой и времени
import sqlite3  # Импортируем библиотеку, соответствующую типу нашей базы данных
import subprocess  # Запуск приложений windows
import os  # для работы с командной строкой (определение экрана)
import logging  # модуль логирования
import sys
import time  # работа со временем
from datetime import datetime
import random
import keyboard  # работа с нажатиями клавиш
import pyautogui as pg  # работа с картинками


def startlnk():  # функция запуска приложения
    #subprocess.Popen("E:\soft\\battle.net\Battle.net\Battle.net Launcher.exe")
    subprocess.Popen('C:\Program Files (x86)\Battle.net\Battle.net Launcher.exe -w 800 -h 600')  # запуск приложения
    time.sleep(2)  # время ожидания запуска battle.net

def screen_resolution():  # функция определения разрешения экрана
    cmd = 'wmic path Win32_VideoController get CurrentHorizontalResolution,CurrentVerticalResolution'
    size_tuple = tuple(map(int, os.popen(cmd).read().split()[-2::]))
    print(size_tuple)

# описываем параметры логирования
logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')


# примеры логирования с разными уровнями важности
logging.warning('This will get logged to a file')
logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')

# исполняемый код
screen_resolution()  # определяем разрешение экрана
startlnk()  # запуск приложения Battle.net
