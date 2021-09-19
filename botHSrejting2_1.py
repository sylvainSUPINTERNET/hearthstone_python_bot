# python3
# bot for hearthstoune rejting game

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
    subprocess.Popen('C:\Program Files (x86)\Battle.net\Battle.net Launcher.exe')  # запуск приложения
    time.sleep(10)  # время ожидания запуска battle.net
    keyboard.send("windows+up")  # разворачивает приложение на все окно

def screen_resolution():  # функция определения разрешения экрана
    global screen_width_x, screen_height_y
    cmd = 'wmic path Win32_VideoController get CurrentHorizontalResolution,CurrentVerticalResolution'
    size_tuple = tuple(map(int, os.popen(cmd).read().split()[-2::]))
    screen_width_x = size_tuple[0]
    screen_height_y = size_tuple[1]
    logging.info('%s screen width', screen_width_x)  # запись в лог файл ширины экрана
    logging.info('%s screen height', screen_height_y)  # запись в лог файл высоты экрана
    return screen_width_x, screen_height_y  # возвращение глобальных переменных

def ss(template):  # функция определения и двойного нажатия на координаты кнопки
    global zero, activity, screen_width_x, screen_height_y
    try:
        buttonx, buttony = pg.locateCenterOnScreen(template, region=(0, 0, screen_width_x, screen_height_y), confidence=0.7)
        activity = time.time()
        pg.moveTo(buttonx, buttony)
        pg.doubleClick(buttonx, buttony)
        time.sleep(1)
        return activity
    except TypeError:
        return zero

def pointclick():  # функция произвольного нажатия в цикле
    global screen_width_x, screen_height_y
    pg.doubleClick(screen_width_x * 0.95, screen_height_y * 0.1)

def hero_strength(template):  # функция силы героя
    global zero, activity, screen_width_x, screen_height_y
    try:
        buttonx, buttony = pg.locateCenterOnScreen(template, region=(0, screen_height_y * 0.8, screen_width_x, screen_height_y * 0.2), confidence=0.7)
        activity = time.time()
        pg.moveTo(buttonx, buttony)
        pg.doubleClick(buttonx, buttony)
        time.sleep(1)
        return activity
    except TypeError:
        return zero

def simple_press(template):  # функция одинарного нажатия
    global activity, zero, screen_width_x, screen_height_y
    try:
        buttonx, buttony = pg.locateCenterOnScreen(template, region=(0, 0, screen_width_x, screen_height_y), confidence=0.7)
        activity = time.time()
        pg.moveTo(buttonx, buttony)
        pg.click(buttonx, buttony)
        time.sleep(1)
        pg.moveTo(screen_width_x * 0.95, screen_height_y * 0.1)
        return activity
    except TypeError:
        return zero

def card_selection(template):  # функция выбора стартовой руки
    global activity, screen_width_x, screen_height_y
    try:
        buttonx, buttony = pg.locateCenterOnScreen(template, region=(0, screen_height_y * 0.6, screen_width_x * 0.7, screen_height_y * 0.4), confidence=0.7)
        pg.moveTo(buttonx, buttony)
        time.sleep(13)
        pg.click(buttonx, buttony)
        activity = time.time()
        return activity
    except TypeError:
        return zero

def start_game(template):
    global hod
    global Gcikl
    global Ggame
    global cikl
    global vygr
    global progr
    global zero
    global vygr
    global progr
    global activity, screen_width_x, screen_height_y
    try:
        buttonx, buttony = pg.locateCenterOnScreen(template, region=(screen_width_x * 0.7, screen_height_y * 0.6, screen_width_x * 0.3, screen_height_y * 0.4), confidence=0.7)
        pg.moveTo(buttonx, buttony)
        Gcikl += 1
        hod = 1
        Ggame = 1
        cikl = 0
        vygr = 0
        progr = 0
        activity = time.time()
        time.sleep(1)
        return hod, Gcikl, Ggame, cikl, vygr, progr, activity
    except TypeError:
        return zero

def vash_hod(template):
    global game  # индикатор своего хода
    global zero
    global activity, screen_width_x, screen_height_y
    try:
        buttonx, buttony = pg.locateCenterOnScreen(template, region=(0, 0, screen_width_x, screen_height_y), confidence=0.7)
        if game == 0:
            game = 1
            # print("Старт хода")
            pg.moveTo(buttonx, buttony, duration=0)
            activity = time.time()
            time.sleep(1)
            pg.moveTo(screen_width_x * 0.95, screen_height_y * 0.1)
            return game, activity
    except TypeError:
        return zero

def chughoj_hod(template):
    global game
    global unit
    global hod
    global mana
    global zero
    global activity, screen_width_x, screen_height_y
    try:
        buttonx, buttony = pg.locateCenterOnScreen(template, region=(0, 0, screen_width_x, screen_height_y), confidence=0.7)
        pg.moveTo(buttonx, buttony)
        # print(buttonx, buttony)
        if game == 1:
            hod += 1
            game = 0
            unit = 0
        # print("Ход противника")
        activity = time.time()
        time.sleep(5)
        pg.moveTo(screen_width_x * 0.95, screen_height_y * 0.1)
        if hod < 11:
            mana = hod
        elif hod >= 11:
            mana = 10
        return game, unit, hod, mana, activity
    except TypeError:
        return zero


def karta(template):  # функция покупки юнита
    global zero
    global unit
    global hod
    global game
    global moneta
    global mana
    global activity, screen_width_x, screen_height_y
    try:
        buttonx, buttony = pg.locateCenterOnScreen(template, region=(0, screen_height_y * 0.6, screen_width_x * 0.9, screen_height_y * 0.4), confidence=0.7)
        pg.moveTo(buttonx, buttony)
        activity = time.time()
        # print('Нашел карту', buttonx, buttony)
        # print("unit", unit)
        # print("hod", hod)
        pg.press(['right'])
        if hod == 4 and unit == 0:
            moneta = 1
            # print("Выложил монету на стол")
            pg.moveTo(buttonx, buttony, duration=0)  # перемещение к кнопке
            pg.mouseDown(button='left')  # нажать левую клавишу мыши
            pg.moveTo(screen_width_x / 2, screen_height_y / 2, duration=1)  # перемещение
            pg.mouseUp(button='left')  # отпустить левую клавиши мыши
            unit = 1
        if unit == 0 and hod > 3 and game == 1 and mana >= 5:
            # print("Выложил одну карту на стол")
            pg.moveTo(buttonx, buttony, duration=0)  # перемещение к кнопке
            pg.mouseDown(button='left')  # нажать левую клавишу мыши
            pg.moveTo(screen_width_x / 2, screen_height_y / 2, duration=1)  # перемещение
            pg.mouseUp(button='left')  # отпустить левую клавиши мыши
            pg.moveTo(buttonx, buttony, duration=0)
            unit += 1
        return unit, hod, game, moneta, mana, activity
    except TypeError:
        return zero


def health(template):  # функция лечения
    global zero, activity, screen_width_x, screen_height_y
    try:
        buttonx, buttony = pg.locateCenterOnScreen(template, region=(screen_width_x * 0.5, screen_height_y * 0.8, screen_width_x * 0.5, screen_height_y * 0.2), confidence=0.7)
        activity = time.time()
        pg.moveTo(buttonx, buttony)
        # print(buttonx, buttony)
        pg.press(['right'])
        # print("лечение")
        pg.moveTo(buttonx, buttony, duration=0)  # перемещение к кнопке
        pg.mouseDown(button='left')  # нажать левую клавишу мыши
        pg.moveTo(screen_width_x * 0.5, buttony, duration=1)  # перемещение
        pg.mouseUp(button='left')  # отпустить левую клавиши мыши
        return activity
    except TypeError:
        return zero


def throw_a_ball(template):
    global zero, activity, screen_width_x, screen_height_y
    try:
        buttonx, buttony = pg.locateCenterOnScreen(template, region=(0, 400, screen_width_x, screen_height_y), confidence=0.7)
        activity = time.time()
        pg.moveTo(buttonx, buttony)
        print(buttonx, buttony)
        pg.press(['right'])
        print("метнуть шар")
        pg.moveTo(buttonx, buttony, duration=0)  # перемещение к кнопке
        pg.mouseDown(button='left')  # нажать левую клавишу мыши
        pg.moveTo(400, 113, duration=1)  # перемещение
        pg.mouseUp(button='left')  # отпустить левую клавиши мыши
        pg.click(button='right')
        return activity
    except TypeError:
        return zero


def punch_in_the_face():
    global activity, screen_width_x, screen_height_y
    activity = time.time()
    pg.moveTo(400, 460, duration=0)  # перемещение к своему лицу
    pg.mouseDown(button='left')  # нажать левую клавишу мыши
    pg.moveTo(400, 113, duration=1)  # перемещение
    pg.mouseUp(button='left')  # отпустить левую клавиши мыши
    pg.click(button='right')  # нажать и отпустить правую клавишу
    return activity


