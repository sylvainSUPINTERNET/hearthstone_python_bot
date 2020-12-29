import pyautogui
import subprocess #Запуск приложений windows
import time #работа со временем


def startlnk(): #функция запуска приложения
    subprocess.Popen('C:\Program Files (x86)\Battle.net\Battle.net Launcher.exe') #запуск приложения
    time.sleep(2) #время ожидания запуска battle.net


def pointclick():  # функция произвольного нажатия в цикле
    pyautogui.doubleClick(1599, 524)


def ss(template):  # функция определения и двойного нажатия на координаты кнопки
    try:
        buttonx, buttony = pyautogui.locateCenterOnScreen(template, region=(0, 0, 1600, 900), confidence=0.7) 
        pyautogui.moveTo(buttonx, buttony)
        pyautogui.doubleClick(buttonx, buttony)
        print(buttonx, buttony)
        time.sleep(2)
    except TypeError:
        print("двойной клик не будет")
       
def start_game(template):
    global hod
    global Gcikl
    global Ggame
    global cikl
    try:
        buttonx, buttony = pyautogui.locateCenterOnScreen(template, region=(0, 0, 1600, 900), confidence=0.7) 
        pyautogui.moveTo(buttonx, buttony)
        print(buttonx, buttony)
        Gcikl += 1
        hod = 1
        Ggame = 1
        cikl = 0
        return hod
        return Gcikl
        return Ggame
        return cikl
        print("Старт игры")                  
        time.sleep(15) 
    except TypeError:
        print("Игра не началась")
                    

def vash_hod(template):
    global game #индикатор своего хода
    try:
        buttonx, buttony = pyautogui.locateCenterOnScreen(template, region=(0, 0, 1600, 900), confidence=0.7) 
        if game == 0:
            game = 1
            print("Старт хода")  
            pyautogui.moveTo(buttonx, buttony, duration=0)                     
            time.sleep(15) 
            return game
        time.sleep(2)
    except TypeError:
        print("Не мой ход")


def chughoj_hod(template):
    global game
    global unit
    global hod 
    global mana
    try:
        buttonx, buttony = pyautogui.locateCenterOnScreen(template, region=(0, 0, 1600, 900), confidence=0.7) 
        pyautogui.moveTo(buttonx, buttony)
        print(buttonx, buttony)
        time.sleep(2)
        if game == 1 :
            hod +=1
            game = 0
            unit = 0                    
        print("Ход противника")                  
        time.sleep(15) 
        if hod < 11:
            mana = hod
        elif hod >= 11:
            mana = 10
        return game
        return unit
        return hod
        return mana
    except TypeError:
        print("Не чужой ход")
        


def karta(template):  # функция покупки юнита
    global unit
    global hod
    global game
    global moneta
    try:
        buttonx, buttony = pyautogui.locateCenterOnScreen(template, region=(0, 500, 1600, 400), confidence=0.7) 
        pyautogui.moveTo(buttonx, buttony)
        print(buttonx, buttony)
        print("unit", unit)
        print("hod", hod)
        print("game", game)
        pyautogui.press(['right'])
        if hod == 4 and unit == 0:
            moneta=1
            print("Выложил монету на стол")
            pyautogui.moveTo(buttonx, buttony, duration=0) #перемещение к кнопке 
            pyautogui.mouseDown(button='left') #нажать левую клавишу мыши
            pyautogui.moveTo(969, 614, duration=1) #перемещение
            pyautogui.mouseUp(button='left') #отпустить левую клавиши мыши
        if unit == 0 and hod > 3 and game == 1 and mana >=5 :
            print("Выложил одну карту на стол")
            pyautogui.moveTo(buttonx, buttony, duration=0) #перемещение к кнопке 
            pyautogui.mouseDown(button='left') #нажать левую клавишу мыши
            pyautogui.moveTo(969, 614, duration=1) #перемещение
            pyautogui.mouseUp(button='left') #отпустить левую клавиши мыши
            unit +=1                    
        return unit
        return hod
        return game
        return moneta
    except TypeError:
        print("Нет карты в руке")

