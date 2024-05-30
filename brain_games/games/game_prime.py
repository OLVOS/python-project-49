from brain_games.engine import run_game
from brain_games.consts import PRIME_RULES
from brain_games.utils import get_rnd_num


def is_prime(num):
    num_root = num ** 0.5
    for i in range(2, int(num_root) + 1):
        if num % i == 0:
            return False
    return True


def get_num_and_prime_status():
    num = get_rnd_num()
    answer = True if is_prime(num) else False
    return num, answer


def run_game_prime():
    run_game(PRIME_RULES, get_num_and_prime_status)
