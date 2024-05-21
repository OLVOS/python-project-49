from brain_games.engine import run_game
from brain_games.consts import PRIME_RULES
from random import choice


def get_divisors_for_num(number):
    return [i for i in range(2, number + 1)]


def get_num_and_prime_status():
    answer = ''
    num = choice(range(2, 100))
    list_nums_before_num = get_divisors_for_num(num)

    for i in list_nums_before_num:
        if num == i:
            answer = 'yes'
            break
        if num % i == 0:
            answer = 'no'
            break
    return [num, answer]


def run_game_prime():
    run_game(PRIME_RULES, get_num_and_prime_status)
