import prompt

def welcome_user():
    global name
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + "!")
    
def user_name():
    return name
