import random
import operator

MAIN_TASK = 'What is the result of the expression?'


def game_task():
    number_one = random.randint(1, 100)
    number_two = random.randint(1, 100)
    operators = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul
    }
    operator_symbol = random.choice(list(operators))
    question = f"{number_one} {operator_symbol} {number_two}"
    correct_answer = str(operators.get(operator_symbol)(number_one, number_two))
    return question, correct_answer
