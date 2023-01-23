from game import game
from humor import humor
from music import music
from movie import movie
from time import sleep
from colorama import Fore, Style


def menu():
    print()
    print(Fore.BLUE + f'{"~" * 50}\n{"# " * 25}\n{"~" * 50}' + Style.RESET_ALL)
    txt = 'Привіт. Я розважальний бот'
    for i in txt:
        sleep(0.1)
        print(i, end='', flush=True)
    sleep(0.3)
    print()
    while True:
        print(Fore.BLUE + f'{"~" * 50}\n{"# " * 25}\n{"~" * 50}' + Style.RESET_ALL)
        value = input('\nЧим хочеш зайнятися?\n\t1. Подивитися фільм\n\t2. Послухати музику\n\t'
                          '3. Пограти в ігри\n\t4. Посміятися\n\t0. Попрощатися зі мною\n'
                          'Що обираєш? ')
        match value:
            case "1":
                print(Fore.BLUE + f'{"~" * 50}\n{"# " * 25}\n{"~" * 50}' + Style.RESET_ALL)
                movie()
            case "2":
                print(Fore.BLUE + f'{"~" * 50}\n{"# " * 25}\n{"~" * 50}' + Style.RESET_ALL)
                music()
            case "3":
                game()
            case "4":
                print(Fore.BLUE + f'{"~" * 50}\n{"# " * 25}\n{"~" * 50}' + Style.RESET_ALL)
                humor()
            case "0":
                break
            case _:
                print(Fore.BLUE + f'{"~" * 50}\n{"# " * 25}\n{"~" * 50}' + Style.RESET_ALL)
                print('Я тебе не зрозумів. Обери пункт меню корректно.')


if __name__ == '__main__':
    menu()
    