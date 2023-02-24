import random

main_task = 'Answer "yes" if the number is even, otherwise answer "no".'

def even(question):
    if question % 2 == 0:
        return 'yes'
    else:
        return 'no'

def game_task():
    question = random.randint(1,100)
    correct_answer = str(even(question))
    return question, correct_answer