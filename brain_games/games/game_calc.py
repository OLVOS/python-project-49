from brain_games.engine import run_game
from brain_games.consts import CALC_RULES, MATH_SIGNS
from random import choice, randint


def get_math_expression_and_result():
    num1, num2 = randint(1, 100), randint(1, 100)
    math_sign = choice(MATH_SIGNS)
    math_expression = f'{num1} {math_sign} {num2}'

    result = eval(math_expression)
    return [math_expression, str(result)]


def run_game_calc():
    run_game(CALC_RULES, get_math_expression_and_result)
