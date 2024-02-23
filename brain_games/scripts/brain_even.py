import sys
sys.path.append('/home/python-project-49/brain_games/scripts')
sys.path.append('/home/python-project-49/brain_games')
import cli
import brain_game
from random import randint
import time



def time_string(text, sec=0.1):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(sec)


def game():
    time_string('Answer "yes" if the number is even, otherwise answer "no"', sec=0.05)
    time.sleep(2)

    count_of_correct = 0
    is_even = []

    while count_of_correct < 3:
        question = randint(0, 101)
        time_string(f'\nQuestion: {question}')

        is_even.clear()
        is_even.append('yes') if question % 2 == 0 else is_even.append('no')

        user_answer = [input('\nYour answer: ')]
        if user_answer == is_even:
            time_string('Correct!')
            count_of_correct += 1
        else:
            time_string(f'"{user_answer[0]}" is wrong answer ;(. Correct answer was "{is_even[0]}".\n')
            time_string(f'Let\'s try again, {cli.user_name[0]}!')
            time.sleep(1)

    time.sleep(1)
    time_string(f'\nCongratulations, {cli.user_name[0]}!\n')


def main():
    brain_game.main()
    game()

if __name__ == '__main__':
    main()