def health(template):  # функция лечения
    try:
        buttonx, buttony = pyautogui.locateCenterOnScreen(template, region=(800, 600, 400, 300), confidence=0.7) 
        pyautogui.moveTo(buttonx, buttony)
        print(buttonx, buttony)
        pyautogui.press(['right'])
        print("лечение")
        pyautogui.moveTo(buttonx, buttony, duration=0) #перемещение к кнопке 
        pyautogui.mouseDown(button='left') #нажать левую клавишу мыши
        pyautogui.moveTo(800, buttony, duration=1) #перемещение
        pyautogui.mouseUp(button='left') #отпустить левую клавиши мыши
    except TypeError:
        print("Не востановил здоровье")
        
def projgrysh(template):
    global progr
    try:
        buttonx, buttony = pyautogui.locateCenterOnScreen(template, region=(0, 0, 1600, 900), confidence=0.7) 
        pyautogui.moveTo(buttonx, buttony)
        print(buttonx, buttony)
        progr +=1
        print("Пройгрыш ", progr)  #выводит значение
        pyautogui.moveTo(buttonx, buttony, duration=0) #перемещение
        pyautogui.doubleClick(buttonx, buttony)
        time.sleep(2) #время ожидания запуска HS
        return progr
    except TypeError:
        print("Не пройгрыш")
        

def vyjgrysh(template):
    global vygr 
    try:
        buttonx, buttony = pyautogui.locateCenterOnScreen(template, region=(0, 0, 1600, 900), confidence=0.7) 
        pyautogui.moveTo(buttonx, buttony)
        print(buttonx, buttony)
        vygr +=1
        print("Выйгрыш ", vygr)  #выводит значение
        pyautogui.moveTo(buttonx, buttony, duration=0) #перемещение
        pyautogui.doubleClick(buttonx, buttony)
        time.sleep(2) #время ожидания запуска HS
        return vygr
    except TypeError:
        print("Не выйгрыш")
        

def endGame(template):
    global Ggame
    try:
        buttonx, buttony = pyautogui.locateCenterOnScreen(template, region=(0, 0, 1600, 900), confidence=0.7) 
        pyautogui.moveTo(buttonx, buttony)
        print(buttonx, buttony)
        Ggame = 0
        print("Конец игры")  #выводит значение 
        pyautogui.doubleClick(buttonx, buttony)
        time.sleep(2) #время ожидания запуска HS
        return Ggame
    except TypeError:
        print("не конец игры")
        

startlnk()#запуск приложения Battle.net
game=0 #индикатор игры (вашего хода)
cikl=1 #подсчет общего числа циклов программы
hod=0 #учет номера хода !start_game()-->1 !chughoj_hod()-->+1
progr=0 #подсчет проигранных игр
unit=0 #количество выложенных юнитов за ход (для того что бы знать сколько выложено)
Ggame=0 #индикатор начала рейтинговой игры !start_game()-->1, endGame()-->0
Ngame=0 #подсчет количества игр !(основное тело цикла)
vygr=0 #подсчет выйгрышей
Gcikl=0 #счетчик циклов внутри игры
moneta=0 #индикатор монеты в руке
mana=0  #счетчик маны во время хода
template = "00_btn_game.png"