def projgrysh(template):
    global zero
    global progr
    global activity
    try:
        buttonx, buttony = pg.locateCenterOnScreen(template, region=(0, 0, 1024, 768), confidence=0.7)
        pg.moveTo(buttonx, buttony)
        # print(buttonx, buttony)
        progr = 1
        pg.moveTo(buttonx, buttony, duration=0)
        pg.doubleClick(buttonx, buttony)
        activity = time.time()
        time.sleep(2)
        return progr, activity
    except TypeError:
        return zero


def vyjgrysh(template):
    global zero
    global vygr
    global activity
    try:
        buttonx, buttony = pg.locateCenterOnScreen(template, region=(0, 0, 1024, 768), confidence=0.7)
        pg.moveTo(buttonx, buttony)
        # print(buttonx, buttony)
        activity = time.time()
        vygr = 1
        pg.moveTo(buttonx, buttony, duration=0)
        pg.doubleClick(buttonx, buttony)
        time.sleep(1)
        return vygr, activity
    except TypeError:
        return zero


def endGame(template):
    global zero
    global Ggame
    global activity
    try:
        buttonx, buttony = pg.locateCenterOnScreen(template, region=(0, 0, 1024, 768), confidence=0.7)
        activity = time.time()
        pg.moveTo(buttonx, buttony)
        print(buttonx, buttony)
        Ggame = 0
        print("Конец игры")
        pg.doubleClick(buttonx, buttony)
        time.sleep(1)
        return Ggame, activity
    except TypeError:
        return zero


def timer_game():
    global start_time
    now = datetime.datetime.now()
    loctime = format(time.time() - start_time)  # время в игре
    # print(now)
    return now, loctime


def print_oll_table():  # функция вывода всей таблицы
    c.execute("SELECT * FROM total;")
    all_results = c.fetchall()
    for id in all_results:
        print(id[0], id[1], id[2], id[3], id[4], id[5], id[6], id[7], id[8], id[9], id[10], id[11], id[12], id[13],
              id[14],
              id[15], id[16], id[17], id[18], id[19], id[20], )
        conn.commit()  # применяем изменения


def load_table():
    c.execute("SELECT * FROM total  WHERE   name_id = (SELECT MAX(name_id)  FROM total);")
    result_old = c.fetchone()
    # print(result_old) # выводит последнюю строку таблицы
    # for id in result_old: # выводит по одному все значения последней строки
    #     print(id)
    b = result_old[1]
    # print(result_old[0])
    # print(b)
    conn.commit()


def fill_table_start():  # заполняем строку таблицы
    c.execute("""INSERT INTO total(date, startgame, endgame, l_days, l_hours, l_minuts, l_seconds,
                g_days, g_hours, g_minuts, g_seconds, tipe, deck, hod, localvictory, locallosing,
                localpercent, globalvictory, globallosing, globalpercent)
                VALUES('01.01.2021', '00:00', '00.00', '0', '0', '0', '0',
                '0', '0', '0', '0', 'стандарт', 'жрец', '0' , '0', '0', '0', '0', '0', '0');""")
    conn.commit()


def fill_table():  # заполняем строку таблицы
    global now, localpercent
    global start_time
    global tipe
    global deck
    global vygr
    global progr
    global hod
    global activity
    date = start_time.strftime("%d.%m.%Y")
    startgame = start_time.strftime("%H:%M:%S")
    end_game = datetime.now()
    endgame = end_game.strftime("%H:%M:%S")

    loctime = end_game - start_time  # время в игре
    l_days = loctime.days  # дни
    l_hours = int(loctime.seconds / 3600)  # часы
    l_minuts = int((loctime.seconds - l_hours * 3600) / 60)  # минуты
    l_seconds = loctime.seconds - l_hours * 3600 - l_minuts * 60  # секунды
    if vygr == 0 and progr == 0:
        progr = 1
    if vygr == 1:
        localpercent = 'выйгрыш'
    if progr == 1:
        localpercent = 'пройгрыш'
    if (time.time() - activity) >= 300:
        localpercent = 'offline'
    c.execute("SELECT * FROM total  WHERE   name_id = (SELECT MAX(name_id)  FROM total);")
    result_old = c.fetchone()
    # print(result_old)
    g_days = result_old[8] + l_days  # дни
    g_hours = result_old[9] + l_hours  # часы
    g_minuts = result_old[10] + l_minuts  # минуты
    g_seconds = result_old[11] + l_seconds  # секунды

    if g_seconds >= 60:
        g_minuts = g_minuts + int(g_seconds / 60)
        g_seconds = g_seconds - (int(g_seconds / 60)) * 60
    if g_minuts >= 60:
        g_hours = g_hours + int(g_minuts / 60)
        g_minuts = g_minuts - (int(g_minuts / 60)) * 60
    if g_hours >= 24:
        g_days = g_days + int(g_hours / 24)
        g_hours = g_hours - (int(g_hours / 24)) * 24

    localvictory = vygr
    locallosing = progr
    globalvictory = result_old[18] + vygr
    globallosing = result_old[19] + progr
    globalpercent = round(((globalvictory / (globalvictory + globallosing)) * 100), 2)
    c.execute("""INSERT INTO total(date, startgame, endgame, l_days, l_hours, l_minuts, l_seconds, 
                g_days, g_hours, g_minuts, g_seconds, tipe, deck, hod, localvictory, locallosing,
                    localpercent, globalvictory, globallosing, globalpercent) 
                    VALUES(?, ?, ?, ?, ?, ? , ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ? , ?, ?);""",
              (date, startgame, endgame, l_days, l_hours, l_minuts, l_seconds,
               g_days, g_hours, g_minuts, g_seconds, tipe, deck, hod, localvictory, locallosing,
               localpercent, globalvictory, globallosing, globalpercent))
    conn.commit()


