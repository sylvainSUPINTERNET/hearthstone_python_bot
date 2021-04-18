# python3

import subprocess  # Запуск приложений windows
import time  # работа со временем
import pyautogui as pg  # работа с картинками
import keyboard  # работа с нажатиями клавиш
import sys  # системными библиотеками
import datetime  # работа с датой и времени
from datetime import datetime
import sqlite3  # Импортируем библиотеку, соответствующую типу нашей базы данных
import random  # рандомные числа


def startlnk():  # функция запуска приложения
    subprocess.Popen('C:\Program Files (x86)\Battle.net\Battle.net Launcher.exe')  # запуск приложения
    time.sleep(2)  # время ожидания запуска battle.net


def pointclick():  # функция нажатия в цикле по координатам
    pg.doubleClick(1900, 1000)


def double_press(template, x, y, h, w):  # функция определения и двойного нажатия на координаты кнопки
    global zero, activity
    try:
        buttonx, buttony = pg.locateCenterOnScreen(template, region=(x, y, h, w), confidence=0.7)
        activity = time.time()
        pg.doubleClick(buttonx, buttony)
        return activity
    except TypeError:
        return zero


def simple_press(template, x, y, h, w):  # функция определения и одинарного нажатия на координаты кнопки
    global activity, zero
    try:
        buttonx, buttony = pg.locateCenterOnScreen(template, region=(x, y, h, w), confidence=0.7)
        activity = time.time()
        pg.click(buttonx, buttony)
        return activity
    except TypeError:
        return zero


def start_game(template):
    global hod, Gcikl, Ggame, cikl, vygr, progr, zero, vygr, progr, activity
    try:
        buttonx, buttony = pg.locateCenterOnScreen(template, region=(0, 0, 1920, 1080), confidence=0.7)
        pg.click(buttonx, buttony)
        Gcikl += 1
        hod = 1
        Ggame = 1
        cikl = 0
        vygr = 0
        progr = 0
        activity = time.time()
        return hod, Gcikl, Ggame, cikl, vygr, progr, activity
    except TypeError:
        return zero


def vash_hod(template):
    global game  # индикатор своего хода
    global zero
    global activity
    try:
        buttonx, buttony = pg.locateCenterOnScreen(template, region=(0, 0, 1920, 1080), confidence=0.7)
        if game == 0:
            game = 1
            pg.moveTo(buttonx, buttony, duration=0)
            activity = time.time()
            return game, activity
    except TypeError:
        return zero


def chughoj_hod(template):
    global game, hod, mana, zero, activity
    try:
        buttonx, buttony = pg.locateCenterOnScreen(template, region=(0, 0, 1920, 1080), confidence=0.7)
        pg.moveTo(buttonx, buttony)
        if game == 1:
            hod += 1
            game = 0
        activity = time.time()
        time.sleep(5)
        if hod < 11:
            mana = hod
        elif hod >= 11:
            mana = 10
        return game, hod, mana, activity
    except TypeError:
        return zero


# def karta(template):  # функция покупки юнита
#     global zero, unit
#     global hod
#     global game
#     global moneta
#     global mana
#     global activity
#     try:
#         buttonx, buttony = pg.locateCenterOnScreen(template, region=(0, 700, 1600, 200), confidence=0.7)
#         pg.moveTo(buttonx, buttony)
#         activity = time.time()
#         print('Нашел карту', buttonx, buttony)
#         print("unit", unit)
#         print("hod", hod)
#         pg.press(['right'])
#         if hod == 4 and unit == 0:
#             moneta = 1
#             print("Выложил монету на стол")
#             pg.moveTo(buttonx, buttony, duration=0)  # перемещение к кнопке
#             pg.mouseDown(button='left')  # нажать левую клавишу мыши
#             pg.moveTo(969, 614, duration=1)  # перемещение
#             pg.mouseUp(button='left')  # отпустить левую клавиши мыши
#         if unit == 0 and hod > 3 and game == 1 and mana >= 5:
#             print("Выложил одну карту на стол")
#             pg.moveTo(buttonx, buttony, duration=0)  # перемещение к кнопке
#             pg.mouseDown(button='left')  # нажать левую клавишу мыши
#             pg.moveTo(969, 614, duration=1)  # перемещение
#             pg.mouseUp(button='left')  # отпустить левую клавиши мыши
#             unit += 1
#         return unit, hod, game, moneta, mana, activity
#     except TypeError:
#         return zero


def projgrysh(template):
    global zero, progr, activity
    try:
        buttonx, buttony = pg.locateCenterOnScreen(template, region=(0, 0, 1920, 1080), confidence=0.7)
        progr = 1
        pg.moveTo(buttonx, buttony, duration=0)
        pg.doubleClick(buttonx, buttony)
        activity = time.time()
        return progr, activity
    except TypeError:
        return zero


def vyjgrysh(template):
    global zero, vygr, activity
    try:
        buttonx, buttony = pg.locateCenterOnScreen(template, region=(0, 0, 1920, 1080), confidence=0.7)
        pg.moveTo(buttonx, buttony)
        activity = time.time()
        vygr = 1
        pg.moveTo(buttonx, buttony, duration=0)
        pg.doubleClick(buttonx, buttony)
        time.sleep(1)
        return vygr, activity
    except TypeError:
        return zero


