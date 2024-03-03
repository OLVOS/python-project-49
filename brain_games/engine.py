from brain_games.cli import welcome_user, user_name


def game(rules, que_ans):
    welcome_user()
    print(rules)

    correct = 0
    for i, num in enumerate(que_ans):
        if correct != 3:
            que = que_ans[i]["question"]
            ans = que_ans[i]["answer"]
            wrong_txt = "is wrong answer ;(. Correct answer was"

            print(f'Question: {que}')
            usr_ans = input('Your answer: ')

            if usr_ans == ans:
                print('Correct!')
                correct += 1

            else:
                print(f'"{usr_ans}" {wrong_txt} "{ans}".\n'
                      f'Let\'s try again, {user_name[0]}!')

    print(f'Congratulations, {user_name[0]}!')
