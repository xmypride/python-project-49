import random

MAIN_TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def prime(number):
    for i in range(2, int(number - 1)):
        if number % i == 0:
            return 'no'
    return 'yes'


def game_task():
    number = random.randint(2, 100)
    question = number
    correct_answer = prime(number)
    return question, correct_answer


if __name__ == '__main__':
    game_task()
