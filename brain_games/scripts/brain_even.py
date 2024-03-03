from brain_games.engine import game
from random import choice


even_rules = 'Answer "yes" if the number is even, otherwise answer "no".'


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
    game(even_rules, even_question_answer())


if __name__ == '__main__':
    main()
