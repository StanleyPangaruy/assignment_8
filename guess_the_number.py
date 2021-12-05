# Program 2: Guess the number
# Generate 1 random number (0-100)
# Ask the user to guess the number
# Display “Greater than” if the inputed number is greater than the random number
# Display “Less than” if the inputed number is less than the random number
# Repeat asking the user until the random number has been guessed correctly.

from random import randint

def guesser():

    randomNum = randint(0,100) #randomnly generates the number to be guessed from 0 to 100
    guessNum = int(input()) #asks for the user input to guess to the number
    guessCount = 1 #current guesscount to account for the correct guess

    #loops only when user's guess is not equal the randomly generated number
    while guessNum != randomNum: 
        if guessNum > randomNum: #guess is higher than the random number
            print('Your guess is too high. Go lower!')
            print('Take another guess.')
            guessNum = int(input())
            guessCount += 1 #adds to the guess count for every guess

        elif guessNum < randomNum: #guess is lower than the random number
            print('Your guess is too low. Go higher!')
            print('Guess again!')
            guessNum = int(input())
            guessCount += 1 #adds to the guess count for every guess

        else:
            break #exits the loop if none satisfies

    #displays your number of guesses after guessing the correct number.
    if randomNum == guessNum:

        print(f"""---------------------------------------------------
Nice! You figured out my number in only {guessCount} guesses.
---------------------------------------------------""")

def main():

    print("""--------------------------------
I have a number from 0 to 100.
What is my number?
--------------------------------""")

    guesser()

main()

