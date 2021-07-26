from random import choice, randint
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

def stop():
    choice = str(input("Do you want to play again? (Y/N): "))
    if choice.lower() == "y":
        # start the game
        play()
    elif choice.lower() == 'n':
        # end the game
        exit()
    else:
        print("Please Enter 'Y' to play a new game or 'N' to stop!")
        stop()

def play():
    def getRange():
        # get the range
        lowerBound = int(input("\n\tEnter Lower bound: "))
        upperBound = int(input("\n\tEnter Upper bound: "))

        return lowerBound, upperBound

    lowerBound, upperBound = getRange()
    while upperBound < lowerBound or upperBound == lowerBound:
        print("Upper Bound must be greater than lower Bound!\n")
        lowerBound, upperBound = getRange()

    # get the lucky number 
    luckyNumber = genie(lowerBound, upperBound)

    # get the number of guesses
    numGuesses = round(math.log(upperBound - lowerBound + 1, 2))

    print("\n\tYou only have {0} chances to guess the integer!\n".format(numGuesses))

    # Initializing the number of guesses.
    countGuesses = 0

    flag = True

    # game loop
    while flag:
        countGuesses += 1

        # taking guessing number as input
        guess = int(input("Guess a number: "))

        # Condition testing
        if countGuesses >= numGuesses:
            print("\n\tGuesses remaining: {0} \n".format(numGuesses - countGuesses))
            print("\n\tThe Lucky Number Number is %d \n" % luckyNumber)
            print("\n\tBetter Luck Next time!\n")
            flag = False
        if guess == luckyNumber:
            print("\nCongratulations you guessed the lucky number, {0}, in {1} guesse(s)!\n".format(luckyNumber, countGuesses))
            # break the loop - guess found
            break
        elif guess < luckyNumber:
            print("\tYou guessed too small!\n")
            print("\n\tGuesses remaining: {0} \n".format(numGuesses - countGuesses))
        elif guess > luckyNumber:
            print("\tYou Guessed too high!\n")
            print("\n\tGuesses remaining: {0} \n".format(numGuesses - countGuesses))

    stop()

if __name__ == "__main__":
    play()

