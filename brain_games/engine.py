from cli import welcome_user, user_name
import time


def timer(text, sec=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(sec)


def game(rules, que_ans):
    timer(rules)
    time.sleep(1)

    correct_ans = 0
    for i, num in enumerate(que_ans):
        que = que_ans[i]["question"]
        ans = que_ans[i]["answer"]
        wrong_txt = "is wrong answer ;(. Correct answer was"

        if correct_ans != 3:
            timer(f'\nQuestion: {que}')
            usr_ans = input('\nYour answer: ')

            if usr_ans == ans:
                timer('Correct!')
                correct_ans += 1

            else:
                timer(f'"{usr_ans}" {wrong_txt} "{ans}".\n', sec=0.05)
                timer(f'Let\'s try again, {user_name[0]}!')
                time.sleep(1)

    time.sleep(1)
    timer(f'\nCongratulations, {user_name[0]}!\n')


def main():
    welcome_user()
    game()


if __name__ == '__main__':
    main()
