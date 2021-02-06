# python3


import datetime  # работа с датой и времени
import sqlite3  # Импортируем библиотеку, соответствующую типу нашей базы данных
import subprocess  # Запуск приложений windows
import sys
import time  # работа со временем
from datetime import datetime
import random
import keyboard  # работа с нажатиями клавиш
import pyautogui as pg  # работа с картинками


def startlnk():  # функция запуска приложения
    subprocess.Popen("E:\soft\\battle.net\Battle.net\Battle.net Launcher.exe")
    # subprocess.Popen('C:\Program Files (x86)\Battle.net\Battle.net Launcher.exe -w 800 -h 600')  # запуск приложения
    time.sleep(2)  # время ожидания запуска battle.net


def pointclick():  # функция произвольного нажатия в цикле
    pg.doubleClick(750, 80)


def ss(template):  # функция определения и двойного нажатия на координаты кнопки
    global zero, activity
    try:
        buttonx, buttony = pg.locateCenterOnScreen(template, region=(0, 0, 1920, 1080), confidence=0.7)
        activity = time.time()
        pg.moveTo(buttonx, buttony)
        pg.doubleClick(buttonx, buttony)
        time.sleep(1)
        return activity
    except TypeError:
        return zero


def karta(template):  # функция покупки юнита
    global zero
    global activity
    try:
        buttonx, buttony = pg.locateCenterOnScreen(template, region=(0, 300, 800, 300), confidence=0.7)
        pg.moveTo(buttonx, buttony)
        activity = time.time()
        pg.moveTo(buttonx, buttony, duration=0)  # перемещение к кнопке
        pg.mouseDown(button='left')  # нажать левую клавишу мыши
        pg.moveTo(400, 310, duration=1)  # перемещение
        pg.mouseUp(button='left')  # отпустить левую клавиши мыши
        pg.press(['right'])
        return activity
    except TypeError:
        return zero


def bony_go(template, hod):  # функция выбора карт
    global activity
    try:
        if hod == 1: # 4 карты 280. 345. 410. 480   или 5 карт  500. 430. 370. 320. 270
            pg.moveTo(500, 600)
            karta('btn/800x600/btn_moneta.png')
            pg.moveTo(410, 600)
            karta('btn/800x600/btn_pryg_skok.png')
            pg.moveTo(345, 600)
            karta('btn/800x600/btn_pryg_skok.png')
            pg.moveTo(280, 600)
            karta('btn/800x600/btn_pryg_skok.png')


        activity = time.time()
        time.sleep(1)
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
    global activity
    try:
        buttonx, buttony = pg.locateCenterOnScreen(template, region=(0, 0, 800, 600), confidence=0.7)
        pg.moveTo(buttonx, buttony)
        # print(buttonx, buttony)
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
    global activity
    try:
        buttonx, buttony = pg.locateCenterOnScreen(template, region=(0, 0, 800, 600), confidence=0.7)
        if game == 0:
            game = 1
            # print("Старт хода")
            pg.moveTo(buttonx, buttony, duration=0)
            activity = time.time()
            time.sleep(1)
            pg.moveTo(750, 500)
            return game, activity
    except TypeError:
        return zero


def chughoj_hod(template):
    global game
    global unit
    global hod
    global mana
    global zero
    global activity
    try:
        buttonx, buttony = pg.locateCenterOnScreen(template, region=(0, 0, 800, 600), confidence=0.7)
        pg.moveTo(buttonx, buttony)
        # print(buttonx, buttony)
        if game == 1:
            hod += 1
            game = 0
            unit = 0
        # print("Ход противника")
        activity = time.time()
        time.sleep(5)
        pg.moveTo(750, 500)
        if hod < 11:
            mana = hod
        elif hod >= 11:
            mana = 10
        return game, unit, hod, mana, activity
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


