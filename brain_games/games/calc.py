import random
import operator

MAIN_TASK = 'What is the result of the expression?'

# The minimum possible number in the expression
LOWER_LIMIT = 1

# The maximum possible number in the expression
UPPER_LIMIT = 100


def game_task():
    number_one = random.randint(LOWER_LIMIT, UPPER_LIMIT)
    number_two = random.randint(LOWER_LIMIT, UPPER_LIMIT)
    operators = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul
    }
    operator_symbol = random.choice(list(operators))
    question = f"{number_one} {operator_symbol} {number_two}"
    correct_answer = str(operators.get(operator_symbol)(number_one, number_two))
    return question, correct_answer