def grec_standart():
    global Ggame
    global Ngame
    global Gcikl
    global game
    global hod
    global mana
    global moneta
    global tipe
    global deck
    global vygr
    global progr
    global cikl
    global unit
    global start_time
    global delay
    global activity
    tipe = 'стандарт'
    deck = 'жрец'
    ss(active_dir + "btn_grec.png")
    ss(active_dir + "btn_game_st.png")
    start_game(active_dir + "btn_start.png")
    if Ggame == 1:
        Ngame += 1
        print("Игра жрецом началась", Gcikl)
        start_time = datetime.now()  # текущие дата и время
        while Ggame == 1:
            if keyboard.is_pressed('Enter'):  # если клавиша Esc
                fill_table()  # заполняем БД
                print_oll_table()
                sys.exit()  # завершаем программу
            if (time.time() - activity) >= 280:
                pointclick()
            if (time.time() - activity) >= 300:
                Ggame = 0
            Gcikl += 1
            ss(active_dir + "btn_start.png")
            card_selection(active_dir + "btn_ok.png")
            chughoj_hod(active_dir + "chughoj_hod.png")
            vash_hod(active_dir + "btn_end.png")
            # print("hod=", hod)
            if hod == 1 and game == 1:
                close_time = time.time() + 15
                while True:
                    ##bla bla
                    if time.time() > close_time:
                        break
                pg.press(['right'])
                simple_press(active_dir + "btn_end.png")
                simple_press(active_dir + "btn_end2.png")
            elif hod > 1 and hod < 4 and game == 1:
                close_time = time.time() + delay
                while True:
                    ##bla bla
                    if time.time() > close_time:
                        break
                pg.press(['right'])
                health(active_dir + "btn_health.png")
                simple_press(active_dir + "btn_end.png")
            elif hod == 4 and game == 1:
                pg.press(['right'])
                karta(active_dir + "btn_m0.png")
                if moneta == 1:
                    mana += 1
                    moneta = 0
                    pg.press(['right'])
                close_time = time.time() + delay
                while True:
                    if unit == 0 and mana >= 5:
                        pg.press(['right'])
                        karta(active_dir + "btn_m5.png")
                        if unit == 1:
                            mana = mana - 5
                    if time.time() > close_time:
                        break
                if mana >= 2:
                    health(active_dir + "btn_health.png")
                    mana = 0
                moneta = 0
                simple_press(active_dir + "btn_end.png")
            elif hod == 5 and game == 1:
                close_time = time.time() + delay
                while True:
                    if unit == 0 and mana >= 5:
                        pg.press(['right'])
                        karta(active_dir + "btn_m5.png")
                        if unit == 1:
                            mana = mana - 5
                    if time.time() > close_time:
                        break
                if unit == 0 and mana >= 2:
                    health(active_dir + "btn_health.png")
                    mana = 0
                pg.press(['right'])
                simple_press(active_dir + "btn_end.png")
            elif hod == 6 and game == 1:
                close_time = time.time() + delay
                while True:
                    ##bla bla
                    if unit == 0:
                        karta(active_dir + "btn_m6.png")
                        if unit == 1:
                            mana = 0
                    if unit == 0:
                        karta(active_dir + "btn_m5.png")
                        if unit == 1:
                            mana = 1
                    if time.time() > close_time:
                        break
                if unit == 0 and mana >= 2:
                    health(active_dir + "btn_health.png")
                    mana = 0
                pg.press(['right'])
                simple_press(active_dir + "btn_end.png")
            elif hod == 7 and game == 1:
                close_time = time.time() + delay
                while True:
                    ##bla bla
                    if unit == 0:
                        karta(active_dir + "btn_m7.png")
                        if unit == 1:
                            mana = 0
                    if unit == 0:
                        pg.press(['right'])
                        karta(active_dir + "btn_m6.png")
                        if unit == 1:
                            mana = 1
                    if unit == 0:
                        pg.press(['right'])
                        karta(active_dir + "btn_m5.png")
                        if unit == 1:
                            mana = 2
                    if time.time() > close_time:
                        break
                if mana >= 2:
                    health(active_dir + "btn_health.png")
                    mana = 0
                pg.press(['right'])
                simple_press(active_dir + "btn_end.png")
            elif hod == 8 and game == 1:
                close_time = time.time() + delay
                while True:
                    ##bla bla
                    if unit == 0:
                        pg.press(['right'])
                        karta(active_dir + "btn_m8.png")
                        if unit == 1:
                            mana = 0
                    if unit == 0:
                        pg.press(['right'])
                        karta(active_dir + "btn_m7.png")
                        if unit == 1:
                            mana = 1
                    if unit == 0:
                        pg.press(['right'])
                        karta(active_dir + "btn_m6.png")
                        if unit == 1:
                            mana = 2
                    if unit == 0:
                        pg.press(['right'])
                        karta(active_dir + "btn_m5.png")
                        if unit == 1:
                            mana = 3
                    if time.time() > close_time:
                        break
                if mana >= 2:
                    health(active_dir + "btn_health.png")
                    mana = 0
                pg.press(['right'])
                simple_press(active_dir + "btn_end.png")
            elif hod == 9 and game == 1:
                close_time = time.time() + delay
                while True:
                    ##bla bla
                    if unit == 0:
                        pg.press(['right'])
                        karta(active_dir + "btn_m9.png")
                        if unit == 1:
                            mana = 0
                    if unit == 0:
                        pg.press(['right'])
                        karta(active_dir + "btn_m8.png")
                        if unit == 1:
                            mana = 1
                    if unit == 0:
                        pg.press(['right'])
                        karta(active_dir + "btn_m7.png")
                        if unit == 1:
                            mana = 2
                    if unit == 0:
                        pg.press(['right'])
                        karta(active_dir + "btn_m6.png")
                        if unit == 1:
                            mana = 3
                    if unit == 0:
                        pg.press(['right'])
                        karta(active_dir + "btn_m5.png")
                        if unit == 1:
                            mana = 4
                    if time.time() > close_time:
                        break
                if mana >= 2:
                    health(active_dir + "btn_health.png")
                    mana = 0
                pg.press(['right'])
                simple_press(active_dir + "btn_end.png")
            elif hod >= 10 and game == 1:
                close_time = time.time() + delay
                while True:
                    ##bla bla
                    if unit == 0:
                        pg.press(['right'])
                        karta(active_dir + "btn_m10.png")
                        if unit == 1:
                            mana = 0
                    if unit == 0:
                        pg.press(['right'])
                        karta(active_dir + "btn_m9.png")
                        if unit == 1:
                            mana = 1
                    if unit == 0:
                        pg.press(['right'])
                        karta(active_dir + "btn_m8.png")
                        if unit == 1:
                            mana = 2
                    if unit == 0:
                        pg.press(['right'])
                        karta(active_dir + "btn_m7.png")
                        if unit == 1:
                            mana = 3
                    if unit == 0:
                        pg.press(['right'])
                        karta(active_dir + "btn_m6.png")
                        if unit == 1:
                            mana = 4
                    if unit == 0:
                        pg.press(['right'])
                        karta(active_dir + "btn_m5.png")
                        if unit == 1:
                            mana = 5
                    if time.time() > close_time:
                        break
                if mana >= 2:
                    health(active_dir + "btn_health.png")
                    mana = 0
                pg.press(['right'])
                simple_press(active_dir + "btn_end.png")
            projgrysh(active_dir + "end_game.png")
            vyjgrysh(active_dir + "victory.png")
            endGame(active_dir + "end_game2.png")
            if Ggame == 0:
                fill_table()  # заполняем БД
            #               print_oll_table()
            ss(active_dir + "ok_2.png")
            ss(active_dir + "bt.png")
            ss(active_dir + "bt2.png")
        return Ggame, Ngame, Gcikl, vygr, progr, start_time, tipe, deck, activity


def hant_standart():
    global Ggame
    global Ngame
    global Gcikl
    global game
    global hod
    global mana
    global moneta
    global tipe
    global deck
    global vygr
    global progr
    global cikl
    global unit
    global start_time
    global delay
    global activity
    tipe = 'стандарт'
    deck = 'охотник'
    ss(active_dir + "btn_hant.png")
    ss(active_dir + "btn_game_st.png")
    start_game(active_dir + "btn_start.png")
    if Ggame == 1:
        Ngame += 1
        print("игра охотником началась", Gcikl)
        start_time = datetime.now()  # текущие дата и время
        while Ggame == 1:
            if keyboard.is_pressed('Enter'):  # если клавиша Esc
                timer_game()  # подсчет времени
                fill_table()  # заполняем БД
                print_oll_table()
                sys.exit()  # завершаем программу
            if (time.time() - activity) >= 280:
                pointclick()
            if (time.time() - activity) >= 300:
                Ggame = 0
            Gcikl += 1
            card_selection(active_dir + "btn_ok.png")
            chughoj_hod(active_dir + "chughoj_hod.png")
            vash_hod(active_dir + "btn_end.png")
            print("hod=", hod)
            if hod == 1 and game == 1:
                close_time = time.time() + 15
                while True:
                    ##bla bla
                    if time.time() > close_time:
                        break
                pg.press(['right'])
                simple_press(active_dir + "btn_end.png")
                simple_press(active_dir + "btn_end2.png")
            elif hod > 1 and hod < 4 and game == 1:
                close_time = time.time() + delay
                while True:
                    ##bla bla
                    if time.time() > close_time:
                        break
                pg.press(['right'])
                hero_strength(active_dir + "btn_strela.png")
                ss(active_dir + "btn_end.png")
                ss(active_dir + "btn_end2.png")
            elif hod == 4 and game == 1:
                pg.press(['right'])
                karta(active_dir + "btn_m0.png")
                if moneta == 1:
                    mana += 1
                    moneta = 0
                    pg.press(['right'])
                close_time = time.time() + delay
                while True:
                    if unit == 0 and mana >= 5:
                        pg.press(['right'])
                        karta(active_dir + "btn_m5.png")
                        if unit == 1:
                            mana = mana - 5
                    if time.time() > close_time:
                        break
                if mana >= 2:
                    hero_strength(active_dir + "btn_strela.png")
                    mana = 0
                moneta = 0
                ss(active_dir + "btn_end.png")
                ss(active_dir + "btn_end2.png")
            elif hod == 5 and game == 1:
                close_time = time.time() + delay
                while True:
                    ##bla bla
                    if unit == 0:
                        pg.press(['right'])
                        karta(active_dir + "btn_m5.png")
                        if unit == 1:
                            mana = 1
                    if time.time() > close_time:
                        break
                if mana >= 2:
                    hero_strength(active_dir + "btn_strela.png")
                    mana = 0
                pg.press(['right'])
                ss(active_dir + "btn_end.png")
                ss(active_dir + "btn_end2.png")
            elif hod == 6 and game == 1:
                close_time = time.time() + delay
                while True:
                    ##bla bla
                    if unit == 0:
                        pg.press(['right'])
                        karta(active_dir + "btn_m6.png")
                        if unit == 1:
                            mana = 0
                    if unit == 0:
                        pg.press(['right'])
                        karta(active_dir + "btn_m5.png")
                        if unit == 1:
                            mana = 1
                    if time.time() > close_time:
                        break
                if mana >= 2:
                    hero_strength(active_dir + "btn_strela.png")
                    mana = 0
                pg.press(['right'])
                ss(active_dir + "btn_end.png")
                ss(active_dir + "btn_end2.png")
            elif hod >= 7 and game == 1:
                close_time = time.time() + delay
                while True:
                    ##bla bla
                    if unit == 0:
                        karta(active_dir + "btn_m7.png")
                        if unit == 1:
                            mana = mana - 7
                    if unit == 0:
                        pg.press(['right'])
                        karta(active_dir + "btn_m6.png")
                        if unit == 1:
                            mana = mana - 6
                    if unit == 0:
                        pg.press(['right'])
                        karta(active_dir + "btn_m5.png")
                        if unit == 1:
                            mana = mana - 5
                    if time.time() > close_time:
                        break
                if mana >= 2:
                    hero_strength(active_dir + "btn_strela.png")
                    mana = 0
                pg.press(['right'])
                ss(active_dir + "btn_end.png")
                ss(active_dir + "btn_end2.png")
            projgrysh(active_dir + "end_game.png")
            vyjgrysh(active_dir + "victory.png")
            endGame(active_dir + "end_game2.png")
            if Ggame == 0:
                fill_table()  # заполняем БД
            #               print_oll_table()
            ss(active_dir + "ok_2.png")
            ss(active_dir + "bt.png")
            ss(active_dir + "bt2.png")
        return Ggame, Ngame, Gcikl, vygr, progr, start_time, activity


