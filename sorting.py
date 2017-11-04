from random import randint
import random


def get_random_list(rng, low=2, high=8, type="int"):
    if type is "float":
        lst = [random.uniform(low, high) for i in range(rng)]
    elif type is "int":
        lst = [randint(-1000, 1000) for i in range(rng)]
    return lst
