import random
rock = '''
Rock
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
Paper
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
Scissors
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
game_vars = [rock, scissors, paper]
player_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors \n"))
print(game_vars[player_input])
computer_input = random.randint(0,2)
print("Computer chose: \n" + game_vars[computer_input])

if (player_input == computer_input):
    print("You both have chosen the same input. Try again!")
elif player_input == 0:
    if computer_input == 1:
        print("Player Wins. Rock wins against scissors.")
    else:
        print("Computer Wins. Paper wins against rock.")
elif player_input == 1:
    if computer_input == 2:
        print("Player Wins. Scissors win against paper.")
    else:
        print("Computer Wins. Rock wins against scissors.")
elif player_input == 2:
    if computer_input == 0:
        print("Player Wins. Rock wins against scissors.")
    else:
        print("Computer Wins. Scissors win against paper.")