import json
from datetime import datetime
from time import sleep
from colorama import Fore, Style


# Ігрове поле
maps = list(range(1, 10))

#Виграшні комбінації
victories = ((0, 1, 2), (3, 4, 5), (6, 7, 8),
             (0, 3, 6), (1, 4, 7), (2, 5, 8),
             (0, 4, 8), (2, 4, 6))


def print_maps():
    """Малює ігрове поле"""
    print(Fore.BLUE + "--------------" + Style.RESET_ALL)
    for i in range(3):
        print(Fore.BLUE + "|" + Style.RESET_ALL, maps[0+i*3],
              Fore.BLUE + "|" + Style.RESET_ALL, maps[1+i*3],
              Fore.BLUE + "|" + Style.RESET_ALL, maps[2+i*3],
              Fore.BLUE + "|" + Style.RESET_ALL)
        print(Fore.BLUE + "-------------" + Style.RESET_ALL)


def step_maps(step, symbol):
    """Вибір клітинки"""
    ind = maps.index(step)
    maps[ind] = symbol


def get_result():
    """Визначення переможця"""
    win = ""

    for i in victories:
        if maps[i[0]] == "X" and maps[i[1]] == "X" and maps[i[2]] == "X":
            win = "X"
        if maps[i[0]] == "O" and maps[i[1]] == "O" and maps[i[2]] == "O":
            win = "O"

    return win


def check_line(sum_O, sum_X):
    """Перевірка можливості перемоги"""
    global step
    step = ""
    for line in victories:
        o = 0
        x = 0
        for j in range(0, 3):
            if maps[line[j]] == "O":
                o = o + 1
            if maps[line[j]] == "X":
                x = x + 1
        if o == sum_O and x == sum_X:
            for j in range(0, 3):
                if maps[line[j]] != "O" and maps[line[j]] != "X":
                    step = maps[line[j]]
    return step


def AI():
    """Штучний інтеелкт вибирає хід"""
    global step
    step = ""

    check_line(2, 0)
    if step == "":
        check_line(0, 2)
    if step == "":
        check_line(1, 0)
    if step == "":
        check_line(0, 1)
    if step == "":
        if maps[4] != "X" and maps[4] != "O":
            step = 5
    if step == "":
        if maps[0] != "X" and maps[0] != "O":
            step = 1
    return step


def valid_input():
    """Перевірка уведення номера клітинки"""
    valid = False
    print(f"{player_name}, твій хід: ")
    while not valid:
        try:
            step = int(input(f"Обери клітинку: "))
        except:
            print("Уведіть новмер клітинки")
            continue
        if step >= 1 and step <= 9:
            if (str(maps[step-1]) not in "XO"):
                step_maps(step, symbol)
                valid = True
            else:
                print("Ця клітинка вже зайнята")
        else:
            print("Оберіть клітинку від 1 до 9")


def xo_2():
    """Запуск гри на двох гравців"""
    print(Fore.CYAN + "╔══╗╔════╗╔══╗╔═══╗╔════╗")
    print("║╔═╝╚═╗╔═╝║╔╗║║╔═╗║╚═╗╔═╝")
    print("║╚═╗──║║──║╚╝║║╚═╝║──║║──")
    print("╚═╗║──║║──║╔╗║║╔╗╔╝──║║──")
    print("╔═╝║──║║──║║║║║║║║───║║──")
    print("╚══╝──╚╝──╚╝╚╝╚╝╚╝───╚╝──" + Style.RESET_ALL)
    counter = 0
    game_over = False
    player1 = True
    player_name1 = input("Уведіть ім\'я першого гравця: ")
    player_name2 = input("Уведіть ім\'я другого гравця: ")
    global symbol, player_name
    winner = ""
    name_winner = ""

    while not game_over:
        if counter < 9:
            print_maps()
            if player1:
                symbol = "X"
                player_name = player_name1
                valid_input()
            else:
                symbol = "O"
                player_name = player_name2
                valid_input()
            winner = get_result()

            if winner != "":
                game_over = True
            else:
                game_over = False
            player1 = not (player1)
            counter += 1
        else:
            print(Fore.GREEN + "╔╗╔╗╔══╗╔╗╔╗╔╗╔╗╔═══╗")
            print("║║║║╚╗╔╝║║║║║║║║║╔═╗║")
            print("║╚╝║─║║─║╚╝║║║║║║╚═╝║")
            print("║╔╗║─║║─╚═╗║║║╔║╚╗╔╗║")
            print("║║║║╔╝╚╗──║║║╚╝║─║║║║")
            print("╚╝╚╝╚══╝──╚╝╚══╝─╚╝╚╝" + Style.RESET_ALL)
            break
    print_maps()
    if winner == "X":
        name_winner = player_name1
        print(Fore.YELLOW + "╔══╗╔═══╗╔═══╗╔═══╗╔╗──╔╗╔══╗╔══╗╔══╗╔╗")
        print("║╔╗║║╔══╝║╔═╗║║╔══╝║║──║║║╔╗║║╔═╝║╔╗║║║")
        print("║║║║║╚══╗║╚═╝║║╚══╗║╚╗╔╝║║║║║║║──║╚╝║║║")
        print("║║║║║╔══╝║╔══╝║╔══╝║╔╗╔╗║║║║║║║──║╔╗║╚╝")
        print("║║║║║╚══╗║║───║╚══╗║║╚╝║║║╚╝║║║──║║║║╔╗")
        print("╚╝╚╝╚═══╝╚╝───╚═══╝╚╝──╚╝╚══╝╚╝──╚╝╚╝╚╝" + Style.RESET_ALL)
        print(f"Переміг: {winner}. {name_winner}, вітаю!")
    elif winner == "O":
        name_winner = player_name1
        print(Fore.YELLOW + "╔══╗╔═══╗╔═══╗╔═══╗╔╗──╔╗╔══╗╔══╗╔══╗╔╗")
        print("║╔╗║║╔══╝║╔═╗║║╔══╝║║──║║║╔╗║║╔═╝║╔╗║║║")
        print("║║║║║╚══╗║╚═╝║║╚══╗║╚╗╔╝║║║║║║║──║╚╝║║║")
        print("║║║║║╔══╝║╔══╝║╔══╝║╔╗╔╗║║║║║║║──║╔╗║╚╝")
        print("║║║║║╚══╗║║───║╚══╗║║╚╝║║║╚╝║║║──║║║║╔╗")
        print("╚╝╚╝╚═══╝╚╝───╚═══╝╚╝──╚╝╚══╝╚╝──╚╝╚╝╚╝" + Style.RESET_ALL)
        print(f"Переміг: {winner}. {name_winner}, вітаю!")

    winner_dict = {datetime.now().strftime("%d-%m-%Y %H:%M"): name_winner}
    with open("xo_winner.json", "r", encoding="utf-8") as fr:
        data = json.load(fr)

    with open("xo_winner.json", "w", encoding="utf-8") as fw:
        data.update(winner_dict)
        json.dump(data, fw)
    global maps
    maps = list(range(1, 10))


