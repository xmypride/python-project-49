import random

MAIN_TASK = 'Answer "yes" if the number is even, otherwise answer "no".'

LOWER_LIMIT = 1

UPPER_LIMIT = 100


def even(question):
    if question % 2 == 0:
        return True
    else:
        return False


def game_task():
    question = random.randint(LOWER_LIMIT, UPPER_LIMIT)
    correct_answer = even(question)
    return (question, 'yes') if correct_answer else (question, 'no')
