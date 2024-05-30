from brain_games.engine import run_game
from brain_games.consts import GCD_RULES
from brain_games.utils import get_rnd_num_by_step
import math


def get_gcd(num1, num2):
    return math.gcd(num1, num2)


def get_two_nums_and_divisor():
    num_1, num_2 = get_rnd_num_by_step(), get_rnd_num_by_step()
    gcd = get_gcd(num_1, num_2)
    nums = f'{num_1} {num_2}'
    return nums, str(gcd)


def run_game_gcd():
    run_game(GCD_RULES, get_two_nums_and_divisor)
