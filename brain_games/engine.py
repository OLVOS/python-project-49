from brain_games.cli import welcome_user, user_name


def game(rules, que_ans):
    welcome_user()
    print(rules)

    for i, num in enumerate(que_ans):
        que = que_ans[i]["question"]
        ans = que_ans[i]["answer"]

        print(f'Question: {que}')
        usr_ans = input('Your answer: ')

        if usr_ans == ans:
            print('Correct!')

        else:
            print(f'"{usr_ans}" '
                  ' is wrong answer ;(. Correct answer was '
                  f'"{ans}".\n'
                  f'Let\'s try again, {user_name[0]}!')
            return

    print(f'Congratulations, {user_name[0]}!')
