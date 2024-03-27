from brain_games.engine import run_game
from brain_games.consts import CALC_RULES, OPERANDS
from random import choice, choices


def get_question_and_answer():
    res = []

    get_list = [choices(range(50), k=2) for i in range(3)]
    for i, num in enumerate(get_list):
        op = choice(OPERANDS)

        first, second = get_list[i][0], get_list[i][1]

        res.append(
            [
                ''.join([f'{first} {op[1]} {second}']),
                str(op[0](first, second))
            ]
        )

    return res


def run_game_calc():
    run_game(CALC_RULES, get_question_and_answer())
