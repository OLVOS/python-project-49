from brain_games.engine import run_game
from brain_games.consts import PRIME_RULES
from random import choice


def dividers_list(number):
    dividers = []
    for index, number in enumerate(number):
        dividers.append([i for i in range(2, number)])
    return dividers


def prime_question_answer(dividers_lst):
    result = []

    rnd_nums = [choice(range(2, 100)) for i in range(3)]
    dividers = dividers_lst(rnd_nums)

    for index, number in enumerate(rnd_nums):
        for i, num in enumerate(dividers[index]):
            last_number = dividers[index][-1]
            current_div = dividers[index][i]

            if number % current_div == 0:
                result.append([number, 'no'])
                break

            elif current_div == last_number:
                result.append([number, 'yes'])
                break
    return result


def prime_final():
    return prime_question_answer(dividers_list)


def run_game_prime():
    run_game(PRIME_RULES, prime_final())