def endGame(template):
    global zero, Ggame, activity
    try:
        buttonx, buttony = pg.locateCenterOnScreen(template, region=(0, 0, 1600, 900), confidence=0.7)
        activity = time.time()
        pg.moveTo(buttonx, buttony)
        Ggame = 0
        pg.doubleClick(buttonx, buttony)
        time.sleep(1)
        return Ggame, activity
    except TypeError:
        return zero


def fill_table(): # заполняем строку таблицы
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
    print(result_old)

    g_days = result_old[8] + l_days  # дни
    g_hours = result_old[9] + l_hours  # часы
    g_minuts = result_old[10] + l_minuts  # минуты
    g_seconds = result_old[11] + l_seconds  # секунды

    if g_seconds >= 60:
        g_minuts = g_minuts + int(g_seconds / 60)
        g_seconds = g_seconds - (int(g_seconds / 60))*60
    if g_minuts >= 60:
        g_hours = g_hours  + int(g_minuts / 60)
        g_minuts = g_minuts - (int(g_minuts / 60))*60
    if g_hours >= 24:
        g_days = g_days  + int(g_hours / 24)
        g_hours = g_hours - (int(g_hours / 24))*24


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


def activity_analysis():
    global activity
    if (time.time() - activity) >= 420:
        simple_press("btn_gear.png")
        simple_press("btn_exit.png")
        simple_press("btn_connect_again.png")
        time.sleep(600)
    return activity



# variables (переменные)
Ngame = 0  # подсчет количества игр !(основное тело цикла)
vygr = 0  # подсчет выйгрышей в данной сессии
progr = 0  # подсчет проигранных игр в данной сессии
Ggame = 0  # индикатор начала рейтинговой игры !start_game()-->1, endGame()-->0
Gcikl = 0  # счетчик циклов внутри игры
cikl = 1  # подсчет общего числа циклов программы
hod = 0  # учет номера хода !start_game()-->1 !chughoj_hod()-->+1
game = 0  # индикатор игры (вашего хода)
mana = 0  # счетчик маны во время хода
zero = 0  # ноль
delay = 25  # вемя на свой ход
activity = time.time()  # анализ активности игрового процесса

card_hand = [None, None, None, None, None, None, None, None, None, None]
# # 1 карта в руке
# x_one = (400, 0)
# # 2 карты в руке
# x_two = (380, 420)
# # 3 карты в руке
# x_free = (300, 380, 450)
# # 4 карты в руке (1-й ход без монеты)
# x_fore = (270, 330, 390, 460)
# # 5 карт в руке
# x_five = (270, 320, 370, 420, 490)
# # 6 карт в руке (1-й ход с монетой)
# x_six = (250, 290, 330, 370, 410, 470)
# # 7 карт в руке
# x_seven = (240, 280, 315, 345, 380, 420, 480)
# # 8 карт в руке
# x_eight = (235, 265, 295, 335, 365, 395, 430, 480)
# # 9 карт в руке
# x_nine = (230, 260, 290, 320, 350, 380, 410, 440, 490)
# 10 карт в руке
x_ten = (660, 720, 765, 815, 860, 910, 950, 1000, 1050, 1130)

card_hand = None
carts_bd = ['btn/1920x1080/carts/1_demon_bezdny.png', 'btn/1920x1080/carts/1_nestabilnaja_skverna.png',
'btn/1920x1080/carts/1_temnyj_pakt.png', 'btn/1920x1080/carts/2_oskvernenie.png',
'btn/1920x1080/carts/3_obratnaja_vspyshka.png', 'btn/1920x1080/carts/3_pohischenie_gizni.png',
'btn/1920x1080/carts/4_kataklizm.png', 'btn/1920x1080/carts/6_ohotnik_heming.png',
'btn/1920x1080/carts/1_kobold_bibliotekar.png', 'btn/1920x1080/carts/2_ingener_novichok.png',
'btn/1920x1080/carts/3_bezrassudnyj_trol.png', 'btn/1920x1080/carts/2_neogidannyj_povorot.png',
'btn/1920x1080/carts/3_strela_tmy.png', 'btn/1920x1080/carts/10_meha_ktun.png',
'btn/1920x1080/carts/3_chute_na_demonov.png', 'btn/1920x1080/carts/7_princ_keltas.png',
'btn/1920x1080/carts/1_kara_ognennaja.png', 'btn/1920x1080/carts/5_kuklovod_dorian.png',
'btn/1920x1080/carts/4_adskoe_plamja.png']

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


def recognize(template, x, y, h, w):  # функция распознования карты
    global zero, activity, cart_recognize
    try:
        buttonx, buttony = pg.locateCenterOnScreen(template, region=(x, y, h, w), confidence=0.7)
        activity = time.time()
        pg.moveTo(buttonx, buttony)
        cart_recognize = 'rec'
        return activity, cart_recognize
    except TypeError:
        cart_recognize = 'dontrec'
        return zero, cart_recognize