def voin_standart():
    global Ggame
    global Ngame
    global Gcikl
    global game
    global hod
    global mana
    global moneta
    global tipe
    global deck
    global vygr
    global progr
    global cikl
    global unit
    global start_time
    global delay
    global activity
    tipe = 'стандарт'
    deck = 'воин'
    ss(active_dir + "btn_voin.png")
    ss(active_dir + "btn_game_st.png")
    start_game(active_dir + "btn_start.png")
    if Ggame == 1:
        Ngame += 1
        print("Игра воином началась", Gcikl)
        start_time = datetime.now()  # текущие дата и время
        while Ggame == 1:
            if keyboard.is_pressed('Enter'):  # если клавиша Esc
                timer_game()  # подсчет времени
                fill_table()  # заполняем БД
                print_oll_table()
                sys.exit()  # завершаем программу
            if (time.time() - activity) >= 280:
                pointclick()
            if (time.time() - activity) >= 300:
                Ggame = 0
            Gcikl += 1
            ss(active_dir + "btn_start.png")
            card_selection(active_dir + "btn_ok.png")
            chughoj_hod(active_dir + "chughoj_hod.png")
            vash_hod(active_dir + "btn_end.png")
            print("hod=", hod)
            if hod == 1 and game == 1:
                close_time = time.time() + 15
                while True:
                    ##bla bla
                    if time.time() > close_time:
                        break
                pg.press(['right'])
                simple_press(active_dir + "btn_end.png")
                simple_press(active_dir + "btn_end2.png")
            elif hod > 1 and hod < 4 and game == 1:
                close_time = time.time() + delay
                while True:
                    ##bla bla
                    if time.time() > close_time:
                        break
                pg.press(['right'])
                hero_strength(active_dir + "btn_schit.png")
                ss(active_dir + "btn_end.png")
                ss(active_dir + "btn_end2.png")
            elif hod == 4 and game == 1:
                pg.press(['right'])
                karta(active_dir + "btn_m0.png")
                if moneta == 1:
                    mana += 1
                    moneta = 0
                    pg.press(['right'])
                close_time = time.time() + delay
                while True:
                    if unit == 0 and mana >= 5:
                        pg.press(['right'])
                        karta(active_dir + "btn_m5.png")
                        if unit == 1:
                            mana = mana - 5
                    if time.time() > close_time:
                        break
                if mana >= 2:
                    hero_strength(active_dir + "btn_schit.png")
                    mana = 0
                moneta = 0
                ss(active_dir + "btn_end.png")
                ss(active_dir + "btn_end2.png")
            elif hod == 5 and game == 1:
                close_time = time.time() + delay
                while True:
                    ##bla bla
                    if unit == 0:
                        pg.press(['right'])
                        karta(active_dir + "btn_m5.png")
                        if unit == 1:
                            mana = 1
                    if time.time() > close_time:
                        break
                if mana >= 2:
                    hero_strength(active_dir + "btn_schit.png")
                    mana = 0
                pg.press(['right'])
                ss(active_dir + "btn_end.png")
                ss(active_dir + "btn_end2.png")
            elif hod == 6 and game == 1:
                close_time = time.time() + delay
                while True:
                    ##bla bla
                    if unit == 0:
                        pg.press(['right'])
                        karta(active_dir + "btn_m6.png")
                        if unit == 1:
                            mana = 0
                    if unit == 0:
                        pg.press(['right'])
                        karta(active_dir + "btn_m5.png")
                        if unit == 1:
                            mana = 1
                    if time.time() > close_time:
                        break
                if mana >= 2:
                    hero_strength(active_dir + "btn_schit.png")
                    mana = 0
                pg.press(['right'])
                ss(active_dir + "btn_end.png")
                ss(active_dir + "btn_end2.png")
            elif hod >= 7 and game == 1:
                close_time = time.time() + delay
                while True:
                    ##bla bla
                    if unit == 0:
                        karta(active_dir + "btn_m7.png")
                        if unit == 1:
                            mana = mana - 7
                    if unit == 0:
                        pg.press(['right'])
                        karta(active_dir + "btn_m6.png")
                        if unit == 1:
                            mana = mana - 6
                    if unit == 0:
                        pg.press(['right'])
                        karta(active_dir + "btn_m5.png")
                        if unit == 1:
                            mana = mana - 5
                    if time.time() > close_time:
                        break
                if mana >= 2:
                    hero_strength(active_dir + "btn_schit.png")
                    mana = 0
                pg.press(['right'])
                ss(active_dir + "btn_end.png")
                ss(active_dir + "btn_end2.png")
            projgrysh(active_dir + "end_game.png")
            vyjgrysh(active_dir + "victory.png")
            endGame(active_dir + "end_game2.png")
            if Ggame == 0:
                fill_table()  # заполняем БД
            #                print_oll_table()
            ss(active_dir + "ok_2.png")
            ss(active_dir + "bt.png")
            ss(active_dir + "bt2.png")
        return Ggame, Ngame, Gcikl, vygr, progr, start_time, activity


def mag_standart():
    global Ggame
    global Ngame
    global Gcikl
    global game
    global hod
    global mana
    global moneta
    global tipe
    global deck
    global vygr
    global progr
    global cikl
    global unit
    global start_time
    global delay
    global activity
    tipe = 'стандарт'
    deck = 'маг'
    ss(active_dir + "btn_mag.png")
    ss(active_dir + "btn_game_st.png")
    start_game(active_dir + "btn_start.png")
    if Ggame == 1:
        Ngame += 1
        print("Игра магом началась", Gcikl)
        start_time = datetime.now()  # текущие дата и время
        while Ggame == 1:
            if keyboard.is_pressed('Enter'):  # если клавиша Esc
                timer_game()  # подсчет времени
                fill_table()  # заполняем БД
                print_oll_table()
                sys.exit()  # завершаем программу
            if (time.time() - activity) >= 280:
                pointclick()
            if (time.time() - activity) >= 300:
                Ggame = 0
            Gcikl += 1
            ss(active_dir + "btn_start.png")
            card_selection(active_dir + "btn_ok.png")
            chughoj_hod(active_dir + "chughoj_hod.png")
            vash_hod(active_dir + "btn_end.png")
            print("hod=", hod)
            if hod == 1 and game == 1:
                close_time = time.time() + 15
                while True:
                    ##bla bla
                    if time.time() > close_time:
                        break
                pg.press(['right'])
                simple_press(active_dir + "btn_end.png")
                simple_press(active_dir + "btn_end2.png")
            elif hod > 1 and hod < 4 and game == 1:
                close_time = time.time() + delay
                while True:
                    ##bla bla
                    if time.time() > close_time:
                        break
                pg.press(['right'])
                throw_a_ball(active_dir + "btn_shar.png")
                ss(active_dir + "btn_end.png")
                ss(active_dir + "btn_end2.png")
            elif hod == 4 and game == 1:
                pg.press(['right'])
                karta(active_dir + "btn_m0.png")
                if moneta == 1:
                    mana += 1
                    moneta = 0
                    pg.press(['right'])
                close_time = time.time() + delay
                while True:
                    if unit == 0 and mana >= 5:
                        pg.press(['right'])
                        karta(active_dir + "btn_m5.png")
                        if unit == 1:
                            mana = mana - 5
                    if time.time() > close_time:
                        break
                if mana >= 2:
                    throw_a_ball(active_dir + "btn_shar.png")
                    mana = 0
                moneta = 0
                ss(active_dir + "btn_end.png")
                ss(active_dir + "btn_end2.png")
            elif hod == 5 and game == 1:
                close_time = time.time() + delay
                while True:
                    ##bla bla
                    if unit == 0:
                        pg.press(['right'])
                        karta(active_dir + "btn_m5.png")
                        if unit == 1:
                            mana = 1
                    if time.time() > close_time:
                        break
                if mana >= 2:
                    throw_a_ball(active_dir + "btn_shar.png")
                    mana = 0
                pg.press(['right'])
                ss(active_dir + "btn_end.png")
                ss(active_dir + "btn_end2.png")
            elif hod == 6 and game == 1:
                close_time = time.time() + delay
                while True:
                    ##bla bla
                    if unit == 0:
                        pg.press(['right'])
                        karta(active_dir + "btn_m6.png")
                        if unit == 1:
                            mana = 0
                    if unit == 0:
                        pg.press(['right'])
                        karta(active_dir + "btn_m5.png")
                        if unit == 1:
                            mana = 1
                    if time.time() > close_time:
                        break
                if mana >= 2:
                    throw_a_ball(active_dir + "btn_shar.png")
                    mana = 0
                pg.press(['right'])
                ss(active_dir + "btn_end.png")
                ss(active_dir + "btn_end2.png")
            elif hod >= 7 and game == 1:
                close_time = time.time() + delay
                while True:
                    ##bla bla
                    if unit == 0:
                        karta(active_dir + "btn_m7.png")
                        if unit == 1:
                            mana = mana - 7
                    if unit == 0:
                        pg.press(['right'])
                        karta(active_dir + "btn_m6.png")
                        if unit == 1:
                            mana = mana - 6
                    if unit == 0:
                        pg.press(['right'])
                        karta(active_dir + "btn_m5.png")
                        if unit == 1:
                            mana = mana - 5
                    if time.time() > close_time:
                        break
                if mana >= 2:
                    throw_a_ball(active_dir + "btn_shar.png")
                    mana = 0
                pg.press(['right'])
                ss(active_dir + "btn_end.png")
                ss(active_dir + "btn_end2.png")
            projgrysh(active_dir + "end_game.png")
            vyjgrysh(active_dir + "victory.png")
            endGame(active_dir + "end_game2.png")
            if Ggame == 0:
                fill_table()  # заполняем БД
            #                print_oll_table()
            ss(active_dir + "ok_2.png")
            ss(active_dir + "bt.png")
            ss(active_dir + "bt2.png")
        return Ggame, Ngame, Gcikl, vygr, progr, start_time, activity


