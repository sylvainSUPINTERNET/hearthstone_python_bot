# python3
import time
import datetime
from datetime import datetime
from datetime import timedelta
import sqlite3 # Импортируем библиотеку, соответствующую типу нашей базы данных

# работа со временем
# datetime
# # datetime
#
# today = datetime.date.today()
# now = datetime.datetime.now()
#
#
# print(today)
# print(datetime.date.today())
# print(now)
#
# # обратное преобразование
# d = datetime.date(2012, 12, 14)
#
# print(d.year)  # 2012
# print(d.day)  # 14
# print(d.month)  # 12
#
#
# # # Значение: datetime.datetime(2017, 4, 5, 0, 18, 51, 980187)
# # now = datetime.datetime.now()
# # then = datetime.datetime(2020, 12, 1)
# #
# # # Кол-во времени между датами.
# # delta = now - then
# # print(delta.days)  # 38
# # print(delta.seconds)  # 1131
#
#
# now = datetime.datetime.now()
# time.sleep(5)
# then = datetime.datetime.now()
#
# # Кол-во времени между датами.
# delta = now - then
# print(delta.days)  # 38
# print(delta.seconds)  # 1131


# %a: аббревиатура дня недели. Например, Wed - от слова Wednesday (по умолчанию используются английские наименования)
# %A: день недели полностью, например, Wednesday
# %b: аббревиатура названия месяца. Например, Oct (сокращение от October)
# %B: название месяца полностью, например, October
# %d: день месяца, дополненный нулем, например, 01
# %m: номер месяца, дополненный нулем, например, 05
# %y: год в виде 2-х чисел
# %Y: год в виде 4-х чисел
# %H: час в 24-х часовом формате, например, 13
# %I: час в 12-ти часовом формате, например, 01
# %M: минута
# %S: секунда
# %f: микросекунда
# %p: указатель AM/PM
# %c: дата и время, отформатированные под текущую локаль
# %x: дата, отформатированная под текущую локаль
# %X: время, форматированное под текущую локаль

# now = datetime.now()
# print(now.strftime("%Y-%m-%d"))             # 2017-05-03
# print(now.strftime("%d/%m/%Y"))             # 03/05/2017
# print(now.strftime("%d/%m/%y"))             # 03/05/17
# print(now.strftime("%d %B %Y (%A)"))        # 03 May 2017 (Wednesday)
# print(now.strftime("%d/%m/%y %I:%M"))       # 03/05/17 01:36




# time
# # time
#
# time_sec_1970 = time.time() # время в секундах с 1970 г.
# time_year_1970 = int(time.time() / ((3600 * 24)*365)) # сколько лет прошло с 1970г.
# print('время в секундах с 1970 г. - ', time_sec_1970)
# print('сколько лет прошло с 1970г. - ', time_year_1970)
# time.sleep(0)
#
# time_x = time.gmtime() # time.struct_time
# # (tm_year=2021, tm_mon=1, tm_mday=3, tm_hour=11, tm_min=18, tm_sec=0, tm_wday=6, tm_yday=3, tm_isdst=0)
# time_1 = time.asctime() # Sun Jan  3 14:18:00 2021
# time_2 = time.ctime()  #  Sun Jan  3 14:18:00 2021
# time_3 = time_x.tm_year # год
# time_4 = time_x.tm_mon # месяц
# time_5 = time_x.tm_mday # день
# time_6 = time_x.tm_hour # час
# time_7 = time_x.tm_min # минуты
# time_8 = time_x.tm_sec # секунды
# time_9 = time_x.tm_wday # день недели от 0 до 6
# time_10 = time_x.tm_yday # день года от 0 до 366
#
#
# print(time_x)
# print(time_1)
# print(time_2)
# print('год', time_3)
# print('месяц', time_4)
# print('день', time_5)
# print('час', time_6)
# print('минуты', time_7)
# print('секунды', time_8)
# print('день недели от 0 до 6', time_9)
# print('день недели от 0 до 6', time_10)
#
#
# named_tuple = time.localtime() # получить struct_time
# time_string = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)
# time_string_1 = time.strftime("%d.%m.%Y, %H:%M", named_tuple)
#
#
# print(time_string)
# print(time_string_1)
#
# # обратное преобразование времени
# time_string = "15 June, 2019"
# result = time.strptime(time_string, "%d %B, %Y") # обратное преобразование строки во время
# print(result)
# print(result.tm_year)  # вывод времени