def start_hand():
    global cart_recognize, card_hand, carts_bd
    recognize("btn/1920x1080/btn_start_hand.png", 720, 110, 450, 150)
    time.sleep(2)
    if cart_recognize == 'rec':  # на экране стартовая рука
        cart_recognize = None
        recognize("btn/1920x1080/karty_4.png", 930, 400, 70, 270)
        if cart_recognize == 'rec':  # на экране 4 карты для выбора
            time.sleep(3)
            cart_recognize = None
            x = 450  # координата первой карты 1920 1080
            y = 350
            h = 250
            w = 350
            for a in range(4):  # распознаем все 4 карты по очереди
                for cart in range(18):
                    cart_recognize = None
                    recognize(carts_bd[cart], x, y, h, w)
                    if cart_recognize == 'rec':
                        print(a, "-я карта", carts_bd[cart])
                    # else:
                    #     print('dont rec')
                x += 250
            # card_hand[5] = "moneta"
        else:  # на экране 3 карты
            x = 500  # координата первой карты 800 600
            y = 350
            h = 250
            w = 350
            for a in range(3):  # распознаем все 3 карты по очереди
                for cart in range(18):
                    cart_recognize = None
                    recognize(carts_bd[cart], x, y, h, w)
                    if cart_recognize == 'rec':
                        print(a, "-я карта", carts_bd[cart])
                    # else:
                    #     print('dont rec')
                x += 350
    simple_press("btn/1920x1080/btn_ok.png", 1300, 800, 230, 230)
    return card_hand


def lock_wild():
    global Ggame, Ngame, Gcikl, game, hod, mana, moneta, tipe, deck, vygr
    global progr, cikl, unit, start_time, activity, card_hand
    tipe = 'вольный'
    deck = 'лок'
    simple_press("btn/1920x1080/btn_game.png", 840, 300, 300, 80)
    simple_press("btn/1920x1080/lock.png", 350, 230, 270, 125)
    start_game("btn/1920x1080/btn_play.png")
    if Ggame == 1:
        Ngame += 1
        start_time = datetime.now()  # текущие дата и время
        while Ggame == 1:
            if (time.time() - activity) >= 280:
                pointclick()
            if (time.time() - activity) >= 300:
                Ggame = 0
            Gcikl += 1
            simple_press("btn/1920x1080/btn_start.png", 760, 160, 400, 70)
            start_hand()
            chughoj_hod("btn/1920x1080/chughoj_hod.png")
            vash_hod("btn/1920x1080/btn_end.png")

            if game == 1:
                if hod == 1:
                    close_time = time.time() + 15
                    while True:
                        if time.time() > close_time:
                            break
                #     if card_hand[5] == "moneta":  # в руке 6 карт с монетой
                #         pg.press(['right'])
                #         x = x_six[4]
                #         pg.moveTo(x, 600)
                #         karta("btn/800x600/moneta.png") # выложил монету осталось 5 карт
                #         mana = 2
                #         for a in range(0, 10):
                #             if card_hand[a] == 'rec' and mana > 1:
                #                 x = x_five[a]
                #                 pg.moveTo(x, 600)
                #                 karta("btn/800x600/pryg_skoker.png")
                #             elif card_hand[a] == 'rec' and mana == 1:
                #                 x = x_fore[a]
                #                 pg.moveTo(x, 600)
                #                 karta("btn/800x600/pryg_skoker.png")
                #     else:
                #         mana = 1
                #         for a in range(0, 10):
                #             if card_hand[a] == 'rec' and mana == 1:
                #                 x = x_fore[a]
                #                 pg.moveTo(x, 600)
                #                 karta("btn/800x600/pryg_skoker.png")
                #                 mana = 0
                #     pg.press(['right'])
                #     simple_press("btn/800x600/btn_end.png")
                #     simple_press("btn/800x600/btn_end2.png")
                # if hod > 1:
                #     close_time = time.time() + 15
                #     while True:
                #         if time.time() > close_time:
                #             break
                #         pg.press(['right'])
                #         for a in range(0, 10):
                #             pg.moveTo(x_ten[a], 600)
                #             time.sleep(1)
                #             karta("btn/800x600/pryg_skoker.png")
                #     pg.press(['right'])
                #     simple_press("btn/800x600/btn_end.png")
                #     simple_press("btn/800x600/btn_end2.png")
            projgrysh("btn/800x600/end_game.png")
            vyjgrysh("btn/800x600/victory.png")
            endGame("btn/800x600/end_game2.png")
            if Ggame == 0:
                fill_table()  # заполняем БД

        return Ggame, Ngame, Gcikl, vygr, progr, start_time, activity


# исполняемый код
startlnk()  # запуск приложения Battle.net
while "Бесконечный цикл":  # Цикл анализа
    time.sleep(5)
    simple_press('btn/1920x1080/00_btn_game.png', 300, 800, 400, 300)
    simple_press("btn/1920x1080/btn_game.png", 800, 290, 300, 100)
    lock_wild()
    pointclick()
    activity_analysis()