def roga_standart():
    global Ggame
    global Ngame
    global Gcikl
    global game
    global hod
    global mana
    global moneta
    global tipe
    global deck
    global vygr
    global progr
    global cikl
    global unit
    global start_time
    global delay
    global activity
    tipe = 'стандарт'
    deck = 'рога'
    ss(active_dir + "btn_roga.png")
    ss(active_dir + "btn_game_st.png")
    start_game(active_dir + "btn_start.png")
    if Ggame == 1:
        Ngame += 1
        # print("Игра рогой началась", Gcikl)
        start_time = datetime.now()  # текущие дата и время
        while Ggame == 1:
            if keyboard.is_pressed('Enter'):  # если клавиша Esc
                timer_game()  # подсчет времени
                fill_table()  # заполняем БД
                print_oll_table()
                sys.exit()  # завершаем программу
            if (time.time() - activity) >= 280:
                pointclick()
            if (time.time() - activity) >= 300:
                Ggame = 0
            Gcikl += 1
            ss(active_dir + "btn_start.png")
            card_selection(active_dir + "btn_ok.png")
            chughoj_hod(active_dir + "chughoj_hod.png")
            vash_hod(active_dir + "btn_end.png")
            # print("hod=", hod)
            if hod == 1 and game == 1:
                close_time = time.time() + 20
                while True:
                    ##bla bla
                    if time.time() > close_time:
                        break
                pg.press(['right'])
                simple_press(active_dir + "btn_end.png")
                simple_press(active_dir + "btn_end2.png")
            elif hod > 1 and hod < 4 and game == 1:
                close_time = time.time() + delay
                while True:
                    ##bla bla
                    if time.time() > close_time:
                        break
                pg.press(['right'])
                hero_strength(active_dir + "btn_two_swords.png")
                punch_in_the_face()
                simple_press(active_dir + "btn_end.png")
                simple_press(active_dir + "btn_end2.png")
            elif hod == 4 and game == 1:
                pg.press(['right'])
                karta(active_dir + "btn_m0.png")
                if moneta == 1:
                    mana += 1
                    moneta = 0
                    pg.press(['right'])
                close_time = time.time() + delay
                while True:
                    if unit == 0 and mana >= 5:
                        pg.press(['right'])
                        karta(active_dir + "btn_m5.png")
                        if unit == 1:
                            mana = mana - 5
                    if time.time() > close_time:
                        break
                if mana >= 2:
                    hero_strength(active_dir + "btn_two_swords.png")
                    punch_in_the_face()
                    mana = 0
                moneta = 0
                ss(active_dir + "btn_end.png")
                ss(active_dir + "btn_end2.png")
            elif hod == 5 and game == 1:
                close_time = time.time() + delay
                while True:
                    ##bla bla
                    if unit == 0:
                        pg.press(['right'])
                        karta(active_dir + "btn_m5.png")
                        if unit == 1:
                            mana = 1
                    if time.time() > close_time:
                        break
                if mana >= 2:
                    hero_strength(active_dir + "btn_two_swords.png")
                    punch_in_the_face()
                    mana = 0
                pg.press(['right'])
                simple_press(active_dir + "btn_end.png")
                simple_press(active_dir + "btn_end2.png")
            elif hod == 6 and game == 1:
                close_time = time.time() + delay
                while True:
                    ##bla bla
                    if unit == 0 and mana >= 6:
                        pg.press(['right'])
                        karta(active_dir + "btn_m6.png")
                        if unit == 1:
                            mana = mana - 6
                    if unit == 0 and mana >= 5:
                        pg.press(['right'])
                        karta(active_dir + "btn_m5.png")
                        if unit == 1:
                            mana = mana - 5
                    if time.time() > close_time:
                        break
                if mana >= 2:
                    hero_strength(active_dir + "btn_two_swords.png")
                    punch_in_the_face()
                    mana = 0
                pg.press(['right'])
                simple_press(active_dir + "btn_end.png")
                simple_press(active_dir + "btn_end2.png")
            elif hod >= 7 and game == 1:
                close_time = time.time() + delay
                while True:
                    ##bla bla
                    if unit == 0:
                        karta(active_dir + "btn_m7.png")
                        if unit == 1:
                            mana = mana - 7
                    if unit == 0:
                        pg.press(['right'])
                        karta(active_dir + "btn_m6.png")
                        if unit == 1:
                            mana = mana - 6
                    if unit == 0:
                        pg.press(['right'])
                        karta(active_dir + "btn_m5.png")
                        if unit == 1:
                            mana = mana - 5
                    if time.time() > close_time:
                        break
                if mana >= 2:
                    hero_strength(active_dir + "btn_two_swords.png")
                    punch_in_the_face()
                    mana = 0
                pg.press(['right'])
                simple_press(active_dir + "btn_end.png")
                simple_press(active_dir + "btn_end2.png")
            projgrysh(active_dir + "end_game.png")
            vyjgrysh(active_dir + "victory.png")
            endGame(active_dir + "end_game2.png")
            if Ggame == 0:
                fill_table()  # заполняем БД
        #               print_oll_table()
            ss(active_dir + "ok_2.png")
            ss(active_dir + "bt.png")
            ss(active_dir + "bt2.png")
        return Ggame, Ngame, Gcikl, vygr, progr, start_time, activity


