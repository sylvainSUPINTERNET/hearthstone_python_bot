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

def start_game(template):  # функция определения начала игры
    global hod
    global Gcikl
    global Ggame
    global cikl
    global zero
    global activity, screen_width_x, screen_height_y
    try:
        buttonx, buttony = pg.locateCenterOnScreen(template, region=(0, 0, screen_width_x, screen_height_y), confidence=0.7)
        pg.moveTo(buttonx, buttony)
        pg.click(buttonx, buttony)
        Gcikl += 1
        hod = 1
        print('Нашел активную игру')
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

def level_game(template):
    global game  # индикатор игры уровня
    global zero, game
    global activity, screen_width_x, screen_height_y
    try:
        buttonx, buttony = pg.locateCenterOnScreen(template, region=(0, 0, screen_width_x, screen_height_y), confidence=0.7)
        pg.moveTo(buttonx, buttony, duration=0)
        pg.click(buttonx, buttony)
        if game == 0:
            game = 1
            while game == 1:
                activity = time.time()
                time.sleep(2)
                ss(active_dir + "played_out.png")  # выбор стартовой руки (нажатие на кнопку разыграно)
                time.sleep(2)
                ss(active_dir + "milhaus.png")  # выбор милхауса
                time.sleep(1)
                ss(active_dir + "magic_explosion.png")  # выбор чарадейского взрыва Милхауса
                time.sleep(1)
                ss(active_dir + "all_is_ready.png")  # выбор кнопки все готово
                time.sleep(1)
                end_level(active_dir + "victory_m.png")  # поиск выйгрыша уровня
            return game, activity
    except TypeError:
        return zero

def end_level(template):
    global game
    global activity, screen_width_x, screen_height_y
    try:
        buttonx, buttony = pg.locateCenterOnScreen(template, region=(0, 0, screen_width_x, screen_height_y), confidence=0.7)
        pg.moveTo(buttonx, buttony)
        if game == 1:
            game = 0
        # print("Уровень пройден")
        activity = time.time()
        time.sleep(1)
        return game, activity
    except TypeError:
        return zero

def present(template):  # функция открытия поиска всех подарков по кнопке ОК
    global Ggame, activity, screen_width_x, screen_height_y, zero
    try:
        buttonx, buttony = pg.locateCenterOnScreen(template, region=(0, 0, screen_width_x, screen_height_y), confidence=0.7)
        pg.doubleClick(buttonx, buttony)
        activity = time.time()
        Ggame = 1
        return Ggame, activity
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
        Ggame = 0
        # print("Конец игры")
        # pg.doubleClick(buttonx, buttony)

        while Ggame == 0:
            time.sleep(1)
            ss(active_dir + "present.png")  # поиск подарка
            present(active_dir + "btn_ready.png")  # поиск кнопки готово
            present(active_dir + "losing_m.png")

        Ggame = 0
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
Ggame = 0  # индикатор начала игры !start_game()-->1, endGame()-->0
Gcikl = 0  # счетчик циклов внутри игры
cikl = 1  # подсчет общего числа циклов программы
game = 0  # индикатор игры (одного уровня)
delay = 25  # вемя на свой ход
activity = time.time()  # анализ активности игрового процесса
zero = 0

boss_level = dict.fromkeys(['enemy_1.png', 'enemy_2.png', 'enemy_3.png', 'enemy_4.png', 'enemy_5.png', 'enemy_6.png', 'enemy_7.png'], 1)

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


def mercenaries_deck():
    global Ggame, Ngame, Gcikl, game, hod, mana, moneta, tipe, deck, vygr, progr
    global cikl, unit, start_time, delay, activity

    tipe = 'наемники'
    deck = 'гринд 4'
    cikl += 1
    time.sleep(1)
    ss(active_dir + "00_btn_game.png")  # выбор кнопки играть в окне batlenet
    ss(active_dir + "btn_mercenaries.png")  # выбор вкладки наемники в основном окне
    ss(active_dir + "btn_pvp.png")  # выбор режима pvp
    ss(active_dir + "normal_mode.png")  # выбор обычного режима
    ss(active_dir + "select.png")  # нажатие на кнопку выбор
    ss(active_dir + "ok_3.png")  # кнопка статистики предыдущей игры
    time.sleep(1)
    pointclick()
    time.sleep(1)
    start_game(active_dir + "level_4.png")  # пошел выбор противника, игра активна
    if Ggame == 1:
        Ngame += 1
        start_time = datetime.now()  # текущие дата и время
        if Ggame == 1:
            ss(active_dir + "select_2.png")  # нажатие на кнопку выбор (подтверждение выбора уровня)
            time.sleep(1)
            ss(active_dir + "select_2.png")  # нажатие на кнопку выбор (текущей колоды колоды)
            time.sleep(4)
            ss(active_dir + "confirm.png")  # выбор кнопки подтвердить
            time.sleep(5)
        while Ggame == 1:  # проверка активности в игре
            if (time.time() - activity) >= 280:
                pointclick()
            if (time.time() - activity) >= 300:
                Ggame = 0
            Gcikl += 1
            level_game(active_dir + "btn_game_st_2.png")  # выбор N-го уровня игры (кнопка играть)

            for i in range(1, 4):
                time.sleep(1)
                pg.doubleClick()  # произвольное нажатие после прогресса первой тройки героев


            ss(active_dir + "ugol.png")  # выбор способности для одного из героев для следующих уровней`
            time.sleep(1)
            ss(active_dir + "btn_take.png")  # выбор кнопки взять способность

            for one in boss_level:  # перебираем всех боссов уровней
                ss(active_dir + str(one))  # выбор противника (следующего уровня)
                level_game(active_dir + "btn_game_st_2.png")  # выбор N-го уровня игры (кнопка играть)


            # окончание игры

            endGame(active_dir + "present.png")  # просмотр статистики за игру и нажатие на кнопку ок
            endGame(active_dir + "losing_m.png")  # пройгрыш
            if Ggame == 0:
                time.sleep(1)
                pointclick()
                fill_table()  # заполняем БД
        return Ggame, Ngame, Gcikl, vygr, progr, start_time, activity
    pointclick()
    activity_analysis()