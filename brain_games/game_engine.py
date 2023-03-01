import prompt
from brain_games import cli


ANSWERS_FOR_WIN = 3


def game_step(question, correct_answer):
    print('Question: ' + str(question))
    answer = prompt.string('Your answer: ')
    if correct_answer == answer:
        print('Correct!')
        return True
    else:
        print(f"{answer} is wrong answer ;(. \
        Correct answer was {correct_answer}")
        return False


def game_process(game):
    user_name = cli.welcome_user()
    print(game.MAIN_TASK)
    count = 0
    while count < ANSWERS_FOR_WIN:
        question, correct_answer = game.game_task()
        if game_step(question, correct_answer):
            count += 1
        else:
            print("Let's try again, " + user_name + "!")
            break

    if count == ANSWERS_FOR_WIN:
        print('Congratulations, ' + user_name + '!')
