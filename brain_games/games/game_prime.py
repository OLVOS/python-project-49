from brain_games.engine import run_game
from brain_games.consts import PRIME_RULES
from random import choice


def get_divisors_of_num(num):
    res = []
    for number in num:
        res.append([i for i in range(2, number)])
    return res


def get_question_and_answer(divisors):
    res = []

    num = [choice(range(2, 100)) for i in range(3)]
    div = divisors(num)

    for index, number in enumerate(num):
        for i, num in enumerate(div[index]):
            prime_num = div[index][-1]
            current_div = div[index][i]

            if number % current_div == 0:
                res.append([number, 'no'])
                break
            elif current_div == prime_num:
                res.append([number, 'yes'])
                break

    return res


def prime_final():
    return get_question_and_answer(get_divisors_of_num)


def run_game_prime():
    run_game(PRIME_RULES, prime_final())
