import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_number:
            print(f'Sory the number is higher')
        elif guess > random_number:
            print(f"Sorry the number is lower")
    print(f"Correct!!! yes the number is {random_number}.")

guess(10)


def guessAI(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low #low = high
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)?? ').lower()
        if feedback == 'h':
            high  = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print(f'yay! The computer guessed your number, {guess}, correctly')

guessAI(10)