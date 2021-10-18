# python3
# bot for hearthstoune rejting game

import datetime  # работа с датой и времени
import sqlite3  # Импортируем библиотеку, соответствующую типу нашей базы данных
import os  # для работы с командной строкой (определение экрана)
import logging  # модуль логирования
import time  # работа со временем
from datetime import datetime
import pyautogui as pg  # работа с картинками

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

def hero_strength(template):  # функция силы героя воин
    global zero, activity, screen_width_x, screen_height_y
    try:
        buttonx, buttony = pg.locateCenterOnScreen(template, region=(0, int(screen_height_y * 0.7), screen_width_x, int(screen_height_y * 0.3)), confidence=0.7)
        activity = time.time()
        pg.moveTo(buttonx, buttony)
        pg.doubleClick(buttonx, buttony)
        time.sleep(1)
        return activity
    except TypeError:
        print('сила не найдена')
        return zero

def simple_press(template):  # функция одинарного нажатия
    global activity, zero, screen_width_x, screen_height_y
    try:
        buttonx, buttony = pg.locateCenterOnScreen(template, region=(0, 0, screen_width_x, screen_height_y), confidence=0.7)
        activity = time.time()
        pg.moveTo(buttonx, buttony)
        pg.click(buttonx, buttony)
        time.sleep(1)
        return activity
    except TypeError:
        return zero

def card_selection(template):  # функция выбора стартовой руки
    global activity, screen_width_x, screen_height_y, one_mana_st, card_ok
    try:
        buttonx, buttony = pg.locateCenterOnScreen(template, region=(0, 0, screen_width_x, screen_height_y), confidence=0.7)
        logging.info('Start hand ok')  # запись в файл лога
        pg.moveTo(int(screen_width_x * 0.31), screen_height_y * 0.5)  # убираем первую карту
        pg.click(int(screen_width_x * 0.31), screen_height_y * 0.5)
        pg.moveTo(int(screen_width_x * 0.43), screen_height_y * 0.5)  # убираем вторую карту
        pg.click(int(screen_width_x * 0.43), screen_height_y * 0.5)
        pg.moveTo(int(screen_width_x * 0.5), screen_height_y * 0.5)  # убираем третью карту
        pg.click(int(screen_width_x * 0.5), screen_height_y * 0.5)
        pg.moveTo(int(screen_width_x * 0.57), screen_height_y * 0.5)  # убираем четвертую карту
        pg.click(int(screen_width_x * 0.57), screen_height_y * 0.5)
        pg.moveTo(int(screen_width_x * 0.7), screen_height_y * 0.5)  # убираем пятую карту
        pg.click(int(screen_width_x * 0.7), screen_height_y * 0.5)

        for one in one_mana_st:  # перебираем все карты за 1 маны
            # print(one)
            # print('карта - ' + str(one) + ':  мана -' + str(one_mana_st[one]))
            # print(active_dir + 'carts/' + str(one))  # отображение текущей карты в поиске
            simple_press(active_dir + 'carts/' + str(one))

        pg.moveTo(buttonx, buttony)  # переходим к ожиданию на кнопке ок
        time.sleep(45)
        pg.click(buttonx, buttony)
        card_ok = 1
        activity = time.time()
        return activity, card_ok
    except TypeError:
        return zero

def start_game(template):  # функция определения поиска противника
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
        buttonx, buttony = pg.locateCenterOnScreen(template, region=(0, 0, screen_width_x, screen_height_y), confidence=0.7)
        pg.moveTo(buttonx, buttony)
        Gcikl += 1
        hod = 1
        #print('Нашел активную игру')
        logging.info('Start game')
        Ggame = 1
        cikl = 0
        vygr = 0
        progr = 0
        activity = time.time()
        time.sleep(1)
        return hod, Gcikl, Ggame, cikl, vygr, progr, activity
    except TypeError:
        print('НЕ нашел активную игру')
        return zero

def vash_hod(template):
    global game  # индикатор своего хода
    global zero, game, unit, hod, mana
    global activity, screen_width_x, screen_height_y
    try:
        buttonx, buttony = pg.locateCenterOnScreen(template, region=(0, 0, screen_width_x, screen_height_y), confidence=0.7)
        if game == 0 and card_ok:
            game = 1
            pg.moveTo(buttonx, buttony, duration=0)
            activity = time.time()
            if hod == 1:
                hod_1()
            elif hod == 2:
                hod_2()
            elif hod == 3:
                hod_3()
            elif hod == 4:
                hod_4()
            elif hod == 5:
                hod_5()
            elif hod == 6:
                hod_6()
            elif hod == 7:
                hod_7()
            elif hod == 8:
                hod_8()
            elif hod == 9:
                hod_9()
            elif hod >= 10:
                hod_10()
            return game, activity
    except TypeError:
        return zero

