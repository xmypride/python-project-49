import prompt

def user_name():
    global name
    name = prompt.string('May I have your name?')
    return name

def welcome_user():
    user_name()
    print('Hello, ' + name + "!")
