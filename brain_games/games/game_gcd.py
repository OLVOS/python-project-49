from brain_games.engine import run_game
from brain_games.consts import GCD_RULES
from brain_games.utils import get_rnd_num
import math


def get_gcd(num1, num2):
    return math.gcd(num1, num2)


def get_two_nums_and_divisor():
    first_name, second_name = get_rnd_num(), get_rnd_num()
    gcd = get_gcd(first_name, second_name)
    nums = f'{first_name} {second_name}'
    return nums, str(gcd)


def run_game_gcd():
    run_game(GCD_RULES, get_two_nums_and_divisor)
