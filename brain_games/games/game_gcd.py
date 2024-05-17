from brain_games.engine import run_game
from brain_games.consts import GCD_RULES
from math import gcd
from random import choice


def get_question_and_answer():
    get_nums_1 = choice(range(2, 100, 6))
    get_nums_2 = choice(range(2, 100, 6))
    res = [f'{get_nums_1} {get_nums_2}', str(gcd(get_nums_1, get_nums_2))]
    return res


def run_game_gcd():
    run_game(GCD_RULES, get_question_and_answer)
