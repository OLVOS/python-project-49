import sys
sys.path.append('/home/python-project-49/brain_games/scripts')
sys.path.append('/home/python-project-49/brain_games')
import cli
import brain_game
from random import shuffle
import time


def time_string(text, sec=0.1):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(sec)


even_rules = 'Answer "yes" if the number is even, otherwise answer "no"'
ans = []


def even_question():
    even_list = []
    for i in range(0, 100):
        even_list.append(i)
    shuffle(even_list)

    que = []

    ans.clear()
    for num in even_list:
        if num % 2 == 0:
            que.append([num])
            ans.append('yes')

        else:
            que.append([num])
            ans.append('no')

    return iter(que)


def even_answer():
    return iter(ans)


def game(rules, def_question, def_answer):
    current_correct_answer = 0

    time_string(rules, sec=0.05)
    time.sleep(1)

    while current_correct_answer < 3:
        question = next(def_question)
        answer = next(def_answer)

        time_string(f'\nQuestion: {question[0]}')

        user_answer = input('\nYour answer: ')

        if user_answer == answer:
                time_string('Correct!')
                current_correct_answer += 1
        else:
            time_string(f'"{user_answer}" is wrong answer ;(. Correct answer was "{answer}".\n')
            time_string(f'Let\'s try again, {cli.user_name[0]}!')
            time.sleep(1)

    time.sleep(1)
    time_string(f'\nCongratulations, {cli.user_name[0]}!\n')


def main():
    brain_game.main()
    game(even_rules, even_question(), even_answer())


if __name__ == '__main__':
    main()