def hod_1():
    global card_position, unit
    time.sleep(5)
    for card in card_position:
        print(card, screen_height_y)
        pg.moveTo(card, screen_height_y-20)

        for one in one_mana_h:  # перебираем все карты за 1 маны
            print(active_dir + 'carts/' + str(one))
            time.sleep(0.1)
            karta(active_dir + 'carts/' + str(one))
            if unit == 1:
                pointclick()
                break
    if unit != 1:
        for card in card_position:
            pg.moveTo(card, screen_height_y-20)
            karta(active_dir + 'carts/00_moneta_h.png')
            pointclick()
            if unit == 1:
                hero_strength(active_dir + 'big_schit.png')
                pointclick()
            break

def hod_2():
    print(active_dir + 'big_schit.png')
    hero_strength(active_dir + 'big_schit.png')
    pointclick()

def hod_3():
    global card_position, unit
    for card in card_position:
        pg.moveTo(card, screen_height_y-20)

        for one in three_mana_h:  # перебираем все карты за 1 маны
            print(active_dir + 'carts/' + str(one))
            karta(active_dir + 'carts/' + str(one))
            if unit == 1:
                pointclick()
                break

    if unit != 1:
        for card in card_position:
            pg.moveTo(card, screen_height_y-20)

            for one in one_mana_h:  # перебираем все карты за 1 маны
                # print(active_dir + 'carts/' + str(one))
                karta(active_dir + 'carts/' + str(one))
                if unit == 1:
                    hero_strength(active_dir + 'big_schit.png')
                    pointclick()
                    break
        if unit != 1:
            hero_strength(active_dir + 'big_schit.png')
            pointclick()

def hod_4():
    global card_position, unit
    for card in card_position:
        pg.moveTo(card, screen_height_y-20)

        for one in three_mana_h:  # перебираем все карты за 1 маны
            # print(active_dir + 'carts/' + str(one))
            karta(active_dir + 'carts/' + str(one))
            if unit == 1:
                pointclick()
                break

    if unit != 1:
        for card in card_position:
            pg.moveTo(card, screen_height_y-20)

            for one in one_mana_h:  # перебираем все карты за 1 маны
                # print(active_dir + 'carts/' + str(one))
                karta(active_dir + 'carts/' + str(one))
                if unit == 1:
                    hero_strength(active_dir + 'big_schit.png')
                    pointclick()
                    break
        if unit != 1:
            hero_strength(active_dir + 'big_schit.png')
            pointclick()

def hod_5():
    global card_position, unit
    for card in card_position:
        pg.moveTo(card, screen_height_y-20)

        for one in five_mana_h:  # перебираем все карты за 1 маны
            # print(active_dir + 'carts/' + str(one))
            karta(active_dir + 'carts/' + str(one))
            if unit == 1:
                pointclick()
                break

    if unit != 1:
        for card in card_position:
            pg.moveTo(card, screen_height_y-20)

            for one in three_mana_h:  # перебираем все карты за 1 маны
                # print(active_dir + 'carts/' + str(one))
                karta(active_dir + 'carts/' + str(one))
                if unit == 1:
                    pointclick()
                    hero_strength(active_dir + 'big_schit.png')
                    break

            for one in one_mana_h:  # перебираем все карты за 1 маны
                # print(active_dir + 'carts/' + str(one))
                karta(active_dir + 'carts/' + str(one))
                if unit == 1:
                    hero_strength(active_dir + 'big_schit.png')
                    pointclick()
                    break
        if unit != 1:
            hero_strength(active_dir + 'big_schit.png')
            pointclick()

def hod_6():
    global card_position, unit
    for card in card_position:
        pg.moveTo(card, screen_height_y-20)

        for one in five_mana_h:  # перебираем все карты за 1 маны
            # print(active_dir + 'carts/' + str(one))
            karta(active_dir + 'carts/' + str(one))
            if unit == 1:
                pointclick()
                break

    if unit != 1:
        for card in card_position:
            pg.moveTo(card, screen_height_y-20)

            for one in three_mana_h:  # перебираем все карты за 1 маны
                print(active_dir + 'carts/' + str(one))
                karta(active_dir + 'carts/' + str(one))
                if unit == 1:
                    pointclick()
                    hero_strength(active_dir + 'big_schit.png')
                    break

            for one in one_mana_h:  # перебираем все карты за 1 маны
                print(active_dir + 'carts/' + str(one))
                karta(active_dir + 'carts/' + str(one))
                if unit == 1:
                    hero_strength(active_dir + 'big_schit.png')
                    pointclick()
                    break
        if unit != 1:
            hero_strength(active_dir + 'big_schit.png')
            pointclick()

