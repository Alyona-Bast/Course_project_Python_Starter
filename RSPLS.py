from random import randint
from datetime import datetime
import json
from PIL import Image
from colorama import Fore, Style


action_dict = {1: "КАМІНЬ", 2: "НОЖИЦІ", 3: "ПАПІР", 4: "ЯЩІРКА", 5: "СПОК"}
game_score = {"user": 0, "bot": 0}

def determine_winner(user_select, comp_select):
    if user_select == comp_select:
        print(f"Обидва гравці вибрали {action_dict[user_select]}. Нічия!")
    elif user_select == 1:
        if comp_select == 2:
            print("Камінь ламає ножиці. Ти переміг!")
            game_score["user"] += 1
        elif comp_select == 3:
            print("Папір загортає камінь. Перемога за мною!")
            game_score["bot"] += 1
        elif comp_select == 4:
            print("Камінь б\'є ящірку. Ти переміг!")
            game_score["user"] += 1
        elif comp_select == 5:
            print("Спок відкидає камінь. Перемога за мною!")
            game_score["bot"] += 1
    elif user_select == 2:
        if comp_select == 1:
            print("Ножиці ламаються об камінь. Перемога за мною!")
            game_score["bot"] += 1
        elif comp_select == 3:
            print("Ножиці ріжуть папір. Ти переміг!")
            game_score["user"] += 1
        elif comp_select == 4:
            print("Ножиці ріжуть ящірку. Ти переміг!")
            game_score["user"] += 1
        elif comp_select == 5:
            print("Спок ламає ножиці. Перемога за мною!")
            game_score["bot"] += 1
    elif user_select == 3:
        if comp_select == 1:
            print("Папір загортає камінь. Ти переміг!")
            game_score["user"] += 1
        elif comp_select == 2:
            print("Ножиці ріжуть папір. Перемога за мною!")
            game_score["bot"] += 1
        elif comp_select == 4:
            print("Ящірка їсть папір. Перемога за мною!")
            game_score["bot"] += 1
        elif comp_select == 5:
            print("Папір підставляє Спока. Ти переміг!")
            game_score["user"] += 1
    elif user_select == 4:
        if comp_select == 1:
            print("Камінь б\'є ящірку. Перемога за мною!")
            game_score["bot"] += 1
        elif comp_select == 2:
            print("Ножиці ріжуть ящірку. Перемога за мною!")
            game_score["bot"] += 1
        elif comp_select == 3:
            print("Ящірка їсть папір. Ти переміг!")
            game_score["user"] += 1
        elif comp_select == 5:
            print("Ящірка отруює Спока. Ти переміг!")
            game_score["user"] += 1
    elif user_select == 5:
        if comp_select == 1:
            print("Спок відкидає камінь. Ти переміг!")
            game_score["user"] += 1
        elif comp_select == 2:
            print("Спок ламає ножиці. Ти переміг!")
            game_score["user"] += 1
        elif comp_select == 3:
            print("Папір підставляє Спока. Перемога за мною!")
            game_score["bot"] += 1
        elif comp_select == 4:
            print("Ящірка отруює Спока. Перемога за мною!")
            game_score["bot"] += 1

def get_computer_selection():
    selection = randint(1, 5)
    print(f'Я обираю: {action_dict[selection]}')
    return selection


def get_user_selection():
    while True:
        try:
            user_input = int(input(Fore.YELLOW + "КАМІНЬ[1], НОЖИЦІ[2], ПАПІР[3],"
                                                 "ЯЩІРКА[4], СПОК[5]" + Style.RESET_ALL + "\n Обери дію: "))
            if user_input > 0 and user_input < 6:
                break
            else:
                print("Обери число від 1 до 5")
        except ValueError:
            print("Обери число від 1 до 5")
    print(f'Ти вибрав: {action_dict[user_input]}')
    return user_input