# print("--- %s секунд ---" % (time.time() - start_time))
# now = datetime.datetime.now()
# loctime = int(time.time() - start_time)  # время в игре
# print(loctime)
# print(type(loctime))
# start_time = datetime.datetime.now()
# end_time = datetime.datetime.now()
#loctime = format(end_time - start_time)
# print('Время работы: {}'.format(end_time - start_time))
# print('Время работы: {}'.format(loctime))
# print(loctime)
# print(type(loctime))
# print('Время работы: {}'.format(end_time - start_time))





# Работа с базами данными
# conn = sqlite3.connect('mydatabase.db')  # создаем переменную conn и cоздаем соединение с нашей базой данных
# c = conn.cursor()  # Создаем курсор - это специальный объект который делает запросы и получает их результаты
#
# # создаем в БД mydatabase.db таблицу total и создаем стобцы
# c.execute("""CREATE TABLE IF NOT EXISTS total(
#    name_id INTEGER PRIMARY KEY,
#    date DATE NOT NULL,
#    localtime INT NOT NULL,
#    globaltime DATE NOT NULL,
#    tipe TEXT NOT NULL,
#    deck TEXT NOT NULL,
#    localgame INT NOT NULL,
#    localvictory INT NOT NULL,
#    locallosing INT NOT NULL,
#    localpercent REAL NOT NULL,
#    globalvictory INT NOT NULL,
#    globallosing INT NOT NULL,
#    globalpercent REAL NOT NULL);
# """)
# conn.commit()  # применяем изменения
# # conn.close()  # Не забываем закрыть соединение с базой данных
#
#
# def print_oll_table(): #функция вывода всей таблицы
#     c.execute("SELECT * FROM total;")
#     all_results = c.fetchall()
#     for id in all_results:
#         #print(id[0], id[1], id[2], id[3], id[4], id[5], id[6], id[7], id[8], id[9], id[10], id[11], id[12])
#         print(id)
#         conn.commit()  # применяем изменения
# #    conn.close()  # Не забываем закрыть соединение с базой данных
#
# def fill_table(): # заполняем строку таблицы
#     c.execute("""INSERT INTO total(date, localtime, globaltime, tipe, deck, localgame, localvictory, locallosing,
#                 localpercent, globalvictory, globallosing, globalpercent)
#                 VALUES(?, ?, '0.0', 'стандарт', 'жрец', '5' , '2', '3', '70', '60', '30', '50');""",
#               (now, loctime, ))
#     conn.commit()
# #    conn.close()  # Не забываем закрыть соединение с базой данных
#
# # def load_table():
# #     c.execute("SELECT * FROM total  WHERE   name_id = (SELECT MAX(name_id)  FROM total);")
# #     result_old = c.fetchone()
# #     print(result_old) # выводит последнюю строку таблицы
# #     # for id in result_old: # выводит по одному все значения последней строки
# #     #     print(id)
# #     b = result_old[1]
# #     print(result_old[0])
# #     print(b)
# #     conn.commit()
#
#
# def load_table():
#     try:
#         localpercent = (0 / (0 + 10)) * 100
#         c.execute("SELECT * FROM total  WHERE   name_id = (SELECT MAX(name_id)  FROM total);")
#         result_old = c.fetchone()
#         globaltime = result_old[3] + loctime
#         globalvictory = result_old[10]
#         globallosing = result_old[11]
#         globalpercent = (globalvictory / (globalvictory + globallosing)) * 100
#         tipe = 'standart'
#         deck = 'grec'
#         Ngame = 0
#         vygr = 0
#         progr = 0
#         c.execute("""INSERT INTO total(date, localtime, globaltime, tipe, deck, localgame, localvictory, locallosing,
#                             localpercent, globalvictory, globallosing, globalpercent)
#                             VALUES(?, ?, ?, ?, ?, ? , ?, ?, ?, ?, ?, ?);""",
#                       (now, loctime, globaltime, tipe, deck, Ngame, vygr, progr,
#                        localpercent, globalvictory, globallosing, globalpercent))
#         conn.commit()
#     except ZeroDivisionError:
#         localpercent = 0
#         c.execute("SELECT * FROM total  WHERE   name_id = (SELECT MAX(name_id)  FROM total);")
#         result_old = c.fetchone()
#         globaltime = print(type(result_old[3]), type(format(loctime)))
#         print(result_old[3])
#         print(int(str(loctime)))
#         globalvictory = result_old[10]
#         globallosing = result_old[11]
#         globalpercent = 0
#         c.execute("""INSERT INTO total(date, localtime, globaltime, tipe, deck, localgame, localvictory, locallosing,
#                                     localpercent, globalvictory, globallosing, globalpercent)
#                                     VALUES(?, ?, ?, ?, ?, ? , ?, ?, ?, ?, ?, ?);""",
#                       (now, loctime, globaltime, 'standart', 'grec', '0', '0', '0',
#                        localpercent, globalvictory, globallosing, '0.0'))
#         conn.commit()
#
# #fill_table() # заполняем строку таблицы
# print_oll_table() # вывода всей таблицы
# load_table()
# conn.close()  # Не забываем закрыть соединение с базой данных



