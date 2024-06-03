import prompt
from brain_games.consts import AMOUNT_OF_ROUNDS


def run_game(rules, get_answer_and_question):
    name = prompt.string('Welcome to the Brain Games!\n'
                         'May I have your name? ')
    print(f'Hello, {name}! \n{rules}')

    for _ in range(AMOUNT_OF_ROUNDS):
        question, correct_answer = get_answer_and_question()
        user_answer = prompt.string(f"Question: {question}\n"
                                    'Your answer: ')

        if user_answer == correct_answer:
            print('Correct!')

        else:
            print(f'"{user_answer}" is wrong answer ;(.'
                  f'Correct answer was "{correct_answer}".\n'
                  f'Let\'s try again, {name}!')
            break

    print(f'Congratulations, {name}!')