def hod_7():
    global card_position, unit
    for card in card_position:
        pg.moveTo(card, screen_height_y-20)

        for one in seven_mana_h:  # перебираем все карты за 1 маны
            # print(active_dir + 'carts/' + str(one))
            karta(active_dir + 'carts/' + str(one))
            if unit == 1:
                pointclick()
                break

    if unit != 1:
        for card in card_position:
            pg.moveTo(card, screen_height_y-20)

            for one in five_mana_h:  # перебираем все карты за 1 маны
                # print(active_dir + 'carts/' + str(one))
                karta(active_dir + 'carts/' + str(one))
                if unit == 1:
                    pointclick()
                    hero_strength(active_dir + 'big_schit.png')
                    break

            for one in three_mana_h:  # перебираем все карты за 1 маны
                # print(active_dir + 'carts/' + str(one))
                karta(active_dir + 'carts/' + str(one))
                if unit == 1:
                    pointclick()
                    hero_strength(active_dir + 'big_schit.png')
                    break

            for one in one_mana_h:  # перебираем все карты за 1 маны
                # print(active_dir + 'carts/' + str(one))
                karta(active_dir + 'carts/' + str(one))
                if unit == 1:
                    hero_strength(active_dir + 'big_schit.png')
                    pointclick()
                    break
        if unit != 1:
            hero_strength(active_dir + 'big_schit.png')
            pointclick()

def hod_8():
    global card_position, unit
    for card in card_position:
        pg.moveTo(card, screen_height_y-20)

        for one in seven_mana_h:  # перебираем все карты за 1 маны
            # print(active_dir + 'carts/' + str(one))
            karta(active_dir + 'carts/' + str(one))
            if unit == 1:
                pointclick()
                break

    if unit != 1:
        for card in card_position:
            pg.moveTo(card, screen_height_y-20)

            for one in five_mana_h:  # перебираем все карты за 1 маны
                # print(active_dir + 'carts/' + str(one))
                karta(active_dir + 'carts/' + str(one))
                if unit == 1:
                    pointclick()
                    hero_strength(active_dir + 'big_schit.png')
                    break

            for one in three_mana_h:  # перебираем все карты за 1 маны
                # print(active_dir + 'carts/' + str(one))
                karta(active_dir + 'carts/' + str(one))
                if unit == 1:
                    pointclick()
                    hero_strength(active_dir + 'big_schit.png')
                    break

            for one in one_mana_h:  # перебираем все карты за 1 маны
                # print(active_dir + 'carts/' + str(one))
                karta(active_dir + 'carts/' + str(one))
                if unit == 1:
                    hero_strength(active_dir + 'big_schit.png')
                    pointclick()
                    break
        if unit != 1:
            hero_strength(active_dir + 'big_schit.png')
            pointclick()

def hod_9():
    global card_position, unit
    for card in card_position:
        pg.moveTo(card, screen_height_y-20)

        for one in nine_mana_h:  # перебираем все карты за 1 маны
            print(active_dir + 'carts/' + str(one))
            karta(active_dir + 'carts/' + str(one))
            if unit == 1:
                pointclick()
                break

    if unit != 1:
        for card in card_position:
            pg.moveTo(card, screen_height_y-20)

            for one in seven_mana_h:  # перебираем все карты за 1 маны
                # print(active_dir + 'carts/' + str(one))
                karta(active_dir + 'carts/' + str(one))
                if unit == 1:
                    pointclick()
                    hero_strength(active_dir + 'big_schit.png')
                    break

            for one in five_mana_h:  # перебираем все карты за 1 маны
                # print(active_dir + 'carts/' + str(one))
                karta(active_dir + 'carts/' + str(one))
                if unit == 1:
                    pointclick()
                    hero_strength(active_dir + 'big_schit.png')
                    break

            for one in three_mana_h:  # перебираем все карты за 1 маны
                # print(active_dir + 'carts/' + str(one))
                karta(active_dir + 'carts/' + str(one))
                if unit == 1:
                    pointclick()
                    hero_strength(active_dir + 'big_schit.png')
                    break

            for one in one_mana_h:  # перебираем все карты за 1 маны
                # print(active_dir + 'carts/' + str(one))
                karta(active_dir + 'carts/' + str(one))
                if unit == 1:
                    hero_strength(active_dir + 'big_schit.png')
                    pointclick()
                    break
        if unit != 1:
            hero_strength(active_dir + 'big_schit.png')
            pointclick()

