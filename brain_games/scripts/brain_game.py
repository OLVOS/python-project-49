#!/usr/bin/env python3
# добавляю cli в sys.path
import sys
sys.path.append('/home/python-project-49/brain_games/scripts')
sys.path.append('/home/python-project-49/brain_games')
#PYTHONPATH='/home/python-project-49/brain_games'
#PYTHONPATH='/home/python-project-49/brain_games/scripts'
import cli


def main():
    print('Welcome to the Brain Games!')
    cli.welcome_user()


if __name__ == '__main__':
    main()
