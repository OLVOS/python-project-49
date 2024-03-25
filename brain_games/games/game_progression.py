from brain_games.engine import run_game
from brain_games.consts import PROGRESSION_RULES
from random import randint


def get_progr_and_char():
    progr_lst = []
    char_in_progr_list = []

    for _ in range(3):
        step = randint(2, 9)
        range1 = randint(2, 100)
        range2 = (range1 + (step * 10))

        progr_lst += [[str(i) for i in range(range1, range2, step)]]
        char_in_progr_list += [progr_lst[_][step]]

    return {'progr_lst': progr_lst, 'char_in_progr_lst': char_in_progr_list}


def get_cipher(progr_char):
    progr_lst = progr_char['progr_lst']
    char_in_progr_lst = progr_char['char_in_progr_lst']

    for _, char in enumerate(char_in_progr_lst):
        for index, item in enumerate(progr_lst[_]):
            if char == item:
                progr_lst[_][index] = '..'
                break

    return progr_char


def get_question_and_answer(progr_char):
    result = []

    for j, number in enumerate(progr_char['progr_lst']):
        result.append(
            [
                ' '.join(progr_char['progr_lst'][j]),
                progr_char['char_in_progr_lst'][j]
            ]
        )
    return result


def progr_final():
    return get_question_and_answer(get_cipher(get_progr_and_char()))


def run_game_progression():
    run_game(PROGRESSION_RULES, progr_final())
