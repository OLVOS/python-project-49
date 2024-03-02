from brain_games.engine import welcome_user, game
from random import randint


progression_rules = 'What number is missing in the progression?'


def progression_question_answer():
    result = []
    slice_list = []
    char_list = []

    count_prog = 0
    while count_prog < 20:
        step = randint(2, 9)
        rnd_nums = [str(i) for i in range(2, 200, step)]

        slice_list += [rnd_nums[step:step + 10]]
        char_list += [slice_list[count_prog][step]]

        count_prog += 1

    for index, item in enumerate(slice_list):
        for ind, it in enumerate(item):
            if it == char_list[index]:
                slice_list[index][ind] = '..'

    for j, number in enumerate(slice_list):
        result.append(
            {
                "question": ' '.join(slice_list[j]),
                "answer": char_list[j]
            }
        )

    return result


def main():
    welcome_user()
    game(progression_rules, progression_question_answer())


if __name__ == '__main__':
    main()
