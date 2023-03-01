import random

MAIN_TASK = 'What number is missing in the progression?'


def game_task():
    first_number = random.randint(1, 100)
    step = random.randint(5, 10)
    range_numbers = [first_number * i for i in range(1, step + 1)]
    missed_number = random.randint(0, len(range_numbers) - 1)
    correct_answer = str(range_numbers[missed_number])
    range_numbers[missed_number] = '..'
    question = ' '.join(str(number) for number in range_numbers)
    return question, correct_answer


if __name__ == '__main__':
    game_task()
