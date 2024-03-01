import sys
sys.path.append('/home/python-project-49/brain_games')
from engine import welcome_user, game
from random import choice


prime_rules = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def prime_question_answer():
    result = []
    rnd_nums = [choice(range(2, 100)) for i in range(50)]

    for index, number in enumerate(rnd_nums):
        dividers = [i for i in range(2, number)]

        for ind, num in enumerate(dividers):

            if number % num == 0:
                result.append({'question': f'{number}', 'answer': 'no'})
                break

            elif num != dividers[-1]:
                continue

            else:
                result.append({'question': f'{number}', 'answer': 'yes'})
                break

    return result


def run_prime():
    welcome_user()
    game(prime_rules, prime_question_answer())