def hod_10():
    global card_position, unit
    for card in card_position:
        pg.moveTo(card, screen_height_y-20)

        for one in nine_mana_h:  # перебираем все карты за 1 маны
            # print(active_dir + 'carts/' + str(one))
            karta(active_dir + 'carts/' + str(one))
            if unit == 1:
                pointclick()
                break

    if unit != 1:
        for card in card_position:
            pg.moveTo(card, screen_height_y-20)

            for one in seven_mana_h:  # перебираем все карты за 1 маны
                # print(active_dir + 'carts/' + str(one))
                karta(active_dir + 'carts/' + str(one))
                if unit == 1:
                    pointclick()
                    hero_strength(active_dir + 'big_schit.png')
                    break

            for one in five_mana_h:  # перебираем все карты за 1 маны
                # print(active_dir + 'carts/' + str(one))
                karta(active_dir + 'carts/' + str(one))
                if unit == 1:
                    pointclick()
                    hero_strength(active_dir + 'big_schit.png')
                    break

            for one in three_mana_h:  # перебираем все карты за 1 маны
                # print(active_dir + 'carts/' + str(one))
                karta(active_dir + 'carts/' + str(one))
                if unit == 1:
                    pointclick()
                    hero_strength(active_dir + 'big_schit.png')
                    break

            for one in one_mana_h:  # перебираем все карты за 1 маны
                # print(active_dir + 'carts/' + str(one))
                karta(active_dir + 'carts/' + str(one))
                if unit == 1:
                    hero_strength(active_dir + 'big_schit.png')
                    pointclick()
                    break
        if unit != 1:
            hero_strength(active_dir + 'big_schit.png')
            pointclick()

def chughoj_hod(template):
    global game, unit, hod, mana, zero
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
        buttonx, buttony = pg.locateCenterOnScreen(template, region=(0, int(screen_height_y * 0.5), screen_width_x, int(screen_height_y * 0.5)), confidence=0.7)
        pg.moveTo(buttonx, screen_height_y-20)
        print('карта найдена', buttonx, 'x', buttony)
        activity = time.time()
        pg.mouseDown(button='left')  # нажать левую клавишу мыши
        pg.moveTo(screen_width_x / 2, screen_height_y / 2, duration=1)  # перемещение
        pg.mouseUp(button='left')  # отпустить левую клавиши мыши
        unit = 1
        return unit, hod, game, moneta, mana, activity
    except TypeError:
        print("карта не найдена")
        return zero

def projgrysh(template):
    global zero
    global progr
    global activity, screen_width_x, screen_height_y
    try:
        buttonx, buttony = pg.locateCenterOnScreen(template, region=(0, 0, screen_width_x, screen_height_y), confidence=0.7)
        pg.moveTo(buttonx, buttony)
        # print(buttonx, buttony)
        logging.info('Losing!')  # запись в логфайл
        progr = 1
        pg.moveTo(buttonx, buttony, duration=0)
        # pg.doubleClick(buttonx, buttony)
        activity = time.time()
        time.sleep(1)
        return progr, activity
    except TypeError:
        return zero

def vyjgrysh(template):
    global zero
    global vygr
    global activity, screen_width_x, screen_height_y
    try:
        buttonx, buttony = pg.locateCenterOnScreen(template, region=(0, 0, screen_width_x, screen_height_y), confidence=0.7)
        # print(buttonx, buttony)
        logging.info('victory!')  # запись в логфайл
        activity = time.time()
        vygr = 1
        pg.moveTo(buttonx, buttony, duration=0)
        # pg.doubleClick(buttonx, buttony)
        time.sleep(1)
        return vygr, activity
    except TypeError:
        return zero

