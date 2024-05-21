from brain_games.engine import run_game
from brain_games.consts import PROGRESSION_RULES
from random import randint


def get_format_progression(lst):
    res = [" ".join(i) for i in [lst]]
    return res


def get_progr_and_cipher_char():
    step = randint(2, 9)
    range1 = randint(2, 20)
    range2 = (range1 + (step * 10))
    progr_lst = [str(i) for i in range(range1, range2, step)]
    cipher_char_in_progr = progr_lst[step]

    for index, item in enumerate(progr_lst):
        if item == cipher_char_in_progr:
            progr_lst[index] = '..'

    format_progr = get_format_progression(progr_lst)
    return [*format_progr, cipher_char_in_progr]


def run_game_progression():
    run_game(PROGRESSION_RULES, get_progr_and_cipher_char)
