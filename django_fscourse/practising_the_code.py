
import random

#Get Guess
def chuta():
    '''
    Asks for the number guess and transforms the string to a list.
    '''
    return list(input("Qual vai ser?"))

#Generate Computer Code 123
def generate_code():
    digits = [str(num) for num in range(10)]

    #Shuffle the digits
    random.shuffle(digits)
    #then grab the first three
    return digits[:3]

#Generate the Clues
def generate_clues(code, user_guess):

    if user_guess == code:
        return "CODE CRACKED!"

    clues = []

    for ind, num in enumerate(user_guess):
        if num == code[ind]:
            clues.append('match')
        elif num in code:
            clues.append("Close")

    if clues == []:
        return ["Nope"]
    else:
        return clues

#Run Game Logic
print("Welcome Code Breaker!")

secret_code = generate_code()

clue_report = []

while clue_report != "Code Cracked!":
    guess = chuta()

    clue_report = generate_clues(guess, secret_code)
    print("here is the result of ur guess: ")
    for clue in clue_report:
        print(clue)
