import prompt


user_name = []


def welcome_user():
    print('Welcome to the Brain Games!')
    name_ask = prompt.string('May I have your name? ')
    user_name.append(f'{name_ask}')

    print(f'Hello, {user_name[0]}!')


def main():
    welcome_user()


if __name__ == '__main__':
    main()
