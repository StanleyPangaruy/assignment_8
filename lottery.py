# Program 1: Lottery
# Create a program that ask 3 numbers (0-9) from the user.
# Generate 3 random winning numbers (0-9)
# Display “Winner” if all 3 input numbers matched the generated numbers
# Display ”You loss” if not
# Display ”Try again y/n” after each game
# If the user enter “y” the user will play again
# if “n” the program will exit

import random

def lottery():
    randomGenNum = []
    while len(randomGenNum) < 3:
        randomNum = random.randint(0, 9)
        randomGenNum.append(randomNum)
    
    guessCount = 0
    userNumbers = []
    print('this is a game, guess 3 numbers between 0-9')
    while guessCount < 3:
        num = int(input('enter a number :'))
        userNumbers.append(num)
        guessCount += 1

    matchedGuess = []
    for num in userNumbers:
        if num in randomGenNum:
            matchedGuess.append(num)
    return matchedGuess


def check(correct_guess):
    numMatch = int(len(correct_guess))
    if numMatch < 3:
        return False
    else:
        return True

def rePlay():
    retry = input('Try again? y/n: ')
    if retry == 'y':
        return True
    else:
        exit

def retry():
    while rePlay() is True:
        matchedGuess = lottery()
        if check(matchedGuess) is True:
            print('Winner')
        else:
            print('you loss')
            continue
    else:
        exit

def main():
    matchedGuess = lottery()
    if check(matchedGuess) is True:
        print('Winner')
    else:
        print('you loss')
        rePlay()

main()



