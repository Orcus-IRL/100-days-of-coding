# Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).


start = True
while (start):
    from art import logo
    import os
    import random

    os.system('clear')
    print(logo)
    print("Welcome to the Number Guessing Game")
    print("I'm thinking of a number between 1 and 100.")

    number = random.randint(1, 100)
    print(number)
    difficulty = input("chose a difficulty. Type 'easy' or 'hard': ")


    def easy():
        attempts = 10
        while (attempts):
            print(f"you have {attempts} attempts remaining to guess the number.")
            guess = int(input("\nMake a guess: "))
            if (guess < number):
                print("Too low.")
                attempts -= 1
            elif (guess > number):
                print("Too high.")
                attempts -= 1
            else:
                print(f"You Got it! The answer was {number}.")
                break
        if (attempts == 0):
            print("You ran out of guesses, you lose!")


    def hard():
        attempts = 5
        while (attempts):
            print(f"you have {attempts} attempts remaining to guess the number.")
            guess = int(input("\nMake a guess: "))
            if (guess < number):
                print("Too low.")
                attempts -= 1
            elif (guess > number):
                print("Too high.")
                attempts -= 1
            else:
                print(f"You Got it! The answer was {number}.")
                break
        if (attempts == 0):
            print("You ran out of guesses, you lose!")


    if (difficulty.lower() == "easy"):
        easy()
    elif (difficulty.lower() == "hard"):
        hard()
    else:
        print("NOT A DIFFICULT LEVEL!!")

    game = input("You wanna play Y/N: ")
    if (game.lower() == "n"):
        start = False
    elif (game.lower() == 'y'):
        start = True
    else:
        print("Type y or n")