def xo_1():
    """Запуск гри з ботом"""
    print(Fore.CYAN + "╔══╗╔════╗╔══╗╔═══╗╔════╗")
    print("║╔═╝╚═╗╔═╝║╔╗║║╔═╗║╚═╗╔═╝")
    print("║╚═╗──║║──║╚╝║║╚═╝║──║║──")
    print("╚═╗║──║║──║╔╗║║╔╗╔╝──║║──")
    print("╔═╝║──║║──║║║║║║║║───║║──")
    print("╚══╝──╚╝──╚╝╚╝╚╝╚╝───╚╝──" + Style.RESET_ALL)
    game_over = False
    player1 = True
    global symbol, player_name
    player_name = input("Уведіть своє ім\'я: ")
    counter = 0
    winner = ""

    while not game_over:
        if counter < 9:
            print_maps()
            if player1:
                symbol = "X"
                valid_input()
            else:
                print("Тепер мій хід")
                sleep(1)
                symbol = "O"
                AI()
                step_maps(step, symbol)
            winner = get_result()

            if winner != "":
                game_over = True
            else:
                game_over = False
            player1 = not (player1)
            counter += 1
        else:
            print(Fore.GREEN + "╔╗╔╗╔══╗╔╗╔╗╔╗╔╗╔═══╗")
            print("║║║║╚╗╔╝║║║║║║║║║╔═╗║")
            print("║╚╝║─║║─║╚╝║║║║║║╚═╝║")
            print("║╔╗║─║║─╚═╗║║║╔║╚╗╔╗║")
            print("║║║║╔╝╚╗──║║║╚╝║─║║║║")
            print("╚╝╚╝╚══╝──╚╝╚══╝─╚╝╚╝" + Style.RESET_ALL)
            break
    print_maps()
    if winner == "X":
        print(Fore.YELLOW + "╔══╗╔═══╗╔═══╗╔═══╗╔╗──╔╗╔══╗╔══╗╔══╗╔╗")
        print("║╔╗║║╔══╝║╔═╗║║╔══╝║║──║║║╔╗║║╔═╝║╔╗║║║")
        print("║║║║║╚══╗║╚═╝║║╚══╗║╚╗╔╝║║║║║║║──║╚╝║║║")
        print("║║║║║╔══╝║╔══╝║╔══╝║╔╗╔╗║║║║║║║──║╔╗║╚╝")
        print("║║║║║╚══╗║║───║╚══╗║║╚╝║║║╚╝║║║──║║║║╔╗")
        print("╚╝╚╝╚═══╝╚╝───╚═══╝╚╝──╚╝╚══╝╚╝──╚╝╚╝╚╝" + Style.RESET_ALL)
        print(f"Переміг: {winner}. {player_name}, вітаю!")
        winner_dict = {datetime.now().strftime("%d-%m-%Y %H:%M"): player_name}

        with open("xo_winner.json", "r", encoding="utf-8") as fr:
            data = json.load(fr)

        with open("xo_winner.json", "w", encoding="utf-8") as fw:
            data.update(winner_dict)
            json.dump(data, fw)
    elif winner == "O":
        print(Fore.RED + "╔═══╗───╔══╗─╔╗╔╗╔══╗╔═══╗╔══╗╔══╗─╔╗")
        print("║╔═╗║───║╔╗║─║║║║║╔═╝║╔═╗║║╔╗║║╔╗║─║║")
        print("║╚═╝║───║╚╝╚╗║║║║║║──║╚═╝║║╚╝║║╚╝╚╗║║")
        print("╚╗╔╗║───║╔═╗║║║╔║║║──║╔══╝║╔╗║║╔═╗║╚╝")
        print("─║║║║───║╚═╝║║╚╝║║║──║║───║║║║║╚═╝║╔╗")
        print("─╚╝╚╝───╚═══╝╚══╝╚╝──╚╝───╚╝╚╝╚═══╝╚╝" + Style.RESET_ALL)
        print(f"Перемога за мною!")
    global maps
    maps = list(range(1, 10))




