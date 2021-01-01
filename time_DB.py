# python3
import time
import datetime
import sqlite3 # Импортируем библиотеку, соответствующую типу нашей базы данных

today = datetime.date.today()
now = datetime.datetime.now()
start_time = time.time() # учет начального времени работы программы

# print(today)
# print(now)
# print(start_time)
#
# print("--- %s секунд ---" % (time.time() - start_time))


start_time = datetime.datetime.now()
end_time = datetime.datetime.now()
loctime = format(end_time - start_time)
# print('Время работы: {}'.format(end_time - start_time))
# print('Время работы: {}'.format(loctime))


conn = sqlite3.connect('mydatabase.db')  # создаем переменную conn и cоздаем соединение с нашей базой данных
c = conn.cursor()  # Создаем курсор - это специальный объект который делает запросы и получает их результаты

# создаем в БД mydatabase.db таблицу total и создаем стобцы
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
# conn.close()  # Не забываем закрыть соединение с базой данных


def print_oll_table(): #функция вывода всей таблицы
    c.execute("SELECT * FROM total;")
    all_results = c.fetchall()
    for id in all_results:
        #print(id[0], id[1], id[2], id[3], id[4], id[5], id[6], id[7], id[8], id[9], id[10], id[11], id[12])
        print(id)
        conn.commit()  # применяем изменения
#    conn.close()  # Не забываем закрыть соединение с базой данных

def fill_table(): # заполняем строку таблицы
    c.execute("""INSERT INTO total(date, localtime, globaltime, tipe, deck, localgame, localvictory, locallosing,
                localpercent, globalvictory, globallosing, globalpercent) 
                VALUES(?, ?, '1 sec', 'стандарт', 'жрец', '5' , '2', '3', '70%', '60', '30', '50');""",
              (now, loctime, ))
    conn.commit()
#    conn.close()  # Не забываем закрыть соединение с базой данных

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



fill_table() # заполняем строку таблицы
print_oll_table() # вывода всей таблицы
load_table()
conn.close()  # Не забываем закрыть соединение с базой данных

print('Время работы: {}'.format(end_time - start_time))