# Работа с БД 03.01.2021
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
   localgame INT NOT NULL,
   localvictory INT NOT NULL,
   locallosing INT NOT NULL,
   localpercent REAL NOT NULL,
   globalvictory INT NOT NULL,
   globallosing INT NOT NULL,
   globalpercent REAL NOT NULL);
""")
conn.commit()  # применяем изменения



c.execute("""INSERT INTO total(date, startgame, endgame, l_days, l_hours, l_minuts, l_seconds,
            g_days, g_hours, g_minuts, g_seconds, tipe, deck, localgame, localvictory, locallosing,
            localpercent, globalvictory, globallosing, globalpercent)
            VALUES('01.01.2021', '00:00', '00.00', '0', '0', '0', '0',
            '0', '0', '0', '0', 'стандарт', 'жрец', '0' , '0', '0', '0', '0', '0', '0');""")
conn.commit()


start_time = datetime.now()
date = start_time.strftime("%d.%m.%Y")
startgame = start_time.strftime("%H:%M:%S")
end_game = datetime(2021, 1, 16)
endgame = end_game.strftime("%H:%M:%S")

loctime = end_game - start_time  # время в игре
l_days = loctime.days #дни
l_hours = int(loctime.seconds/3600) #часы
l_minuts = int((loctime.seconds - l_hours*3600)/60) #минуты
l_seconds = loctime.seconds - l_hours*3600 - l_minuts*60 #секунды




vygr = 1
progr = 6
localpercent = round((vygr / (vygr + progr)) * 100, 2) #округляем до 3 знаков после запятой
c.execute("SELECT * FROM total  WHERE   name_id = (SELECT MAX(name_id)  FROM total);")
result_old = c.fetchone()
print(result_old)

g_days = result_old[8] + l_days #дни
g_hours = result_old[9] + l_hours #часы
g_minuts = result_old[10] + l_minuts #минуты
g_seconds = result_old[11] + l_seconds  #секунды

tipe = 'жрец'
deck = 'стандарт'

Ngame = vygr + progr
localgame = Ngame
localvictory = vygr
locallosing = progr
globalvictory = result_old[10] + vygr
globallosing = result_old[11] + progr
globalpercent = round(((globalvictory / (globalvictory + globallosing)) * 100), 2)
c.execute("""INSERT INTO total(date, startgame, endgame, l_days, l_hours, l_minuts, l_seconds, 
            g_days, g_hours, g_minuts, g_seconds, tipe, deck, localgame, localvictory, locallosing,
                localpercent, globalvictory, globallosing, globalpercent) 
                VALUES(?, ?, ?, ?, ?, ? , ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ? , ?, ?);""",
          (date, startgame, endgame, l_days, l_hours, l_minuts, l_seconds,
            g_days, g_hours, g_minuts, g_seconds, tipe, deck, localgame, localvictory, locallosing,
                localpercent, globalvictory, globallosing, globalpercent))
conn.commit()