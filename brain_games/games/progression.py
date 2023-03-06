import random

MAIN_TASK = 'What number is missing in the progression?'

LOWER_LIMIT = 1

UPPER_LIMIT = 100

LOWER_STEP_LIMIT = 5

UPPER_STEP_LIMIT = 10


def game_task():
    first_number = random.randint(LOWER_LIMIT, UPPER_LIMIT)
    step = random.randint(LOWER_STEP_LIMIT, UPPER_STEP_LIMIT)
    range_numbers = [first_number * i for i in range(1, step + 1)]
    missed_number = random.randint(0, len(range_numbers) - 1)
    correct_answer = str(range_numbers[missed_number])
    range_numbers[missed_number] = '..'
    question = ' '.join(str(number) for number in range_numbers)
    return question, correct_answer
