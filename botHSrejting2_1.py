# python3
# bot for hearthstoune rejting game

import subprocess  # Запуск приложений windows
import time  # работа со временем
import keyboard  # работа с нажатиями клавиш

# import bot800x600
import voin_vild
# import mercenaries

def startlnk():  # функция запуска приложения
    subprocess.Popen('C:\Program Files (x86)\Battle.net\Battle.net Launcher.exe')  # запуск приложения
    time.sleep(10)  # время ожидания запуска battle.net
    keyboard.send("windows+up")  # разворачивает приложение на все окно


# исполняемый код

def main():
    while "Бесконечный цикл":  # Цикл анализа
        
        voin_vild.voin_vild_deck()
        # bot800x600.standart_game()
        # mercenaries.mercenaries_deck_mission_1_standart()
        # mercenaries.mercenaries_deck_mission_2_hero()

startlnk()  # запуск приложения Battle.net
if __name__ == "__main__":
    main()
