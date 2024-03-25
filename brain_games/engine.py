
def run_game(rules, get_answer_and_question):
    name = input('Welcome to the Brain Games!\n'
                 'May I have your name? ')
    print(f'Hello, {name}!')
    print(rules)

    for attempt_index, el in enumerate(get_answer_and_question):
        question, correct_answer = get_answer_and_question[attempt_index]

        print('Question:', question)
        user_answer = input('Answer: ')
        if user_answer == correct_answer:
            print('Correct!')
        else:
            print(f'"{user_answer}" '
                  ' is wrong answer ;(. Correct answer was '
                  f'"{correct_answer}".\n'
                  f'Let\'s try again, {name}!')
            return

    print(f'Congratulations, {name}!')
