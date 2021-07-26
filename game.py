from random import randint
import math

def genie(lowerBound, upperBound):
    '''
    :type lowerBound int
    :type uperBound int
    :rtype int
    '''
    # generate a random number between lowerBound and upperBound
    luckyNumber = randint(lowerBound, upperBound)
    return luckyNumber

# get the range
lowerBound = int(input("Enter Lower bound: "))
upperBound = int(input("Enter Upper bound: "))

# get the lucky number 
luckyNumber = genie(lowerBound, upperBound)

# get the number of guesses
numGuesses = round(math.log(upperBound - lowerBound + 1, 2))

print("\n\tYou only have {0} chances to guess the integer!\n".format(numGuesses))

# Initializing the number of guesses.
countGuesses = 0

# game loop
while countGuesses < numGuesses:
    countGuesses += 1

    # taking guessing number as input
    guess = int(input("Guess a number: "))

    # Condition testing
    if guess == luckyNumber:
        print("Congratulations you guessed the luck number in {0} guesses!".format(countGuesses))
        # break the loop - guess found
        break
    elif guess < luckyNumber:
        print("You guessed too small!")
    elif guess > luckyNumber:
        print("You Guessed too high!")
    print("\n Guesses remaining: {0} \n".format(numGuesses - countGuesses))

# If number of guesses is more than required guesses:
if countGuesses >= numGuesses:
    print("\nThe Lucky Number Number is %d" % luckyNumber)
    print("\nBetter Luck Next time!")

