import sys
sys.path.append('/home/python-project-49/brain_games')
from engine import welcome_user, game
from math import gcd
from random import choices


gcd_rules = 'Find the greatest common divisor of given numbers.'


def gcd_question_answer():
    pair_list = [choices(range(2, 100, 6), k=2) for i in range(20)]
    sets = []

    for i, num in enumerate(pair_list):
        first, second = pair_list[i][0], pair_list[i][1]

        sets.append(
            {
                "question": ''.join([f'{first} {second}']),
                "answer": str(gcd(first, second))
            }
        )
    return sets


def run_gcd():
    welcome_user()
    game(gcd_rules, gcd_question_answer())
