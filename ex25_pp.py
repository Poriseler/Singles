from random import randint

def computer_guess(low_range, high_range):
    playing = 1
    guesses = 0
    while playing:
        guess = randint(low_range, high_range)
        print("{} - is this your number?".format(guess))
        answer = input("yes/no? ")
        if answer == "yes":
            print("congratulation, it took me {} guesses".format(guesses))
            playing = 0
        else:
            guesses +=1
            new_range = int(input("was it too high(1) or too low(2)? "))
            if new_range == 1:
                high_range = guess - 1
            else:
                low_range = guess + 1


print("Thought about int from 1 to 100")
low_range = 1
high_range = 100
computer_guess(low_range, high_range)
