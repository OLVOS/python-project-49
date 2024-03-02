from brain_games.scripts.brain_even import main as even_run
from brain_games.scripts.brain_calc import main as calc_run
from brain_games.scripts.brain_gcd import main as gcd_run
from brain_games.scripts.brain_progression import main as progression_run
from brain_games.scripts.brain_prime import main as prime_run


def run():
    even_run()
    calc_run()
    gcd_run()
    progression_run()
    prime_run()


if __name__ == '__main__':
    run()

