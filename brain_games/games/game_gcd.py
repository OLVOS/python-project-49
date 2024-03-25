from brain_games.engine import run_game
from brain_games.consts import GCD_RULES
from math import gcd
from random import choices


def get_question_and_answer():
    pair_list = [choices(range(2, 100, 6), k=2) for i in range(3)]
    sets = []

    for i, num in enumerate(pair_list):
        first, second = pair_list[i][0], pair_list[i][1]

        sets.append(
            [
                ''.join([f'{first} {second}']),
                str(gcd(first, second))
            ]
        )
    return sets


def run_game_gcd():
    run_game(GCD_RULES, get_question_and_answer())
