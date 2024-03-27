from brain_games.engine import run_game
from brain_games.consts import GCD_RULES
from math import gcd
from random import choices


def get_question_and_answer():
    res = []

    get_list = [choices(range(2, 100, 6), k=2) for i in range(3)]
    for i, num in enumerate(get_list):
        first, second = get_list[i][0], get_list[i][1]

        res.append(
            [
                ''.join([f'{first} {second}']),
                str(gcd(first, second))
            ]
        )
    return res


def run_game_gcd():
    run_game(GCD_RULES, get_question_and_answer())
