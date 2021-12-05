# Program 1: Lottery
# Create a program that ask 3 numbers (0-9) from the user.
# Generate 3 random winning numbers (0-9)
# Display “Winner” if all 3 input numbers matched the generated numbers
# Display ”You loss” if not
# Display ”Try again y/n” after each game
# If the user enter “y” the user will play again
# if “n” the program will exit

import random

def userGuess():
    generated = []
    while len(generated) < 3:
        random_num = random.randint(0, 9)
        generated.append(random_num)
    
    guess_times = 0
    guessed_numbers = []
    print('this is a game, guess 3 numbers between 0-9')
    while guess_times < 3:
        num = int(input('enter a number :'))
        guessed_numbers.append(num)
        guess_times += 1

    correct_guess = []
    for num in guessed_numbers:
        if num in generated:
            correct_guess.append(num)
    return correct_guess


def check(correct_guess):
    num_correct = int(len(correct_guess))
    if num_correct < 3:
        return False
    else:
        return True

def cont():
    yahno = input('Try again? y/n: ')
    if yahno == 'y':
        return True
    else:
        exit

def retry():
    while cont() is True:
        cg = userGuess()
        if check(cg) is True:
            print('Winner')
        else:
            print('you loss')
            continue
    else:
        exit

def main():
    cg = userGuess()
    if check(cg) is True:
        print('Winner')
    else:
        print('you loss')
        retry()

main()



