#!/usr/bin/env python3
# добавляю cli в sys.path
import sys
sys.path.append('/home/python-project-49/brain_games')
from cli import welcome_user


def main():
    welcome_user()


if __name__ == '__main__':
    main()