def dh_standart():
    global Ggame
    global Ngame
    global Gcikl
    global game
    global hod
    global mana
    global moneta
    global tipe
    global deck
    global vygr
    global progr
    global cikl
    global unit
    global start_time
    global delay
    global activity
    tipe = 'стандарт'
    deck = ' Д Х '
    ss(active_dir + "btn_dh.png")
    ss(active_dir + "btn_game_st.png")
    start_game(active_dir + "btn_start.png")
    if Ggame == 1:
        Ngame += 1
        print("Игра ДХ началась", Gcikl)
        start_time = datetime.now()  # текущие дата и время
        while Ggame == 1:
            if keyboard.is_pressed('Enter'):  # если клавиша Esc
                timer_game()  # подсчет времени
                fill_table()  # заполняем БД
                print_oll_table()
                sys.exit()  # завершаем программу
            if (time.time() - activity) >= 280:
                pointclick()
            if (time.time() - activity) >= 300:
                Ggame = 0
            Gcikl += 1
            ss(active_dir + "btn_start.png")
            card_selection(active_dir + "btn_ok.png")
            chughoj_hod(active_dir + "chughoj_hod.png")
            vash_hod(active_dir + "btn_end.png")
            print("hod=", hod)
            if hod == 1 and game == 1:
                close_time = time.time() + 15
                while True:
                    ##bla bla
                    if time.time() > close_time:
                        break
                pg.press(['right'])
                ss(active_dir + "btn_dh_hand.png")
                punch_in_the_face()
                ss(active_dir + "btn_end.png")
                ss(active_dir + "btn_end2.png")
            elif hod > 1 and hod < 4 and game == 1:
                close_time = time.time() + delay
                while True:
                    ##bla bla
                    if unit == 0 and mana >= 3:
                        pg.press(['right'])
                        karta(active_dir + "btn_m3.png")
                        if unit == 1:
                            mana = mana - 3
                    if unit == 0 and mana >= 4:
                        pg.press(['right'])
                        karta(active_dir + "btn_m4.png")
                        if unit == 1:
                            mana = mana - 4
                    if time.time() > close_time:
                        break
                    if mana >=1:
                        hero_strength(active_dir + "btn_dh_hand.png")
                        punch_in_the_face()
                        mana = 0
                pg.press(['right'])
                ss(active_dir + "btn_end.png")
                ss(active_dir + "btn_end2.png")
            elif hod == 4 and game == 1:
                pg.press(['right'])
                karta(active_dir + "btn_m0.png")
                if moneta == 1:
                    mana += 1
                    pg.press(['right'])
                close_time = time.time() + delay
                while True:
                    ##bla bla
                    if unit == 0 and mana >= 3:
                        pg.press(['right'])
                        karta(active_dir + "btn_m3.png")
                        if unit == 1:
                            mana = mana - 3
                    if unit == 0 and mana >= 4:
                        pg.press(['right'])
                        karta(active_dir + "btn_m4.png")
                        if unit == 1:
                            mana = mana - 4
                    if unit == 0 and mana >= 5:
                        pg.press(['right'])
                        karta(active_dir + "btn_m5.png")
                        if unit == 1:
                            mana = mana - 5
                    if time.time() > close_time:
                        break
                    if mana >= 1:
                        hero_strength(active_dir + "btn_dh_hand.png")
                        punch_in_the_face()
                        mana = 0
                moneta = 0
                ss(active_dir + "btn_end.png")
                ss(active_dir + "btn_end2.png")
            elif hod == 5 and game == 1:
                close_time = time.time() + delay
                while True:
                    ##bla bla
                    if unit == 0 and mana >= 3:
                        pg.press(['right'])
                        karta(active_dir + "btn_m3.png")
                        if unit == 1:
                            mana = mana - 3
                    if unit == 0 and mana >= 4:
                        pg.press(['right'])
                        karta(active_dir + "btn_m4.png")
                        if unit == 1:
                            mana = mana - 4
                    if unit == 0 and mana >= 5:
                        pg.press(['right'])
                        karta(active_dir + "btn_m5.png")
                        if unit == 1:
                            mana = mana - 5
                    if time.time() > close_time:
                        break

                    if mana >= 1:
                        hero_strength(active_dir + "btn_dh_hand.png")
                        punch_in_the_face()
                        mana = 0
                pg.press(['right'])
                ss(active_dir + "btn_end.png")
                ss(active_dir + "btn_end2.png")
            elif hod == 6 and game == 1:
                close_time = time.time() + delay
                while True:
                    ##bla bla
                    if unit == 0 and mana >= 3:
                        pg.press(['right'])
                        karta(active_dir + "btn_m3.png")
                        if unit == 1:
                            mana = mana - 3
                    if unit == 0 and mana >= 4:
                        pg.press(['right'])
                        karta(active_dir + "btn_m4.png")
                        if unit == 1:
                            mana = mana - 4
                    if unit == 0 and mana >= 5:
                        pg.press(['right'])
                        karta(active_dir + "btn_m5.png")
                        if unit == 1:
                            mana = mana - 5
                    if unit == 0 and mana >= 6:
                        pg.press(['right'])
                        karta(active_dir + "btn_m6.png")
                        if unit == 1:
                            mana = mana - 6
                    if time.time() > close_time:
                        break

                    if mana >= 1:
                        hero_strength(active_dir + "btn_dh_hand.png")
                        punch_in_the_face()
                        mana = 0
                pg.press(['right'])
                ss(active_dir + "btn_end.png")
                ss(active_dir + "btn_end2.png")
            elif hod >= 7 and game == 1:
                close_time = time.time() + delay
                while True:
                    ##bla bla
                    if unit == 0 and mana >= 7:
                        karta(active_dir + "btn_m7.png")
                        if unit == 1:
                            mana = mana - 7
                    if unit == 0 and mana >= 6:
                        pg.press(['right'])
                        karta(active_dir + "btn_m6.png")
                        if unit == 1:
                            mana = mana - 6
                    if unit == 0 and mana >= 5:
                        pg.press(['right'])
                        karta(active_dir + "btn_m5.png")
                        if unit == 1:
                            mana = mana - 5
                    if time.time() > close_time:
                        break

                    if mana >= 1:
                        hero_strength(active_dir + "btn_dh_hand.png")
                        punch_in_the_face()
                        mana = 0
                pg.press(['right'])
                ss(active_dir + "btn_end.png")
                ss(active_dir + "btn_end2.png")
            projgrysh(active_dir + "end_game.png")
            vyjgrysh(active_dir + "victory.png")
            endGame(active_dir + "end_game2.png")
            if Ggame == 0:
                fill_table()  # заполняем БД
            #                print_oll_table()
            ss(active_dir + "ok_2.png")
            ss(active_dir + "bt.png")
            ss(active_dir + "bt2.png")
        return Ggame, Ngame, Gcikl, vygr, progr, start_time, activity


def druid_standart():
    global Ggame
    global Ngame
    global Gcikl
    global game
    global hod
    global mana
    global moneta
    global tipe
    global deck
    global vygr
    global progr
    global cikl
    global unit
    global start_time
    global delay
    global activity
    tipe = 'стандарт'
    deck = 'друид'
    ss(active_dir + "btn_druid.png")
    ss(active_dir + "btn_game_st.png")
    start_game(active_dir + "btn_start.png")
    if Ggame == 1:
        Ngame += 1
        print("Игра друидом началась", Gcikl)
        start_time = datetime.now()  # текущие дата и время
        while Ggame == 1:
            if keyboard.is_pressed('Enter'):  # если клавиша Esc
                timer_game()  # подсчет времени
                fill_table()  # заполняем БД
                print_oll_table()
                sys.exit()  # завершаем программу
            if (time.time() - activity) >= 280:
                pointclick()
            if (time.time() - activity) >= 300:
                Ggame = 0
            Gcikl += 1
            ss(active_dir + "btn_start.png")
            card_selection(active_dir + "btn_ok.png")
            chughoj_hod(active_dir + "chughoj_hod.png")
            vash_hod(active_dir + "btn_end.png")
            print("hod=", hod)
            if hod == 1 and game == 1:
                close_time = time.time() + 15
                while True:
                    ##bla bla
                    if time.time() > close_time:
                        break
                pg.press(['right'])
                simple_press(active_dir + "btn_end.png")
                simple_press(active_dir + "btn_end2.png")
            elif hod > 1 and hod < 4 and game == 1:
                close_time = time.time() + delay
                while True:
                    ##bla bla
                    if time.time() > close_time:
                        break
                pg.press(['right'])
                ss(active_dir + "btn_leo.png")
                punch_in_the_face()
                ss(active_dir + "btn_end.png")
                ss(active_dir + "btn_end2.png")
            elif hod == 4 and game == 1:
                pg.press(['right'])
                karta(active_dir + "btn_m0.png")
                if moneta == 1:
                    mana += 1
                    moneta = 0
                    pg.press(['right'])
                close_time = time.time() + delay
                while True:
                    if unit == 0 and mana >= 5:
                        pg.press(['right'])
                        karta(active_dir + "btn_m5.png")
                        if unit == 1:
                            mana = mana - 5
                    if time.time() > close_time:
                        break
                if mana >= 2:
                    ss(active_dir + "btn_leo.png")
                    punch_in_the_face()
                    mana = 0
                moneta = 0
                ss(active_dir + "btn_end.png")
                ss(active_dir + "btn_end2.png")
            elif hod == 5 and game == 1:
                close_time = time.time() + delay
                while True:
                    ##bla bla
                    if unit == 0:
                        pg.press(['right'])
                        karta(active_dir + "btn_m5.png")
                        if unit == 1:
                            mana = 1
                    if time.time() > close_time:
                        break
                if mana >= 2:
                    ss(active_dir + "btn_leo.png")
                    punch_in_the_face()
                    mana = 0
                pg.press(['right'])
                ss(active_dir + "btn_end.png")
                ss(active_dir + "btn_end2.png")
            elif hod == 6 and game == 1:
                close_time = time.time() + delay
                while True:
                    ##bla bla
                    if unit == 0:
                        pg.press(['right'])
                        karta(active_dir + "btn_m6.png")
                        if unit == 1:
                            mana = 0
                    if unit == 0:
                        pg.press(['right'])
                        karta(active_dir + "btn_m5.png")
                        if unit == 1:
                            mana = 1
                    if time.time() > close_time:
                        break
                if mana >= 2:
                    ss(active_dir + "btn_leo.png")
                    punch_in_the_face()
                    mana = 0
                pg.press(['right'])
                ss(active_dir + "btn_end.png")
                ss(active_dir + "btn_end2.png")
            elif hod >= 7 and game == 1:
                close_time = time.time() + delay
                while True:
                    ##bla bla
                    if unit == 0:
                        karta(active_dir + "btn_m7.png")
                        if unit == 1:
                            mana = mana - 7
                    if unit == 0:
                        pg.press(['right'])
                        karta(active_dir + "btn_m6.png")
                        if unit == 1:
                            mana = mana - 6
                    if unit == 0:
                        pg.press(['right'])
                        karta(active_dir + "btn_m5.png")
                        if unit == 1:
                            mana = mana - 5
                    if time.time() > close_time:
                        break
                if mana >= 2:
                    ss(active_dir + "btn_leo.png")
                    punch_in_the_face()
                    mana = 0
                pg.press(['right'])
                ss(active_dir + "btn_end.png")
                ss(active_dir + "btn_end2.png")
            projgrysh(active_dir + "end_game.png")
            vyjgrysh(active_dir + "victory.png")
            endGame(active_dir + "end_game2.png")
            if Ggame == 0:
                fill_table()  # заполняем БД
            #               print_oll_table()
            ss(active_dir + "ok_2.png")
            ss(active_dir + "bt.png")
            ss(active_dir + "bt2.png")
        return Ggame, Ngame, Gcikl, vygr, progr, start_time, activity


