from brain_games.engine import game
from operator import add, sub, mul
from random import choice, choices


calc_rules = 'What is the result of the expression?'


def calc_question_answer():
    pair_list = [choices(range(50), k=2) for i in range(20)]
    sets = []

    for i, num in enumerate(pair_list):
        op = choice([[add, '+'], [sub, '-'], [mul, '*']])

        first, second = pair_list[i][0], pair_list[i][1]
        sets.append(
            {
                "question": ''.join([f'{first} {op[1]} {second}']),
                "answer": str(op[0](first, second))
            }
        )

    return sets


def main():
    game(calc_rules, calc_question_answer())


if __name__ == '__main__':
    main()
