from brain_games.engine import run_game
from brain_games.consts import EVEN_RULES
from random import randint


def get_rand_int():
    return randint(1, 100)


def get_question_and_answer():
    res = []
    for i in range(3):
        quest = get_rand_int()
        ans = 'yes' if quest % 2 == 0 else 'no'
        res.append([quest, ans])

    return res


def run_game_even():
    run_game(EVEN_RULES, get_question_and_answer())
