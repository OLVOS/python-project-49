import sys
sys.path.append('/home/python-project-49/brain_games/scripts')
sys.path.append('/home/python-project-49/brain_games')
import brain_game
from random import randint


def game():
    print('Answer "yes" if the number is even, otherwise answer "no"')
    count_of_correct = 0
    is_even = []

    while count_of_correct < 3:
        question = randint(0, 101)
        print(f'Question: {question}')

        is_even.clear()
        if question % 2 == 0:
            is_even += ['yes']
        else:
            is_even += ['no']

        user_answer = [input('Your answer: ' )]
        if user_answer == is_even:
            print('Correct!')
            count_of_correct += 1
        else:
            print(f'"{user_answer}" is wrong answer ;(. Correct answer was "{is_even}".')
            print('Let\'s try again, Bill!')

    print('Congratulations, Bill!')


def main():
    brain_game.main()
    game()

if __name__ == '__main__':
    main()
