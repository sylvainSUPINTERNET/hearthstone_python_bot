# python3
import subprocess  # Запуск приложений windows
import time  # работа со временем
import pyautogui as pg # работа с картинками
import keyboard # работа с нажатиями клавиш
import sys #  системными библиотеками
import datetime # работа с датой и времени
import sqlite3 # Импортируем библиотеку, соответствующую типу нашей базы данных
import random # рандомные числа


def startlnk():  # функция запуска приложения
    subprocess.Popen('C:\Program Files (x86)\Battle.net\Battle.net Launcher.exe')  # запуск приложения
    time.sleep(2)  # время ожидания запуска battle.net


def pointclick():  # функция произвольного нажатия в цикле
    pg.doubleClick(1599, 524)


def ss(template):  # функция определения и двойного нажатия на координаты кнопки
#    global zero
    try:
        buttonx, buttony = pg.locateCenterOnScreen(template, region=(0, 0, 1600, 900), confidence=0.7) 
        pg.moveTo(buttonx, buttony)
        pg.doubleClick(buttonx, buttony)
        print(buttonx, buttony)
        time.sleep(2)
    except TypeError:
        return zero


def start_game(template):
    global hod
    global Gcikl
    global Ggame
    global cikl
    global zero
    try:
        buttonx, buttony = pg.locateCenterOnScreen(template, region=(0, 0, 1600, 900), confidence=0.7) 
        pg.moveTo(buttonx, buttony)
        print(buttonx, buttony)
        Gcikl += 1
        hod = 1
        Ggame = 1
        cikl = 0
        print("Старт игры")
        time.sleep(15)
        return hod, Gcikl, Ggame, cikl
    except TypeError:
        return zero


def vash_hod(template):
    global game #индикатор своего хода
    global zero
    try:
        buttonx, buttony = pg.locateCenterOnScreen(template, region=(0, 0, 1600, 900), confidence=0.7) 
        if game == 0:
            game = 1
            print("Старт хода")  
            pg.moveTo(buttonx, buttony, duration=0)                     
            time.sleep(5)
            return game
    except TypeError:
        return zero


def chughoj_hod(template):
    global game
    global unit
    global hod
    global mana
    global zero
    try:
        buttonx, buttony = pg.locateCenterOnScreen(template, region=(0, 0, 1600, 900), confidence=0.7) 
        pg.moveTo(buttonx, buttony)
        print(buttonx, buttony)
        if game == 1:
            hod += 1
            game = 0
            unit = 0
        print("Ход противника")                  
        time.sleep(5)
        if hod < 11:
            mana = hod
        elif hod >= 11:
            mana = 10
        return game, unit, hod, mana
    except TypeError:
        return zero


def karta(template):  # функция покупки юнита
    global zero
    global unit
    global hod
    global game
    global moneta
    global mana
    try:
        buttonx, buttony = pg.locateCenterOnScreen(template, region=(0, 700, 1600, 200), confidence=0.7)
        pg.moveTo(buttonx, buttony)
        print('Нашел карту', buttonx, buttony)
        print("unit", unit)
        print("hod", hod)
        pg.press(['right'])
        if hod == 4 and unit == 0:
            moneta = 1
            print("Выложил монету на стол")
            pg.moveTo(buttonx, buttony, duration=0)  # перемещение к кнопке
            pg.mouseDown(button='left')  # нажать левую клавишу мыши
            pg.moveTo(969, 614, duration=1)  # перемещение
            pg.mouseUp(button='left')  # отпустить левую клавиши мыши
        if unit == 0 and hod > 3 and game == 1 and mana >= 5:
            print("Выложил одну карту на стол")
            pg.moveTo(buttonx, buttony, duration=0)  # перемещение к кнопке
            pg.mouseDown(button='left')  # нажать левую клавишу мыши
            pg.moveTo(969, 614, duration=1)  # перемещение
            pg.mouseUp(button='left')  # отпустить левую клавиши мыши
            unit += 1
        return unit, hod, game, moneta, mana
    except TypeError:
        return zero


