import random

MAIN_TASK = 'Answer "yes" if the number is even, otherwise answer "no".'

# The minimum possible number in the expression
LOWER_LIMIT = 1

# The maximum possible number in the expression
UPPER_LIMIT = 100


def even(question):
    if question % 2 == 0:
        return True
    else:
        return False


def game_task():
    question = random.randint(LOWER_LIMIT, UPPER_LIMIT)
    correct_answer = even(question)
    if correct_answer:
        return question, 'yes'
    else:
        return question, 'no'
