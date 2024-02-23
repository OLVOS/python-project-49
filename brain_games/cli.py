import prompt


name_ask = prompt.string('May I have your name? ')
user_name = [f'{name_ask}']

def welcome_user():
    print(f'Hello, {user_name[0]}!')


def main():
    welcome_user()


if __name__ == '__main__':
    main()
