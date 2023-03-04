import random

MAIN_TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'

# The minimum possible number in the expression
LOWER_LIMIT = 2

# The maximum possible number in the expression
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
    if correct_answer:
        return question, 'yes'
    else:
        return question, 'no'


if __name__ == '__main__':
    game_task()