def shaman_standart():
    global Ggame
    global Ngame
    global Gcikl
    global game
    global hod
    global mana
    global moneta
    global tipe
    global deck
    global vygr
    global progr
    global cikl
    global unit
    global start_time
    global delay
    global activity
    tipe = 'стандарт'
    deck = 'шаман'
    ss(active_dir + "btn_shaman.png")
    ss(active_dir + "btn_game_st.png")
    start_game(active_dir + "btn_start.png")
    if Ggame == 1:
        Ngame += 1
        print("игра шаманов началась", Gcikl)
        start_time = datetime.now()  # текущие дата и время
        while Ggame == 1:
            if keyboard.is_pressed('Enter'):  # если клавиша Esc
                timer_game()  # подсчет времени
                fill_table()  # заполняем БД
                print_oll_table()
                sys.exit()  # завершаем программу
            if (time.time() - activity) >= 280:
                pointclick()
            if (time.time() - activity) >= 300:
                Ggame = 0
            Gcikl += 1
            ss(active_dir + "btn_start.png")
            card_selection(active_dir + "btn_ok.png")
            chughoj_hod(active_dir + "chughoj_hod.png")
            vash_hod(active_dir + "btn_end.png")
            print("hod=", hod)
            if hod == 1 and game == 1:
                close_time = time.time() + 15
                while True:
                    ##bla bla
                    if time.time() > close_time:
                        break
                pg.press(['right'])
                simple_press(active_dir + "btn_end.png")
                simple_press(active_dir + "btn_end2.png")
            elif hod > 1 and hod < 4 and game == 1:
                close_time = time.time() + delay
                while True:
                    ##bla bla
                    if time.time() > close_time:
                        break
                pg.press(['right'])
                hero_strength(active_dir + "btn_totem.png")
                ss(active_dir + "btn_end.png")
                ss(active_dir + "btn_end2.png")
            elif hod == 4 and game == 1:
                pg.press(['right'])
                karta(active_dir + "btn_m0.png")
                if moneta == 1:
                    mana += 1
                    moneta = 0
                    pg.press(['right'])
                close_time = time.time() + delay
                while True:
                    if unit == 0 and mana >= 5:
                        pg.press(['right'])
                        karta(active_dir + "btn_m5.png")
                        if unit == 1:
                            mana = mana - 5
                    if time.time() > close_time:
                        break
                if mana >= 2:
                    hero_strength(active_dir + "btn_totem.png")
                    mana = 0
                moneta = 0
                ss(active_dir + "btn_end.png")
                ss(active_dir + "btn_end2.png")
            elif hod == 5 and game == 1:
                close_time = time.time() + delay
                while True:
                    ##bla bla
                    if unit == 0:
                        pg.press(['right'])
                        karta(active_dir + "btn_m5.png")
                        if unit == 1:
                            mana = 1
                    if time.time() > close_time:
                        break
                if mana >= 2:
                    hero_strength(active_dir + "btn_totem.png")
                    mana = 0
                pg.press(['right'])
                ss(active_dir + "btn_end.png")
                ss(active_dir + "btn_end2.png")
            elif hod == 6 and game == 1:
                close_time = time.time() + delay
                while True:
                    ##bla bla
                    if unit == 0:
                        pg.press(['right'])
                        karta(active_dir + "btn_m6.png")
                        if unit == 1:
                            mana = 0
                    if unit == 0:
                        pg.press(['right'])
                        karta(active_dir + "btn_m5.png")
                        if unit == 1:
                            mana = 1
                    if time.time() > close_time:
                        break
                if mana >= 2:
                    hero_strength(active_dir + "btn_totem.png")
                    mana = 0
                pg.press(['right'])
                ss(active_dir + "btn_end.png")
                ss(active_dir + "btn_end2.png")
            elif hod >= 7 and game == 1:
                close_time = time.time() + delay
                while True:
                    ##bla bla
                    if unit == 0:
                        karta(active_dir + "btn_m7.png")
                        if unit == 1:
                            mana = mana - 7
                    if unit == 0:
                        pg.press(['right'])
                        karta(active_dir + "btn_m6.png")
                        if unit == 1:
                            mana = mana - 6
                    if unit == 0:
                        pg.press(['right'])
                        karta(active_dir + "btn_m5.png")
                        if unit == 1:
                            mana = mana - 5
                    if time.time() > close_time:
                        break
                if mana >= 2:
                    hero_strength(active_dir + "btn_totem.png")
                    mana = 0
                pg.press(['right'])
                ss(active_dir + "btn_end.png")
                ss(active_dir + "btn_end2.png")
            projgrysh(active_dir + "end_game.png")
            vyjgrysh(active_dir + "victory.png")
            endGame(active_dir + "end_game2.png")
            if Ggame == 0:
                fill_table()  # заполняем БД
            #               print_oll_table()
            ss(active_dir + "ok_2.png")
            ss(active_dir + "bt.png")
            ss(active_dir + "bt2.png")
        return Ggame, Ngame, Gcikl, vygr, progr, start_time, activity


