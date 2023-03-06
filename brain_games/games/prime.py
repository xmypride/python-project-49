import random

MAIN_TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'

LOWER_LIMIT = 2

UPPER_LIMIT = 100


def prime(number):
    for i in range(LOWER_LIMIT, int(number - 1)):
        if number % i == 0:
            return False
    return True


def game_task():
    number = random.randint(LOWER_LIMIT, UPPER_LIMIT)
    question = number
    correct_answer = prime(number)
    return (question, 'yes') if correct_answer else (question, 'no')
