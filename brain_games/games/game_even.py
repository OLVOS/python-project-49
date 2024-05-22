from brain_games.engine import run_game
from brain_games.consts import EVEN_RULES
from random import randint


def get_num_and_even_status():
    question = randint(1, 100)
    answer = 'yes' if question % 2 == 0 else 'no'
    return [question, answer]


def run_game_even():
    run_game(EVEN_RULES, get_num_and_even_status)
