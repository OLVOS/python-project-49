#!/usr/bin/env python3
# добавляю cli в sys.path
import cli
import sys
sys.path.append('/home/python-project-49/brain_games')


def main():
    print('Welcome to the Brain Games!')
    cli.welcome_user()


if __name__ == '__main__':
    main()
