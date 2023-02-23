#!/usr/bin/env python3

from brain_games.scripts import brain_games
from brain_games import cli
import random
import prompt


def main():
    brain_games.main()
    user_name = brain_games.cli.user_name()

    print('Answer "yes" if the number is even, otherwise answer "no".')

    i = 0

    while i < 3:
        number = random.randint(1, 100)
        print('Question: ' + str(number))
        answer = prompt.string('Your answer: ')
    
        if answer == 'yes' and number % 2 == 0:
            print('Correct!')
            i = i + 1

        elif answer == 'no' and number % 2 != 0:
            print('Correct!')
            i = i + 1

        elif answer != 'yes' and number % 2 == 0:
            correct_answer = 'yes'
            print("'" + answer + "' is wrong answer ;(. Correct answer was '" + correct_answer + "'.")
            print("Let's try again, " + user_name + "!")
            break

        elif answer != 'no' and number % 2 != 0:
            correct_answer = 'no'
            print("'" + answer + "' is wrong answer ;(. Correct answer was '" + correct_answer + "'.")
            print("Let's try again, " + user_name + "!")
            break

    if i == 3:
        print('Congratulations, ' + user_name + '!')

if __name__ == '__main__':
    main()
