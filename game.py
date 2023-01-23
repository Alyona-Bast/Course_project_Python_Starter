from XO import xo_1, xo_2
from RSPLS import rspls
from colorama import Fore, Style

import json


def game():
    while True:
        print(Fore.YELLOW + f'{"~" * 50}\n{"# " * 25}\n{"~" * 50}' + Style.RESET_ALL)
        value = input('\nУ що саме хочеш зіграти?\n\t1. Хрестики-нулики зі мною\n\t'
                      '2. Хрестики-нулики з другом\n\t'
                      '3. Камінь-ножиці-папір-ящірка-Спок\n\t'
                      '4. Подивитися турнірну таблицю\n\t0. Зайнятися чимось іншим\n'
                          'Що обираєш? ')
        match value:
            case "1":
                while True:
                    print(Fore.YELLOW + f'{"~" * 50}\n{"# " * 25}\n{"~" * 50}' + Style.RESET_ALL)
                    xo_1()
                    if input("Бажаєш ще одну партію? Натисни 1\n"
                             "Повернутися у меню, натисни Enter") == "1":
                        pass
                    else:
                        break
            case "2":
                while True:
                    print(Fore.YELLOW + f'{"~" * 50}\n{"# " * 25}\n{"~" * 50}' + Style.RESET_ALL)
                    xo_2()
                    if input("Бажаєш ще одну партію? Натисни 1\n"
                             "Повернутися у меню, натисни Enter") == "1":
                        pass
                    else:
                        break
            case "3":
                while True:
                    print(Fore.YELLOW + f'{"~" * 50}\n{"# " * 25}\n{"~" * 50}' + Style.RESET_ALL)
                    rspls()
                    if input("Бажаєш ще одну партію? Натисни 1\n"
                             "Повернутися у меню, натисни Enter") == "1":
                        pass
                    else:
                        break
            case "4":
                standings()
            case "0":
                break
            case _:
                print('Я тебе не зрозумів. Обери пункт меню корректно.')


def standings():
    while True:
        print(Fore.YELLOW + f'{"~" * 50}\n{"# " * 25}\n{"~" * 50}' + Style.RESET_ALL)
        value = input('\nПереможців якої гри хочеш подивитися?\n\t1. Хрестики-нулики\n\t'
                      '2. Камінь-ножиці-папір-ящірка-Спок\n\t'
                      '0. Якщо передумав\n'
                          'Що обираєш? ')
        match value:
            case "1":
                print(Fore.YELLOW + f'{"~" * 50}\n{"# " * 25}\n{"~" * 50}' + Style.RESET_ALL)
                print(Fore.GREEN + "╔╗╔╗╔╗╔══╗╔╗─╔╗╔╗─╔╗╔═══╗╔═══╗")
                print("║║║║║║╚╗╔╝║╚═╝║║╚═╝║║╔══╝║╔═╗║")
                print("║║║║║║─║║─║╔╗─║║╔╗─║║╚══╗║╚═╝║")
                print("║║║║║║─║║─║║╚╗║║║╚╗║║╔══╝║╔╗╔╝")
                print("║╚╝╚╝║╔╝╚╗║║─║║║║─║║║╚══╗║║║║─")
                print("╚═╝╚═╝╚══╝╚╝─╚╝╚╝─╚╝╚═══╝╚╝╚╝─" + Style.RESET_ALL)
                print("В \"Хрестики-нулики перемагали:\"")
                with open("xo_winner.json", "r", encoding="utf-8") as f:
                    data = json.load(f)
                    for key, value in data.items():
                        print(key, value)
            case "2":
                print(Fore.YELLOW + f'{"~" * 50}\n{"# " * 25}\n{"~" * 50}' + Style.RESET_ALL)
                print(Fore.GREEN + "╔╗╔╗╔╗╔══╗╔╗─╔╗╔╗─╔╗╔═══╗╔═══╗")
                print("║║║║║║╚╗╔╝║╚═╝║║╚═╝║║╔══╝║╔═╗║")
                print("║║║║║║─║║─║╔╗─║║╔╗─║║╚══╗║╚═╝║")
                print("║║║║║║─║║─║║╚╗║║║╚╗║║╔══╝║╔╗╔╝")
                print("║╚╝╚╝║╔╝╚╗║║─║║║║─║║║╚══╗║║║║─")
                print("╚═╝╚═╝╚══╝╚╝─╚╝╚╝─╚╝╚═══╝╚╝╚╝─" + Style.RESET_ALL)
                print('В "Камінь-ножиці-папір-ящірка-Спок" перемагали:')
                with open("rspls_winner.json", "r", encoding="utf-8") as f:
                    data = json.load(f)
                    for key, value in data.items():
                        print(key, value)
            case "0":
                break
            case _:
                print('Я тебе не зрозумів. Обери пункт меню корректно.')