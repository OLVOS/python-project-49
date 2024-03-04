from brain_games.engine import game
from random import choice


prime_rules = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def dividers_list(number):
    dividers = []
    for index, number in enumerate(number):
        dividers.append([i for i in range(2, number)])
    return dividers


def prime_question_answer(dividers_lst):
    result = []

    rnd_nums = [choice(range(2, 100)) for i in range(3)]
    dividers = dividers_lst(rnd_nums)

    for index, number in enumerate(rnd_nums):
        for i, num in enumerate(dividers[index]):
            last_number = dividers[index][-1]
            current_div = dividers[index][i]

            if number % current_div == 0:
                result.append({'question': f'{number}', 'answer': 'no'})
                break

            elif current_div == last_number:
                result.append({'question': f'{number}', 'answer': 'yes'})
                break

    return result


def prime_final():
    return prime_question_answer(dividers_list)


def main():
    game(prime_rules, prime_final())


if __name__ == '__main__':
    main()