def activity_analysis():
    global activity
    if (time.time() - activity) >= 420:
        simple_press("btn/800x600/btn_gear.png")
        simple_press("btn/800x600/btn_exit.png")
        simple_press("btn/800x600/btn_connect_again.png")
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
unit = 0  # количество выложенных юнитов за ход (для того что бы знать сколько выложено)
game = 0  # индикатор игры (вашего хода)
moneta = 0  # индикатор монеты в руке
mana = 0  # счетчик маны во время хода
zero = 0  # ноль
delay = 25  # вемя на свой ход
cart_recognize = None
activity = time.time()  # анализ активности игрового процесса
card_hand = {a: None for a in range(10)}

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

# fill_table_start()

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
    global cart_recognize
    recognize("btn/800x600/btn_start_hand.png", 250, 50, 350, 100)
    time.sleep(2)
    if cart_recognize == 'rec':  # на экране стартовая рука
        cart_recognize = None
        recognize("btn/800x600/4_karty.png", 380, 190, 50, 200)
        if cart_recognize == 'rec':  # на экране 4 карты для выбора
            cart_recognize = None
            x = 120  # координата первой карты 800 600
            y = 190
            # x = 680  # координаты первой карты при 1920 на 1080
            # y = 430
            h = 140
            w = 200
            for a in range(4):  # распознаем все 4 карты по очереди
                cart_recognize = None
                recognize("btn/800x600/v_pryg.png", x, y, h, w)
                card_hand[a] = cart_recognize
                if cart_recognize == 'dontrec':
                    pg.moveTo(x + h / 2, y + w / 2)
                    pg.press(['left'])
                x += 140
            card_hand[5] = "moneta"
        else:  # на экране 3 карты
            for a in range(3):  # распознаем все 3 карты по очереди
                cart_recognize = None
                x = 140  # координата первой карты 800 600
                y = 190
                # x = 710  # координаты первой карты при 1920 на 1080
                # y = 430
                h = 140
                w = 200
                if a == 0:  # 1 карта
                    recognize("btn/800x600/v_pryg.png", x, y, h, w)
                    card_hand[a] = cart_recognize
                    if cart_recognize == 'dontrec':
                        pg.moveTo(x + h / 2, y + w / 2)
                        pg.press(['left'])
                    cart_recognize = None
                if a == 1:
                    recognize("btn/800x600/v_pryg.png", 330, y, h, w)
                    card_hand[a] = cart_recognize
                    if cart_recognize == 'dontrec':
                        pg.moveTo(x + h / 2, y + w / 2)
                        pg.press(['left'])
                    cart_recognize = None
                if a == 2:
                    recognize("btn/800x600/v_pryg.png", 520, y, h, w)
                    card_hand[a] = cart_recognize
                    if cart_recognize == 'dontrec':
                        pg.moveTo(x + h / 2, y + w / 2)
                        pg.press(['left'])
                    cart_recognize = None
    ss("btn/800x600/btn_ok.png")
    return card_hand


def roga_potasovka():
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
    global activity
    tipe = 'потасовка'
    deck = 'рога'
    ss("btn/800x600/btn_potasovka.png")
    start_game("btn/800x600/btn_potasovka_play.png")

    if Ggame == 1:
        Ngame += 1
        start_time = datetime.now()  # текущие дата и время
        while Ggame == 1:
            if (time.time() - activity) >= 280:
                pointclick()
            if (time.time() - activity) >= 300:
                Ggame = 0
            Gcikl += 1
            ss("btn/800x600/btn_start.png")
            start_hand()
            chughoj_hod("btn/800x600/chughoj_hod.png")
            vash_hod("btn/800x600/btn_end.png")
            print("hod=", hod)
            if game == 1:
                if hod == 1:
                    close_time = time.time() + 15
                    while True:
                        if time.time() > close_time:
                            break
                    if card_hand[5] == "moneta": # в руке 6 карт с монетой



                    pg.press(['right'])
                    simple_press("btn/800x600/btn_end.png")
                    simple_press("btn/800x600/btn_end2.png")




                pg.press(['right'])
                simple_press("btn/800x600/btn_end.png")
                simple_press("btn/800x600/btn_end2.png")

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
    ss('btn/800x600/00_btn_game.png')
    ss("btn/800x600/btn_game.png")
    roga_potasovka()
    ss("btn/800x600/bt.png")
    ss("btn/800x600/bt2.png")
    pointclick()
    activity_analysis()