def rspls():
    print(Fore.CYAN + "╔══╗╔════╗╔══╗╔═══╗╔════╗")
    print("║╔═╝╚═╗╔═╝║╔╗║║╔═╗║╚═╗╔═╝")
    print("║╚═╗──║║──║╚╝║║╚═╝║──║║──")
    print("╚═╗║──║║──║╔╗║║╔╗╔╝──║║──")
    print("╔═╝║──║║──║║║║║║║║───║║──")
    print("╚══╝──╚╝──╚╝╚╝╚╝╚╝───╚╝──" + Style.RESET_ALL)
    while True:
        if input("Хочеш дізнатися правила гри? Натисни 1\n"
                 "Щоб зіграти, натисни Enther: ") == "1":
            Image.open("rspls.jpg").show()
        else:
            break
    user_name = input("Уведіть своє ім\'я: ")
    user_select = get_user_selection()
    comp_select = get_computer_selection()
    determine_winner(user_select, comp_select)
    print(f'Рахунок: {game_score["user"]} : {game_score["bot"]}')
    while True:
        print(Fore.YELLOW + f'{"~" * 50}' + Style.RESET_ALL)
        if input("Граємо ще раз? Натисни 1\n"
                 "Щоб завершити, натисни Enther: ") == "1":
            determine_winner(get_user_selection(), get_computer_selection())
            print(f'Рахунок: {game_score["user"]} : {game_score["bot"]}')
            print()
        else:
            break
    if game_score["user"] > game_score["bot"]:
        print(Fore.YELLOW + "╔══╗╔═══╗╔═══╗╔═══╗╔╗──╔╗╔══╗╔══╗╔══╗╔╗")
        print("║╔╗║║╔══╝║╔═╗║║╔══╝║║──║║║╔╗║║╔═╝║╔╗║║║")
        print("║║║║║╚══╗║╚═╝║║╚══╗║╚╗╔╝║║║║║║║──║╚╝║║║")
        print("║║║║║╔══╝║╔══╝║╔══╝║╔╗╔╗║║║║║║║──║╔╗║╚╝")
        print("║║║║║╚══╗║║───║╚══╗║║╚╝║║║╚╝║║║──║║║║╔╗")
        print("╚╝╚╝╚═══╝╚╝───╚═══╝╚╝──╚╝╚══╝╚╝──╚╝╚╝╚╝" + Style.RESET_ALL)
        print(f"Переміг: {user_name}, вітаю!")
        print(f'{user_name}, вітаю! Ти переміг(ла) з рахунком: {game_score["user"]} : {game_score["bot"]}')

        winner_dict = {datetime.now().strftime("%d-%m-%Y %H:%M"):
                           f'{user_name}, рахунок: {game_score["user"]} : {game_score["bot"]}'}
        with open("rspls_winner.json", "r", encoding="utf-8") as fr:
            data = json.load(fr)

        with open("rspls_winner.json", "w", encoding="utf-8") as fw:
            data.update(winner_dict)
            json.dump(data, fw)
    elif game_score["user"] == game_score["bot"]:
        print(Fore.GREEN + "╔╗╔╗╔══╗╔╗╔╗╔╗╔╗╔═══╗")
        print("║║║║╚╗╔╝║║║║║║║║║╔═╗║")
        print("║╚╝║─║║─║╚╝║║║║║║╚═╝║")
        print("║╔╗║─║║─╚═╗║║║╔║╚╗╔╗║")
        print("║║║║╔╝╚╗──║║║╚╝║─║║║║")
        print("╚╝╚╝╚══╝──╚╝╚══╝─╚╝╚╝" + Style.RESET_ALL)
        print(f'Нічия. Рахунок: {game_score["user"]} : {game_score["bot"]}')
    else:
        print(Fore.RED + "╔═══╗───╔══╗─╔╗╔╗╔══╗╔═══╗╔══╗╔══╗─╔╗")
        print("║╔═╗║───║╔╗║─║║║║║╔═╝║╔═╗║║╔╗║║╔╗║─║║")
        print("║╚═╝║───║╚╝╚╗║║║║║║──║╚═╝║║╚╝║║╚╝╚╗║║")
        print("╚╗╔╗║───║╔═╗║║║╔║║║──║╔══╝║╔╗║║╔═╗║╚╝")
        print("─║║║║───║╚═╝║║╚╝║║║──║║───║║║║║╚═╝║╔╗")
        print("─╚╝╚╝───╚═══╝╚══╝╚╝──╚╝───╚╝╚╝╚═══╝╚╝" + Style.RESET_ALL)
        print(f'Я переміг з рахунком: {game_score["user"]} : {game_score["bot"]}')





