#get guess
import random


def get_guess():
    return list( input ("what is your guess?"))
#generate computer code 123
def generate_code():
    digit = [str(num)for num in range(10)]

    #shuffle the digit
    random.shuffle(digit)
    #then grab the first three
    return digit[:3]

#generate the clues

def generate_clues(code,user_guess):
    if user_guess==code:
        return "code cracked!"

    clues = []

    ind= 0
    for ind, num in enumerate(user_guess):
        if num == code[ind]:
            clues.append("match")
        elif num in code :
            clues.append("close")
    
    if clues == []:
        return ["Nope"]
    else:
        return clues     
    while clue_report != "code Cracked!":

        guess = get_guess()

        clue_report = generate_clues(guess,secret_code)
        print("here is the reuslt of your guess: ")
        for clue in clue_report:
            print(clue)


# run game logic
print ("welcome code Breaker!")

secret_code = generate_code()

clueReport = []


# un game logics
x = get_guess()
print(type(x[0]))