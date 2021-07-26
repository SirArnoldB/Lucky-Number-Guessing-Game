# Lucky-Number-Guessing-Game

## Algorithm:
    - User Inputs the range: lower bound and upper bound.
    - Generate and Store a random integer (Lucky Number) within the range
    - Initialize a while loop.
    - Prompt the user for a guess
    - If the guess  > lucky number, output “Try Again! You guessed too high“
    - Else If the guess < lucky number, the user gets an output “Try Again! You guessed too small”
    - And if the user guessed in a minimum number of guesses, the user gets a “Congratulations! ” Output.
    - Else if the user didn’t guess the integer in the minimum number of guesses, he/she will get “Better Luck Next Time!” output.

## Overview:
    > Example Case: The User inputs a range from 1 to 100; And the Compiler randomly selected 43 as the Lucky Number. 
    - Start the game. 
    - If the user enters 50 as the first guess, the compiler shows “Try Again. You guessed too high”. 
    - That means the Lucky number (i.e 43) doesn’t fall in the range from 50 to 100. 
    - That’s the importance of guessing half of the range. 
    - Again, the user guesses half of 50 (Could you tell me why?), and enters 25 as the second guess. 
    - This time compiler will show, “Try Again. You guessed too small”.
    - That means the integers less than 25 (from 1 to 25) are useless to be guessed. 
    - Now the range for user guessing is shorter, i.e., from 25 to 50
    - Intelligently! The user guesses half of this range, and enters so that 37 as the third guess.  
    - This time again the compiler shows the output, “Try Again. You guessed too small”. 
    - For the user, the guessing range is getting smaller by each guess. 
    - Now, the guessing range for user is from 37 to 50, for which the user guesses 44 as the fourth guess. 
    - This time the compiler will show an output “Try Again. You guessed too high”. 
    - So, the new guessing range for users will be from 37 to 44, 
    - Again the user guesses the half of this range, that is, 41 as the fifth guess.  
    - This time the compiler shows the output, “Try Again. You guessed too small”. 
    - This Leaves the guess even smaller such that the range is from 42 to 44. 
    - And now the user guesses 42 as the sixth guess, which is wrong and shows output “Try Again. You guessed too small”. 
    - And finally, the User Guessed the right number which is 43 the seventh guess.

