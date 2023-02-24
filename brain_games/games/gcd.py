from math import gcd
import random

main_task = 'Find the greatest common divisor of given numbers.'

def game_task():
    number_one = random.randint(1, 100)
    number_two = random.randint(1, 100)
    question = f"{number_one} {number_two}"
    correct_answer = str(gcd(number_one, number_two))
    return question, correct_answer