def health(template):  # функция лечения
    global zero
    try:
        buttonx, buttony = pg.locateCenterOnScreen(template, region=(800, 600, 400, 300), confidence=0.7) 
        pg.moveTo(buttonx, buttony)
        print(buttonx, buttony)
        pg.press(['right'])
        print("лечение")
        pg.moveTo(buttonx, buttony, duration=0) #перемещение к кнопке 
        pg.mouseDown(button='left') #нажать левую клавишу мыши
        pg.moveTo(800, buttony, duration=1) #перемещение
        pg.mouseUp(button='left') #отпустить левую клавиши мыши
    except TypeError:
        return zero


def projgrysh(template):
    global zero
    global progr
    try:
        buttonx, buttony = pg.locateCenterOnScreen(template, region=(0, 0, 1600, 900), confidence=0.7) 
        pg.moveTo(buttonx, buttony)
        print(buttonx, buttony)
        progr += 1
        print("Пройгрыш ", progr)  #выводит значение
        pg.moveTo(buttonx, buttony, duration=0) #перемещение
        pg.doubleClick(buttonx, buttony)
        time.sleep(2) #время ожидания запуска HS
        return progr
    except TypeError:
        return zero


def vyjgrysh(template):
    global zero
    global vygr
    try:
        buttonx, buttony = pg.locateCenterOnScreen(template, region=(0, 0, 1600, 900), confidence=0.7) 
        pg.moveTo(buttonx, buttony)
        print(buttonx, buttony)
        vygr +=1
        print("Выйгрыш ", vygr)  #выводит значение
        pg.moveTo(buttonx, buttony, duration=0) #перемещение
        pg.doubleClick(buttonx, buttony)
        time.sleep(2) #время ожидания запуска HS
        return vygr
    except TypeError:
        return zero


def endGame(template):
    global zero
    global Ggame
    try:
        buttonx, buttony = pg.locateCenterOnScreen(template, region=(0, 0, 1600, 900), confidence=0.7) 
        pg.moveTo(buttonx, buttony)
        print(buttonx, buttony)
        Ggame = 0
        print("Конец игры")  #выводит значение 
        pg.doubleClick(buttonx, buttony)
        time.sleep(2) #время ожидания запуска HS
        return Ggame
    except TypeError:
        return zero


def timer_game():
    global start_time
    now = datetime.datetime.now()
    loctime = format(time.time() - start_time)  # время в игре
    print(now)
    return now, loctime


def print_oll_table(): #функция вывода всей таблицы
    c.execute("SELECT * FROM total;")
    all_results = c.fetchall()
    for id in all_results:
        print(id[0], id[1], id[2], id[3], id[4], id[5], id[6], id[7], id[8], id[9], id[10], id[11], id[12])
        conn.commit()  # применяем изменения


def load_table():
    c.execute("SELECT * FROM total  WHERE   name_id = (SELECT MAX(name_id)  FROM total);")
    result_old = c.fetchone()
    print(result_old) # выводит последнюю строку таблицы
    # for id in result_old: # выводит по одному все значения последней строки
    #     print(id)
    b = result_old[1]
    print(result_old[0])
    print(b)
    conn.commit()


def fill_table_start(): # заполняем строку таблицы
    c.execute("""INSERT INTO total(date, localtime, globaltime, tipe, deck, localgame, localvictory, locallosing,
                localpercent, globalvictory, globallosing, globalpercent)
                VALUES('2021-01-02 00:52:09.891453', '0.0', '0.0', 'стандарт', 'жрец', '0' , '0', '0', '0', '0', '1', '1');""")
    conn.commit()


