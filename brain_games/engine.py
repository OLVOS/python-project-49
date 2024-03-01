from cli import welcome_user, user_name
import time


def timer(text, sec=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(sec)


def game(rules, que_ans):
    current_correct_answer = 0

    timer(rules)
    time.sleep(1)

    for i, num in enumerate(que_ans):
        if current_correct_answer != 3:

            timer(f'\nQuestion: {que_ans[i]["question"]}')
            usr_ans = input('\nYour answer: ')

            if usr_ans == que_ans[i]["answer"]:
                timer('Correct!')
                current_correct_answer += 1
            else:
                txt = " is wrong answer ;(. Correct answer was "

                timer(f'"{usr_ans}"{txt}"{que_ans[i]["answer"]}".\n', sec=0.05)
                timer(f'Let\'s try again, {user_name[0]}!')
                time.sleep(1)

    time.sleep(1)
    timer(f'\nCongratulations, {user_name[0]}!\n')


def main():
    welcome_user()
    game()


if __name__ == '__main__':
    main()
