from brain_games.engine import run_game
from brain_games.consts import PROGRESSION_RULES
from random import randint


def get_progr_and_char():
    progr_lst = []
    cipher_char_in_progr = []
    for _ in range(1):
        step = randint(2, 9)
        range1 = randint(2, 100)
        range2 = (range1 + (step * 10))

        progr_lst += [str(i) for i in range(range1, range2, step)]
        cipher_char_in_progr += [progr_lst[step]]
    return [progr_lst, cipher_char_in_progr]


def get_cipher():
    get_list = get_progr_and_char()
    res = [item for index, item in enumerate(get_list[0])]
    for index, item in enumerate(get_list[0]):
        for i in get_list[1]:
            if item == i:
                get_list[0][index] = '..'
                break
    return get_list


def get_format_progression():
    get_progr = get_cipher()
    res = [" ".join(i) for i in get_progr]
    return res


def run_game_progression():
    run_game(PROGRESSION_RULES, get_format_progression)