def fill_table(): # заполняем строку таблицы
    global now
    global start_time
    global tipe
    global deck
    global vygr
    global progr
    loctime = round(int(time.time() - start_time) / 60, 3)  # время в игре  сейчас, округляем до 3 знаков после запятой
    localpercent = round((vygr / (vygr + progr)) * 100, 2) #округляем до 3 знаков после запятой
    c.execute("SELECT * FROM total  WHERE   name_id = (SELECT MAX(name_id)  FROM total);")
    result_old = c.fetchone()
    print(result_old)
    globaltime = round(((result_old[3] + (loctime*60)) / 3600), 3)
    Ngame = vygr + progr
    globalvictory = result_old[10] + vygr
    globallosing = result_old[11] + progr
    globalpercent = round(((globalvictory / (globalvictory + globallosing)) * 100), 2)
    c.execute("""INSERT INTO total(date, localtime, globaltime, tipe, deck, localgame, localvictory, locallosing,
                    localpercent, globalvictory, globallosing, globalpercent) 
                    VALUES(?, ?, ?, ?, ?, ? , ?, ?, ?, ?, ?, ?);""",
              (now, loctime, globaltime, tipe, deck, Ngame, vygr, progr,
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
    start_time = time.time()  # учет начального времени работы программы
    tipe = 'стандарт'
    deck = 'жрец'
    ss("btn_grec.png")
    ss("btn_game_st.png")
    start_game("btn_start.png")
    if Ggame == 1:
        Ngame += 1
        print("Игра жрецом началась", Gcikl)
        while Ggame == 1:
            if keyboard.is_pressed('Enter'): # если клавиша Esc
                timer_game() #подсчет времени
                fill_table() #заполняем БД
                print_oll_table()
                sys.exit()  # завершаем программу
            Gcikl += 1
            ss("btn_start.png")
            ss("btn_ok.png")
            chughoj_hod("chughoj_hod.png")
            vash_hod("btn_end.png")
            print("hod=", hod)
            if hod == 1 and game == 1:
                pg.press(['right'])
                vash_hod("btn_end.png")
                ss("btn_end.png")
            elif hod > 1 and hod < 4 and game == 1:
                pg.press(['right'])
                health("btn_health.png")
                vash_hod("btn_end.png")
                ss("btn_end.png")
            elif hod == 4 and game == 1:
                pg.press(['right'])
                karta("btn_m0.png")
                if moneta == 1:
                    mana += 1
                    karta("btn_m5.png")
                    pg.press(['right'])
                    mana = mana - 5
                if mana >= 2:
                    health("btn_health.png")
                    mana = mana - 2
                moneta = 0
                vash_hod("btn_end.png")
                ss("btn_end.png")
            elif hod == 5 and game == 1:
                karta("btn_m5.png")
                if unit == 0 and mana >= 2:
                    health("btn_health.png")
                    mana = 0
                pg.press(['right'])
                vash_hod("btn_end.png")
                ss("btn_end.png")
            elif hod == 6 and game == 1:
                if unit == 0:
                    karta("btn_m6.png")
                    if unit == 1:
                        mana = 0
                if unit == 0:
                    karta("btn_m5.png")
                    if unit == 1:
                        mana = 1
                if unit == 0 and mana >= 2:
                    health("btn_health.png")
                    mana = 0
                pg.press(['right'])
                vash_hod("btn_end.png")
                ss("btn_end.png")
            elif hod == 7 and game == 1:
                if unit == 0:
                    karta("btn_m7.png")
                    if unit == 1:
                        mana = 0
                if unit == 0:
                    pg.press(['right'])
                    karta("btn_m6.png")
                    if unit == 1:
                        mana = 1
                if unit == 0:
                    pg.press(['right'])
                    karta("btn_m5.png")
                    if unit == 1:
                        mana = 2
                if mana >= 2:
                    health("btn_health.png")
                    mana = 0
                pg.press(['right'])
                vash_hod("btn_end.png")
                ss("btn_end.png")
            elif hod == 8 and game == 1:
                if unit == 0:
                    pg.press(['right'])
                    karta("btn_m8.png")
                    if unit == 1:
                        mana = 0
                if unit == 0:
                    pg.press(['right'])
                    karta("btn_m7.png")
                    if unit == 1:
                        mana = 1
                if unit == 0:
                    pg.press(['right'])
                    karta("btn_m6.png")
                    if unit == 1:
                        mana = 2
                if unit == 0:
                    pg.press(['right'])
                    karta("btn_m5.png")
                    if unit == 1:
                        mana = 3
                if mana >= 2:
                    health("btn_health.png")
                    mana = 0
                pg.press(['right'])
                vash_hod("btn_end.png")
                ss("btn_end.png")
            elif hod == 9 and game == 1:
                if unit == 0:
                    pg.press(['right'])
                    karta("btn_m9.png")
                    if unit == 1:
                        mana = 0
                if unit == 0:
                    pg.press(['right'])
                    karta("btn_m8.png")
                    if unit == 1:
                        mana = 1
                if unit == 0:
                    pg.press(['right'])
                    karta("btn_m7.png")
                    if unit == 1:
                        mana = 2
                if unit == 0:
                    pg.press(['right'])
                    karta("btn_m6.png")
                    if unit == 1:
                        mana = 3
                if unit == 0:
                    pg.press(['right'])
                    karta("btn_m5.png")
                    if unit == 1:
                        mana = 4
                if mana >= 2:
                    health("btn_health.png")
                    mana = 0
                pg.press(['right'])
                vash_hod("btn_end.png")
                ss("btn_end.png")
            elif hod >= 10 and game == 1:
                if unit == 0:
                    pg.press(['right'])
                    karta("btn_m10.png")
                    if unit == 1:
                        mana = 0
                if unit == 0:
                    pg.press(['right'])
                    karta("btn_m9.png")
                    if unit == 1:
                        mana = 1
                if unit == 0:
                    pg.press(['right'])
                    karta("btn_m8.png")
                    if unit == 1:
                        mana = 2
                if unit == 0:
                    pg.press(['right'])
                    karta("btn_m7.png")
                    if unit == 1:
                        mana = 3
                if unit == 0:
                    pg.press(['right'])
                    karta("666.png")
                    if unit == 1:
                        mana = 4
                if unit == 0:
                    pg.press(['right'])
                    karta("btn_m5.png")
                    if unit == 1:
                        mana = 5
                if mana >= 2:
                    health("btn_health.png")
                    mana = 0
                pg.press(['right'])
                vash_hod("btn_end.png")
                ss("btn_end.png")
            projgrysh("end_game.png")
            vyjgrysh("victory.png")
            endGame("end_game2.png")
            if Ggame == 0:
                fill_table()  # заполняем БД
                print_oll_table()
                start_time = time.time()
            ss("bt.png")
            ss("bt2.png")
        return  Ggame, Ngame, Gcikl, vygr, progr, start_time


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
    start_time = time.time()  # учет начального времени работы программы
    tipe = 'стандарт'
    deck = 'охотник'
    ss("btn_hant.png")
    ss("btn_game_st.png")
    start_game("btn_start.png")
    if Ggame == 1:
        Ngame += 1
        print("игра охотником началась", Gcikl)
        while Ggame == 1:
            if keyboard.is_pressed('Enter'): # если клавиша Esc
                timer_game() #подсчет времени
                fill_table() #заполняем БД
                print_oll_table()
                sys.exit()  # завершаем программу
            Gcikl += 1
            ss("btn_ok.png")
            chughoj_hod("chughoj_hod.png")
            vash_hod("btn_end.png")
            print("hod=", hod)
            if hod == 1 and game == 1:
                pg.press(['right'])
                vash_hod("btn_end.png")
                ss("btn_end.png")
            elif hod > 1 and hod < 4 and game == 1:
                pg.press(['right'])
                ss("btn_strela.png")
                vash_hod("btn_end.png")
                ss("btn_end.png")
            elif hod == 4 and game == 1:
                pg.press(['right'])
                karta("btn_m0.png")
                if moneta == 1:
                    mana += 1
                    karta("btn_m5.png")
                    pg.press(['right'])
                if mana >= 2:
                    ss("btn_strela.png")
                    mana = mana - 2
                moneta = 0
                vash_hod("btn_end.png")
                ss("btn_end.png")
            elif hod == 5 and game == 1:
                if unit == 0:
                    pg.press(['right'])
                    karta("btn_m5.png")
                    if unit == 1:
                        mana = 1
                if mana >= 2:
                    ss("btn_strela.png")
                pg.press(['right'])
                vash_hod("btn_end.png")
                ss("btn_end.png")
            elif hod == 6 and game == 1:
                if unit == 0:
                    pg.press(['right'])
                    karta("btn_m6.png")
                    if unit == 1:
                        mana = 0
                if unit == 0:
                    pg.press(['right'])
                    karta("btn_m5.png")
                    if unit == 1:
                        mana = 1
                if mana >= 2:
                    ss("btn_strela.png")
                pg.press(['right'])
                vash_hod("btn_end.png")
                ss("btn_end.png")
            elif hod >= 7 and game == 1:
                if unit == 0:
                    karta("btn_m7.png")
                    if unit == 1:
                        mana = 0
                if unit == 0:
                    pg.press(['right'])
                    karta("btn_m6.png")
                    if unit == 1:
                        mana = 1
                if unit == 0:
                    pg.press(['right'])
                    karta("btn_m5.png")
                    if unit == 1:
                        mana = 2
                if mana >= 2:
                    ss("btn_strela.png")
                pg.press(['right'])
                vash_hod("btn_end.png")
                ss("btn_end.png")
            projgrysh("end_game.png")
            vyjgrysh("victory.png")
            endGame("end_game2.png")
            if Ggame == 0:
                fill_table()  # заполняем БД
                print_oll_table()
                start_time = time.time()
            ss("bt.png")
            ss("bt2.png")
        return  Ggame, Ngame, Gcikl, vygr, progr, start_time


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
    start_time = time.time()  # учет начального времени работы программы
    tipe = 'стандарт'
    deck = 'воин'
    ss("btn_voin.png")
    ss("btn_game_st.png")
    start_game("btn_start.png")
    if Ggame == 1:
        Ngame += 1
        print("Игра воином началась", Gcikl)
        while Ggame == 1:
            if keyboard.is_pressed('Enter'): # если клавиша Esc
                timer_game() #подсчет времени
                fill_table() #заполняем БД
                print_oll_table()
                sys.exit()  # завершаем программу
            Gcikl += 1
            ss("btn_start.png")
            ss("btn_ok.png")
            chughoj_hod("chughoj_hod.png")
            vash_hod("btn_end.png")
            print("hod=", hod)
            if hod == 1 and game == 1:
                pg.press(['right'])
                vash_hod("btn_end.png")
                ss("btn_end.png")
            elif hod > 1 and hod < 4 and game == 1:
                pg.press(['right'])
                ss("btn_schit.png")
                vash_hod("btn_end.png")
                ss("btn_end.png")
            elif hod == 4 and game == 1:
                pg.press(['right'])
                karta("btn_m0.png")
                if moneta == 1:
                    mana += 1
                    karta("btn_m5.png")
                    pg.press(['right'])
                if mana >= 2:
                    ss("btn_schit.png")
                    mana = mana - 2
                moneta = 0
                vash_hod("btn_end.png")
                ss("btn_end.png")
            elif hod == 5 and game == 1:
                 if unit == 0:
                    pg.press(['right'])
                    karta("btn_m5.png")
                    if unit == 1:
                        mana = 1
                 if mana >= 2:
                    ss("btn_schit.png")
                 pg.press(['right'])
                 vash_hod("btn_end.png")
                 ss("btn_end.png")
            elif hod == 6 and game == 1:
                if unit == 0:
                    pg.press(['right'])
                    karta("btn_m6.png")
                    if unit == 1:
                        mana = 0
                if unit == 0:
                    pg.press(['right'])
                    karta("btn_m5.png")
                    if unit == 1:
                        mana = 1
                if mana >= 2:
                    ss("btn_schit.png")
                pg.press(['right'])
                vash_hod("btn_end.png")
                ss("btn_end.png")
            elif hod >= 7 and game == 1:
                if unit == 0:
                    karta("btn_m7.png")
                    if unit == 1:
                        mana = 0
                if unit == 0:
                    pg.press(['right'])
                    karta("btn_m6.png")
                    if unit == 1:
                        mana = 1
                if unit == 0:
                    pg.press(['right'])
                    karta("btn_m5.png")
                    if unit == 1:
                        mana = 2
                if mana >= 2:
                    ss("btn_schit.png")
                pg.press(['right'])
                vash_hod("btn_end.png")
                ss("btn_end.png")
            projgrysh("end_game.png")
            vyjgrysh("victory.png")
            endGame("end_game2.png")
            if Ggame == 0:
                fill_table()  # заполняем БД
                print_oll_table()
                start_time = time.time()
            ss("bt.png")
            ss("bt2.png")
        return  Ggame, Ngame, Gcikl, vygr, progr, start_time


# variables
Ngame = 0  # подсчет количества игр !(основное тело цикла)
vygr = 0  # подсчет выйгрышей в данной сессии
progr = 1  # подсчет проигранных игр в данной сессии
Ggame = 0  # индикатор начала рейтинговой игры !start_game()-->1, endGame()-->0
Gcikl = 0  # счетчик циклов внутри игры
cikl = 1  # подсчет общего числа циклов программы
hod = 0  # учет номера хода !start_game()-->1 !chughoj_hod()-->+1
unit = 0  # количество выложенных юнитов за ход (для того что бы знать сколько выложено)
game = 0  # индикатор игры (вашего хода)
moneta = 0  # индикатор монеты в руке
mana = 0  # счетчик маны во время хода
zero = 0  # ноль
start_time = time.time() # учет начального времени работы программы
now = datetime.datetime.now() # текущие дата и время

# Работа с БД
conn = sqlite3.connect('mydatabase.db')  # создаем переменную conn и  соединение с нашей базой данных
c = conn.cursor()  # Создаем курсор - это специальный объект который делает запросы и получает их результаты
c.execute("""CREATE TABLE IF NOT EXISTS total(
   name_id INTEGER PRIMARY KEY,
   date DATE NOT NULL,
   localtime INT NOT NULL,
   globaltime DATE NOT NULL,
   tipe TEXT NOT NULL,
   deck TEXT NOT NULL,
   localgame INT NOT NULL,
   localvictory INT NOT NULL,
   locallosing INT NOT NULL,
   localpercent REAL NOT NULL,
   globalvictory INT NOT NULL,
   globallosing INT NOT NULL,
   globalpercent REAL NOT NULL);
""")
conn.commit()  # применяем изменения

startlnk()  # запуск приложения Battle.net

#fill_table_start()

while "Бесконечный цикл":  # Цикл анализа
    if keyboard.is_pressed('Enter'):  # если клавиша Esc
        fill_table()  # заполняем БД
        print_oll_table()
        sys.exit()  # завершаем программу
    cikl += 1
    print("Цикл =", cikl)
    print("Колличество игр ", Ngame)
    print("Пройгрыш", progr)
    print("Выйгрыш", vygr)
    time.sleep(5)
    ss("00_btn_game.png")
    ss("btn_game.png")
    a = random.randint(1, 3) # рандомное число от 1 до 3
    if a == 1:
        grec_standart()
    elif a == 2:
        hant_standart()
    elif a == 3:
        voin_standart()

    # На случай потери соединения
    ss("bt.png")
    ss("bt2.png")
    pointclick()
