from random import randint, choice


def get_rnd_num(start=2, end=25):
    return randint(start, end)


def get_rnd_num_by_step(start=2, end=25, step=2):
    return choice(range(start, end, step))
