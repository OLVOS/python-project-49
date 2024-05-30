from brain_games.engine import run_game
from brain_games.consts import PROGRESSION_RULES, PROGRESSION_LENGTH
from brain_games.utils import get_rnd_num


def get_progr_and_cipher_char():
    start, step = get_rnd_num(), get_rnd_num()
    progression = [start + step * i for i in range(PROGRESSION_LENGTH)]

    cipher_index = get_rnd_num(1, 8)
    cipher_char = progression[cipher_index]
    progression[cipher_index] = ".."

    progr = ' '.join(map(str, progression))
    return progr, str(cipher_char)


def run_game_progression():
    run_game(PROGRESSION_RULES, get_progr_and_cipher_char)