while "Бесконечный цикл":  # Цикл анализа
    cikl +=1
    print("Цикл =", cikl)
    print("Колличество игр ", Ngame)
    print("Пройгрыш", progr)
    print("Выйгрыш", vygr)
    time.sleep(5)
    ss("00_btn_game.png")
    ss("btn_game.png")
    ss("btn_grec.png")
    ss("btn_game_st.png")
    start_game("btn_start.png")
    if Ggame == 1 :
        Ngame += 1
    while Ggame == 1 :
        Gcikl +=1
        print("цикл ИГРЫ", Gcikl)
        ss("00_btn_game.png")
        ss("btn_game.png")
        ss("btn_grec.png")
        ss("btn_game_st.png")
        ss("btn_start.png")
        ss("btn_ok.png")
        chughoj_hod("chughoj_hod.png") 
        vash_hod("btn_end.png")
        print ("hod=", hod)
        if hod == 1 and game == 1 :
            pyautogui.press(['right'])
            vash_hod("btn_end.png")
            ss("btn_end.png")

        if hod > 1 and hod < 4 and game == 1 :
            pyautogui.press(['right'])
            health("btn_health.png")
            vash_hod("btn_end.png")
            ss("btn_end.png")

        if hod == 4 and game == 1 :
            pyautogui.press(['right'])
            karta("000.png")
            if moneta == 1 :
                mana +=1
                karta("555.png")
                pyautogui.press(['right'])
            else:
                health("btn_health.png")
            moneta=0
            vash_hod("btn_end.png")
            ss("btn_end.png")
            
        if hod ==5 and game == 1:
            pyautogui.press(['right'])
            karta("555.png")
            if unit == 0:
                health("btn_health.png")                      
            pyautogui.press(['right'])
            vash_hod("btn_end.png")
            ss("btn_end.png")
            
        if hod ==6 and game == 1:
            pyautogui.press(['right'])
            karta("666.png")
            pyautogui.press(['right'])
            karta("555.png")            
            if unit == 0:
                health("btn_health.png")                      
            pyautogui.press(['right'])
            vash_hod("btn_end.png")
            ss("btn_end.png")
            
        if hod ==7 and game == 1:
            if unit == 0:
                pyautogui.press(['right'])
                karta("777.png")
                if unit == 1:
                    mana = 0
                if unit == 0:
                    pyautogui.press(['right'])
                    karta("666.png")
                    if unit == 1:
                        mana = 1
                if unit == 0:
                    pyautogui.press(['right'])
                    karta("555.png")
                    if unit == 1:
                        mana = 2
            if mana >= 2:
                health("btn_health.png")                      
            pyautogui.press(['right'])
            vash_hod("btn_end.png")
            ss("btn_end.png")
            
        if hod ==8 and game == 1:
            if unit == 0:
                pyautogui.press(['right'])
                karta("888.png")
                if unit == 1:
                    mana = 0
                if unit == 0:
                    pyautogui.press(['right'])
                    karta("777.png")
                    if unit == 1:
                        mana = 1
                if unit == 0:
                    pyautogui.press(['right'])
                    karta("666.png")
                    if unit == 1:
                        mana = 2
                if unit == 0:
                    pyautogui.press(['right'])
                    karta("555.png")
                    if unit == 1:
                        mana = 3
            if mana >= 2:
                health("btn_health.png")                      
            pyautogui.press(['right'])
            vash_hod("btn_end.png")
            ss("btn_end.png")
            
        if hod ==9 and game == 1:
            if unit == 0:
                pyautogui.press(['right'])
                karta("999.png")
                if unit == 1:
                    mana = 0
                if unit == 0:
                    pyautogui.press(['right'])
                    karta("888.png")
                    if unit == 1:
                        mana = 1
                if unit == 0:
                    pyautogui.press(['right'])
                    karta("777.png")
                    if unit == 1:
                        mana = 2
                if unit == 0:
                    pyautogui.press(['right'])
                    karta("666.png")
                    if unit == 1:
                        mana = 3
                if unit == 0:
                    pyautogui.press(['right'])
                    karta("555.png")
                    if unit == 1:
                        mana = 4
            if mana >= 2:
                health("btn_health.png")                      
            pyautogui.press(['right'])
            vash_hod("btn_end.png")
            ss("btn_end.png")
            
        if hod >= 10 and game == 1:
            if unit == 0:
                pyautogui.press(['right'])
                karta("101010.png")
                if unit == 1:
                    mana = 0
                if unit == 0:
                    pyautogui.press(['right'])
                    karta("999.png")
                    if unit == 1:
                        mana = 1
                if unit == 0:
                    pyautogui.press(['right'])
                    karta("888.png")
                    if unit == 1:
                        mana = 2
                if unit == 0:
                    pyautogui.press(['right'])
                    karta("777.png")
                    if unit == 1:
                        mana = 3
                if unit == 0:
                    pyautogui.press(['right'])
                    karta("666.png")
                    if unit == 1:
                        mana = 4
                if unit == 0:
                    pyautogui.press(['right'])
                    karta("555.png")
                    if unit == 1:
                        mana = 5                
            if mana >= 2:
                health("btn_health.png")                      
            pyautogui.press(['right'])
            vash_hod("btn_end.png")
            ss("btn_end.png")
            
        projgrysh("end_game.png")
        vyjgrysh("victory.png")
        endGame("end_game2.png")
        ss("bt.png")
        ss("bt2.png")
        if Gcikl >= 200:
            Gcikl = 0
            Ggame = 0
            pointclick()
    print("полный цикл") 
#На случай потери соединения
    ss("bt.png")
    ss("bt2.png")
    pointclick()
