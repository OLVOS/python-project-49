from cli import *
import time


def time_string(text, sec=0.1):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(sec)


def game(rules, def_question_answer):
    current_correct_answer = 0

    time_string(rules, sec=0.05)
    time.sleep(1)

    quest_ans_list = def_question_answer
    for i, num in enumerate(quest_ans_list):
        if current_correct_answer != 3:

            time_string(f'\nQuestion: {quest_ans_list[i]["question"]}')
            user_answer = input('\nYour answer: ')

            if user_answer == quest_ans_list[i]["answer"]:
                time_string('Correct!')
                current_correct_answer += 1
            else:
                time_string(f'"{user_answer}" is wrong answer ;(. Correct answer was "{quest_ans_list[i]["answer"]}".\n', sec=0.05)
                time_string(f'Let\'s try again, {user_name[0]}!')
                time.sleep(1)

    time.sleep(1)
    time_string(f'\nCongratulations, {user_name[0]}!\n')


def main():
    welcome_user()
    game()


if __name__ == '__main__':
    main()

