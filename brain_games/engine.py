import prompt
from brain_games.consts import AMOUNT_OF_ROUDS


def run_game(rules, get_answer_and_question):
    name = prompt.string('Welcome to the Brain Games!\n'
                         'May I have your name? ')
    print(f'Hello, {name}!', f'\n{rules}')

    for i in range(AMOUNT_OF_ROUDS):
        question, correct_answer = get_answer_and_question()
        print('Question:', question)
        user_answer = prompt.string('Answer: ')

        if user_answer == correct_answer:
            print('Correct!')

        else:
            print(f'"{user_answer}" '
                  ' is wrong answer ;(. Correct answer was '
                  f'"{correct_answer}".\n'
                  f'Let\'s try again, {name}!')
            break
    else:
        print(f'Congratulations, {name}!')
