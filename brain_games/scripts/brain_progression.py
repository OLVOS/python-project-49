from brain_games.engine import game
from random import randint


progression_rules = 'What number is missing in the progression?'


def progr_and_char():
    progr_lst = []
    char_in_nums_list = []

    for _ in range(3):
        step = randint(2, 9)
        range1 = randint(2, 100)

        progr_lst += [[str(i) for i in range(range1, (range1 + (step * 10)), step)]]
        char_in_nums_list += [progr_lst[_][step]]
    return {'progr_lst': progr_lst, 'char_in_nums_list': char_in_nums_list}


def progr_cipher(progr_char):
    for _, char in enumerate(progr_char['char_in_nums_list']):
        for index, item in enumerate(progr_char['progr_lst'][_]):
            if char == item:
                progr_char['progr_lst'][_][index] = '..'
                break
    return progr_char


def progr_question_answer(progr_char):
    result = []

    for j, number in enumerate(progr_char['progr_lst']):
        result.append(
            {
                "question": ' '.join(progr_char['progr_lst'][j]),
                "answer": progr_char['char_in_nums_list'][j]
            }
        )
    return result


def progr_final():
    return progr_question_answer(progr_cipher(progr_and_char()))


def main():
    game(progression_rules, progr_final())


if __name__ == '__main__':
    main()

