import sys
sys.path.append('/home/python-project-49/brain_games')
from engine import *
from random import randint


gcd_rules = 'Find the greatest common divisor of given numbers.'


def progression_question_answer():
    result = []
    cut_list = []
    replace_list = []

    count = 0

    while count < 20:
        step = randint(2, 9)
        pair_list = [str(i) for i in range(2, 200, step)]

        progression_list = pair_list[step:step+10]
        cut_list.append(progression_list)

        prog_char = [progression_list[step]]
        replace_list.append(prog_char)

        count += 1

    for index, item in enumerate(cut_list):

        for ind, it in enumerate(item):

            if it == replace_list[index][0]:
                cut_list[index][ind] = '..'

    for j, number in enumerate(cut_list):
        result.append(
            {
                "question": ' '.join(cut_list[j]),
                "answer": replace_list[j][0]
            }
        )

    return result


def main():
    welcome_user()
    game(gcd_rules, progression_question_answer())


if __name__ == '__main__':
    main()