def lock_standart():
    global Ggame
    global Ngame
    global Gcikl
    global game
    global hod
    global mana
    global moneta
    global tipe
    global deck
    global vygr
    global progr
    global cikl
    global unit
    global start_time
    global delay
    global activity
    tipe = 'стандарт'
    deck = 'лок'
    ss(active_dir + "btn_lock.png")
    ss(active_dir + "btn_game_st.png")
    start_game(active_dir + "btn_start.png")
    if Ggame == 1:
        Ngame += 1
        print("игра локом началась", Gcikl)
        start_time = datetime.now()  # текущие дата и время
        while Ggame == 1:
            if keyboard.is_pressed('Enter'):  # если клавиша Esc
                timer_game()  # подсчет времени
                fill_table()  # заполняем БД
                print_oll_table()
                sys.exit()  # завершаем программу
            if (time.time() - activity) >= 280:
                pointclick()
            if (time.time() - activity) >= 300:
                Ggame = 0
            Gcikl += 1
            card_selection(active_dir + "btn_ok.png")
            chughoj_hod(active_dir + "chughoj_hod.png")
            vash_hod(active_dir + "btn_end.png")
            # print("hod=", hod)
            if hod == 1 and game == 1:
                close_time = time.time() + 15
                while True:
                    ##bla bla
                    if time.time() > close_time:
                        break
                pg.press(['right'])
                simple_press(active_dir + "btn_end.png")
                simple_press(active_dir + "btn_end2.png")
            elif hod > 1 and hod < 4 and game == 1:
                close_time = time.time() + delay
                while True:
                    if unit == 0 and mana >= 3:
                        pg.press(['right'])
                        karta(active_dir + "btn_m3.png")
                        if unit == 1:
                            mana = mana - 3
                    if unit == 0 and mana >= 4:
                        pg.press(['right'])
                        karta(active_dir + "btn_m4.png")
                        if unit == 1:
                            mana = mana - 4
                    if time.time() > close_time:
                        break
                if mana >= 2:
                    pg.press(['right'])
                    simple_press(active_dir + "btn_soul.png")
                    mana = 0
                simple_press(active_dir + "btn_end.png")
                simple_press(active_dir + "btn_end2.png")
            elif hod == 4 and game == 1:
                pg.press(['right'])
                karta(active_dir + "btn_m0.png")
                if moneta == 1:
                    mana += 1
                    moneta = 0
                    pg.press(['right'])
                close_time = time.time() + delay
                while True:
                    if unit == 0 and mana >= 3:
                        pg.press(['right'])
                        karta(active_dir + "btn_m3.png")
                        if unit == 1:
                            mana = mana - 3
                    if unit == 0 and mana >= 4:
                        pg.press(['right'])
                        karta(active_dir + "btn_m4.png")
                        if unit == 1:
                            mana = mana - 4
                    if unit == 0 and mana >= 5:
                        pg.press(['right'])
                        karta(active_dir + "btn_m5.png")
                        if unit == 1:
                            mana = mana - 5
                    if time.time() > close_time:
                        break
                if mana >= 2:
                    pg.press(['right'])
                    simple_press(active_dir + "btn_soul.png")
                    mana = 0
                simple_press(active_dir + "btn_end.png")
                simple_press(active_dir + "btn_end2.png")
            elif hod == 5 and game == 1:
                close_time = time.time() + delay
                while True:
                    ##bla bla
                    if unit == 0 and mana >= 3:
                        pg.press(['right'])
                        karta(active_dir + "btn_m3.png")
                        if unit == 1:
                            mana = mana - 3
                    if unit == 0 and mana >= 4:
                        pg.press(['right'])
                        karta(active_dir + "btn_m4.png")
                        if unit == 1:
                            mana = mana - 4
                    if unit == 0 and mana >= 5:
                        pg.press(['right'])
                        karta(active_dir + "btn_m5.png")
                        if unit == 1:
                            mana = mana - 5
                    if time.time() > close_time:
                        break
                if mana >= 2:
                    pg.press(['right'])
                    simple_press(active_dir + "btn_soul.png")
                    mana = 0
                simple_press(active_dir + "btn_end.png")
                simple_press(active_dir + "btn_end2.png")
            elif hod == 6 and game == 1:
                close_time = time.time() + delay
                while True:
                    if unit == 0 and mana >= 3:
                        pg.press(['right'])
                        karta(active_dir + "btn_m3.png")
                        if unit == 1:
                            mana = mana - 3
                    if unit == 0 and mana >= 4:
                        pg.press(['right'])
                        karta(active_dir + "btn_m4.png")
                        if unit == 1:
                            mana = mana - 4
                    if unit == 0 and mana >= 5:
                        pg.press(['right'])
                        karta(active_dir + "btn_m5.png")
                        if unit == 1:
                            mana = mana - 5
                    if unit == 0 and mana >= 6:
                        pg.press(['right'])
                        karta(active_dir + "btn_m6.png")
                        if unit == 1:
                            mana = mana - 6
                    if time.time() > close_time:
                        break
                if mana >= 2:
                    pg.press(['right'])
                    simple_press(active_dir + "btn_soul.png")
                    mana = 0
                simple_press(active_dir + "btn_end.png")
                simple_press(active_dir + "btn_end2.png")
            elif hod >= 7 and game == 1:
                close_time = time.time() + delay
                while True:
                    ##bla bla
                    if unit == 0 and mana >= 3:
                        pg.press(['right'])
                        karta(active_dir + "btn_m3.png")
                        if unit == 1:
                            mana = mana - 3
                    if unit == 0 and mana >= 4:
                        pg.press(['right'])
                        karta(active_dir + "btn_m4.png")
                        if unit == 1:
                            mana = mana - 4
                    if unit == 0 and mana >= 5:
                        pg.press(['right'])
                        karta(active_dir + "btn_m5.png")
                        if unit == 1:
                            mana = mana - 5
                    if unit == 0 and mana >= 6:
                        pg.press(['right'])
                        karta(active_dir + "btn_m6.png")
                        if unit == 1:
                            mana = mana - 6
                    if unit == 0 and mana >= 7:
                        pg.press(['right'])
                        karta(active_dir + "btn_m6.png")
                        if unit == 1:
                            mana = mana - 7
                    if time.time() > close_time:
                        break
                if mana >= 2:
                    pg.press(['right'])
                    simple_press(active_dir + "btn_soul.png")
                    mana = 0
                simple_press(active_dir + "btn_end.png")
                simple_press(active_dir + "btn_end2.png")
            projgrysh(active_dir + "end_game.png")
            vyjgrysh(active_dir + "victory.png")
            endGame(active_dir + "end_game2.png")
            if Ggame == 0:
                fill_table()  # заполняем БД
            #               print_oll_table()
            ss(active_dir + "ok_2.png")
            ss(active_dir + "bt.png")
            ss(active_dir + "bt2.png")
        return Ggame, Ngame, Gcikl, vygr, progr, start_time, activity


def activity_analysis():
    global activity
    if (time.time() - activity) >= 420:
        simple_press(active_dir + "btn_gear.png")
        simple_press(active_dir + "btn_exit.png")
        simple_press(active_dir + "btn_connect_again.png")
        time.sleep(600)
    return activity


# variables (переменные)
screen_width_x = 0  # ширина экрана, координата х - максимальная
screen_height_y = 0  # высота экрана, координата у - максимальная
Ngame = 0  # подсчет количества игр !(основное тело цикла)
vygr = 0  # подсчет выйгрышей в данной сессии
progr = 0  # подсчет проигранных игр в данной сессии
Ggame = 0  # индикатор начала рейтинговой игры !start_game()-->1, endGame()-->0
Gcikl = 0  # счетчик циклов внутри игры
cikl = 1  # подсчет общего числа циклов программы
hod = 0  # учет номера хода !start_game()-->1 !chughoj_hod()-->+1
unit = 0  # количество выложенных юнитов за ход (для того что бы знать сколько выложено)
game = 0  # индикатор игры (вашего хода)
moneta = 0  # индикатор монеты в руке
mana = 0  # счетчик маны во время хода
zero = 0  # ноль
delay = 25  # вемя на свой ход
activity = time.time()  # анализ активности игрового процесса

# sys.path.append(r'D:\00. Обучение\05. Git\00. project\00.botHS\btn\800x600')
# sys.path.append(os.path.join(sys.path[0], '/btn/800x600'))
# print(os.listdir(os.getcwd()))
# print(sys.path)


# Работа с БД
conn = sqlite3.connect('mydatabase.db')  # создаем переменную conn и  соединение с нашей базой данных
c = conn.cursor()  # Создаем курсор - это специальный объект который делает запросы и получает их результаты
c.execute("""CREATE TABLE IF NOT EXISTS total(
   name_id INTEGER PRIMARY KEY,
   date DATE NOT NULL,
   startgame DATE NOT NULL,
   endgame DATE NOT NULL,
   l_days DATE NOT NULL,
   l_hours DATE NOT NULL,
   l_minuts DATE NOT NULL,
   l_seconds DATE NOT NULL,
   g_days DATE NOT NULL,
   g_hours DATE NOT NULL,
   g_minuts DATE NOT NULL,
   g_seconds DATE NOT NULL,
   tipe TEXT NOT NULL,
   deck TEXT NOT NULL,
   hod INT NOT NULL,
   localvictory INT NOT NULL,
   locallosing INT NOT NULL,
   localpercent TEXT NOT NULL,
   globalvictory INT NOT NULL,
   globallosing INT NOT NULL,
   globalpercent REAL NOT NULL);
""")
conn.commit()  # применяем изменения

# описываем параметры логирования
logging.basicConfig(filename='app.log', filemode='w', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logging.info('Start game and logged in')
# примеры логирования с разными уровнями важности
# logging.info('This is an info message')
# logging.debug('This is a debug message')
# logging.warning('This will get logged to a file')
# logging.error('This is an error message')
# logging.critical('This is a critical message')


# исполняемый код
screen_resolution()  # определяем разрешение экрана
active_dir = 'btn/' + str(screen_width_x) + 'x' + str(screen_height_y) + '/'


startlnk()  # запуск приложения Battle.net

# fill_table_start()

while "Бесконечный цикл":  # Цикл анализа
    if keyboard.is_pressed('Enter'):  # если клавиша Esc
        print_oll_table()
        sys.exit()  # завершаем программу
    cikl += 1
    # print("Цикл =", cikl)
    # print("Колличество игр ", Ngame)
    time.sleep(10)
    ss(active_dir + "00_btn_game.png")  # выбор кнопки играть в окне batlenet
    ss(active_dir + "btn_game.png")  # выбор вкладки hearthstone в основном окне
    a = random.randint(1, 2)  # рандомное число от 1 до 9
    if a == 1:
        grec_standart()
    elif a == 2:
        hant_standart()
    elif a == 3:
        voin_standart()
    elif a == 4:
        mag_standart()
    elif a == 5:
        roga_standart()
    elif a == 6:
        dh_standart()
    elif a == 7:
        druid_standart()
    elif a == 8:
        shaman_standart()
    elif a == 9:
        lock_standart()
    time.sleep(5)
    # На случай потери соединения
    ss(active_dir + "ok_2.png")
    ss(active_dir + "bt.png")
    ss(active_dir + "bt2.png")
    pointclick()
    activity_analysis()

