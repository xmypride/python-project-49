from math import gcd
import random

MAIN_TASK = 'Find the greatest common divisor of given numbers.'

LOWER_LIMIT = 1

UPPER_LIMIT = 100


def game_task():
    number_one = random.randint(LOWER_LIMIT, UPPER_LIMIT)
    number_two = random.randint(LOWER_LIMIT, UPPER_LIMIT)
    question = f"{number_one} {number_two}"
    correct_answer = str(gcd(number_one, number_two))
    return question, correct_answer
