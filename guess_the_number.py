# Program 2: Guess the number
# Generate 1 random number (0-100)
# Ask the user to guess the number
# Display “Greater than” if the inputed number is greater than the random number
# Display “Less than” if the inputed number is less than the random number
# Repeat asking the user until the random number has been guessed correctly.

from random import randint


rng = randint(0,100)
number = int(input('Guess the number: '))
while number != rng:
    if number > rng:
        print('Greater than')
        number = int(input('Guess the number: '))
    elif number < rng:
        print('Less than')
        number = int(input('Guess the number: '))
    else:
        break
if rng == number:
    print('You got it')
