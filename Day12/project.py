
import random
from art import logo
choice_attempts = {"easy": 10, "hard": 5}
chosen_number =  random.randint(1,100)

def guess_number(chosen_number, attempt):
    print (f"You have {attempt} remaining to guess the number.")
    new_choice = int(input("Make a guess: "))
    if new_choice == chosen_number:
        print(f"You got it! The answer is {new_choice}")
        return True
    elif new_choice > chosen_number:
        print("Too High")
        print("Guess Again")
        return False
    else:
        print("Too Low")
        print("Guess Again")
        return False
    

play_continue = "y"
while play_continue.lower() == "y":
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")
    choice = input("Choose a difficulty. Type 'easy' or 'hard': ")
    attempts = choice_attempts[choice]

    while attempts > 0:
        if guess_number(chosen_number, attempts):
            attempts = 0
        else:
            attempts -=1
    
    play_continue = input("Do you want to continue playing the game again. Type 'y' or 'n': ")