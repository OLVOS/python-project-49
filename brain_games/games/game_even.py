from brain_games.engine import run_game
from brain_games.consts import EVEN_RULES
from brain_games.utils import get_rnd_num


def is_even(quest):
    return 'yes' if quest % 2 == 0 else 'no'


def get_num_and_even_status():
    question = get_rnd_num()
    answer = is_even(question)
    return question, answer


def run_game_even():
    run_game(EVEN_RULES, get_num_and_even_status)