def endGame(template):
    global zero
    global Ggame
    global activity, screen_width_x, screen_height_y
    try:
        buttonx, buttony = pg.locateCenterOnScreen(template, region=(0, 0, screen_width_x, screen_height_y), confidence=0.7)
        activity = time.time()
        pg.moveTo(buttonx, buttony)
        # print(buttonx, buttony)
        Ggame = 0
        # print("Конец игры")
        # pg.doubleClick(buttonx, buttony)
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

    logging.info('End game')  # запись в логфайл

    c.execute("""INSERT INTO total(date, startgame, endgame, l_days, l_hours, l_minuts, l_seconds, 
                g_days, g_hours, g_minuts, g_seconds, tipe, deck, hod, localvictory, locallosing,
                    localpercent, globalvictory, globallosing, globalpercent) 
                    VALUES(?, ?, ?, ?, ?, ? , ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ? , ?, ?);""",
              (date, startgame, endgame, l_days, l_hours, l_minuts, l_seconds,
               g_days, g_hours, g_minuts, g_seconds, tipe, deck, hod, localvictory, locallosing,
               localpercent, globalvictory, globallosing, globalpercent))
    conn.commit()

def activity_analysis():
    global activity, active_dir
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
card_ok = 0  # говорит о том что выбор стартовой руки состоялся
activity = time.time()  # анализ активности игрового процесса

one_mana_st = dict.fromkeys(['01_geleznaja_shkura_st.png', '01_elemental_st.png', '01_shitonosec_st.png', '01_soldat_st.png'], 1)
one_mana_h = dict.fromkeys(['01_geleznaja_shkura_h.png', '01_shitonosec_h.png', '01_soldat_h.png', '01_elemental_h.png',
                            '01_torgovka_h.png'], 1)
three_mana_h = dict.fromkeys(['03_block_h.png', '03_kobold_h.png', '03_laty_h.png', '03_agent_h.png',
                              '03_lord_h.png', '03_mantija_h.png', '03_vladyka_h.png',
                              '03_smoljanoj_strag_h.png', '03_storog_h.png'], 3)
five_mana_h = dict.fromkeys(['05_golem_h.png', '05_potasovka_h.png'], 5)
seven_mana_h = dict.fromkeys(['07_duh_h.png'], 7)
nine_mana_h = dict.fromkeys(['09_baku.png'], 9)




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

screen_resolution()  # определяем разрешение экрана
active_dir = 'btn/' + str(screen_width_x) + 'x' + str(screen_height_y) + '/'
card_position = (int(screen_width_x * 0.35), int(screen_width_x * 0.38), int(screen_width_x * 0.41), int(screen_width_x * 0.45),
                 int(screen_width_x * 0.47), int(screen_width_x * 0.5), int(screen_width_x * 0.53), int(screen_width_x * 0.55),
                 int(screen_width_x * 0.59))

def voin_vild_deck():
    global Ggame, Ngame, Gcikl, game, hod, mana, moneta, tipe, deck, vygr, progr
    global cikl, unit, start_time, delay, activity

    tipe = 'вольный'
    deck = 'воин'
    cikl += 1
    time.sleep(1)
    ss(active_dir + "00_btn_game.png")  # выбор кнопки играть в окне batlenet
    ss(active_dir + "btn_game.png")  # выбор вкладки hearthstone в основном окне
    time.sleep(1)
    ss(active_dir + "btn_standart.png")  # если сейчас выбран стандарт
    ss(active_dir + "btn_vild_choise.png")  # то переключаемся в вольный
    ss(active_dir + "btn_left.png")  # переходим в левое окно с колодами
    ss(active_dir + "btn_left.png")  # переходим в левое окно с колодами
    ss(active_dir + "voin_vild.png")  # вабираем колоду вольного воина
    ss(active_dir + "btn_game_st.png")  # нажимаем кнопку старт
    start_game(active_dir + "btn_start.png")  # пошел выбор противника, игра активна
    if Ggame == 1:
        Ngame += 1
        #print("Игра воином началась", Gcikl)
        start_time = datetime.now()  # текущие дата и время
        while Ggame == 1:  # проверка активности в игре
            if (time.time() - activity) >= 280:
                pointclick()
            if (time.time() - activity) >= 300:
                Ggame = 0
            Gcikl += 1
            card_selection(active_dir + "btn_ok.png")  # выбор стартовой руки
            chughoj_hod(active_dir + "chughoj_hod.png")
            # print("hod=", hod)
            # окончание игры
            vyjgrysh(active_dir + "victory.png")
            projgrysh(active_dir + "end_game.png")

            endGame(active_dir + "end_game2.png")
            if Ggame == 0:
                fill_table()  # заполняем БД
            ss(active_dir + "ok_2.png")
            ss(active_dir + "bt.png")
            ss(active_dir + "bt2.png")
            vash_hod(active_dir + "btn_end.png")
        return Ggame, Ngame, Gcikl, vygr, progr, start_time, activity
    pointclick()
    activity_analysis()