# Program 1: Lottery
# Create a program that ask 3 numbers (0-9) from the user.
# Generate 3 random winning numbers (0-9)
# Display “Winner” if all 3 input numbers matched the generated numbers
# Display ”You loss” if not
# Display ”Try again y/n” after each game
# If the user enter “y” the user will play again
# if “n” the program will exit

#imports the random module to use certain methods
import random

def lotteryDraw():
    randomGenNum = [] 
    for num in range(0,3):
        randomNum = random.randint(0, 9)
        while randomNum in randomGenNum: #each random number should be unique
            randomNum = random.randint(0, 9) #generates the random numbers
        randomGenNum.append(randomNum) #attach the random numbers to the list
    
    #asks for the user inputs
    guessCount = 0  
    userNumbers = []
    while guessCount < 3:
        num = int(input())
        userNumbers.append(num) #attach the user-entered numbers to the list
        guessCount += 1

    #checks if the user entered data are similar to the randomly generated ones
    matchedGuess = []
    for num in userNumbers:
        if num in randomGenNum: 
            matchedGuess.append(num)
    return matchedGuess, randomGenNum


def check(mGuess):
    #checks if the length of the list is three
    numMatch = int(len(mGuess))
    if numMatch < 3:
        return False
    else:
        return True

def askPlay():
    #asks the user if they want to play again
    print("Now that you've eliminated that unlucky draw,")
    retry = input('Do you want to play again? (y/n) ')
    print('--------------------------------------------')
    if retry[0] == 'y': 
        return True
    elif retry[0] == 'n':
        exit

def retry():
    #executes when the user wants to play again
    while askPlay() is True:
        print('Enter your 3 lucky numbers from 0 to 9')
        matchedGuess, randomGenNum = lotteryDraw()
        if check(matchedGuess) is True:
            print('You Won!')
            print('--------------------------------------------')
        else:
            print(f'You lose! Winning number is {randomGenNum[0]}, {randomGenNum[1]} and {randomGenNum[2]}.')
            print('--------------------------------------------')
            continue
    else:
        print('You got this next time!')
        exit

def main():
    print('--------------------------------------------')
    print('LOTTERY')
    print('Today is your lucky day!')
    print('Enter your 3 unique lucky numbers from 0 to 9: ')
    matchedGuess, randomGenNum = lotteryDraw()
    if check(matchedGuess) is True:
        print('You Won!')
        print('--------------------------------------------')
    else:
        print(f'You lose! Winning numbers are {randomGenNum[0]}, {randomGenNum[1]} and {randomGenNum[2]}.')
        print('--------------------------------------------')
        retry()

main()