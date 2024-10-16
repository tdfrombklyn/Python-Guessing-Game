import random

def computerGuess(lowval, highval, randnum, count=0):
        if highval >= lowval:
                guess = lowval + (highval - lowval) // 2
                if guess == randnum:
                        return count
                
                # If "guess" is greater than the number, 
                # it must be found in the lower half of the set 
                # between the lower value and the guess. 
                elif guess > randnum:
                        count = count + 1 
                        return computerGuess(lowval, guess - 1, randnum, count)
                
                # The number must be in the upper half of number
                # between the guess and the upper value.
                else:
                        count = count + 1
                        return computerGuess(guess + 1, highval, randnum, count)
        else:
                # Number not found 
                return -1
# End of function

# Generate a random number between 1 and 100 
randnum = random.randint(1,101)

count = 0
guess = -99

# Get the user's guess

while (guess != randnum):
        guess = (int) (input("Enter your guess between 1 and 100: "))
        if guess < randnum:
                print("Higher!")
        elif guess > randnum:
                print("Lower!")
        else:
                print("You guessed it!")
                break
        count = count + 1
# End of while loop

print("You took " + str(count) + " steps to guess the number!")
print("Computer took " + str(computerGuess(0,100, randnum)) + " steps!")