import sys
sys.path.append('/home/python-project-49/brain_games')
from engine import welcome_user, game
from random import choice


even_rules = 'Answer "yes" if the number is even, otherwise answer "no"'


def even_question_answer():
    pair_list = [choice(range(50)) for i in range(20)]
    sets = []

    for i in pair_list:
        if i % 2 == 0:
            sets.append({"question": i, "answer": 'yes'})
        else:
            sets.append({"question": i, "answer": 'no'})

    return sets


def main():
    welcome_user()
    game(evem_rules, even_question_answer())


if __name__ == '__main__':
    main()
