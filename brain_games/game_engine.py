import prompt
from brain_games import cli

def game_step(question, correct_answer):
    print('Question: ' + str(question))
    answer = prompt.string('Your answer: ')
    if correct_answer == answer:
        print('Correct!')
        return True
    else:
        print("'" + answer + "' is wrong answer ;(. Correct answer was '" + correct_answer + "'.")
        return False

def game_process(game):
    user_name = cli.welcome_user()
    print(game.main_task)
    count = 0
    while count < 3:
        question, correct_answer = game.game_task()
        if game_step(question, correct_answer):
            count += 1
        else:
            print("Let's try again, " + user_name + "!")
            break

    if count == 3:
        print('Congratulations, ' + user_name + '!')
