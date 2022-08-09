import art
from game_data import data
import random

selected_Choices = []
is_answer_true = True
final_score = 0

def getChoice():
    choice = random.choice(data)
    if choice['name'] in selected_Choices:
        return getChoice()
    else:
        selected_Choices.append(choice['name'])
        return choice

def printChoice(choice, data):
    if choice == "A":
        print(f"Compare A: {data['name']}, {data['description']}, from {data['country']}")
    if choice == "B":
        print(f"Against B: {data['name']}, {data['description']}, from {data['country']}")

def compare():
    choiceA = getChoice()
    printChoice("A", choiceA)
    print(art.vs)
    choiceB = getChoice()
    printChoice("B", choiceB)
    userInput = input("Who has more followers? Type 'A' or 'B': ")
    if userInput.lower() == "a" and (choiceA['follower_count'] > choiceB['follower_count']):
        return True
    elif userInput.lower() == "b" and (choiceB['follower_count'] > choiceA['follower_count']):
        return True
    else:
        return False
        


print(art.logo)
while is_answer_true :
    if len(selected_Choices) != len(data):
        if not compare():
            print(f"Sorry! That's wrong. Final Score: {final_score}")
            is_answer_true = False
        else:
            final_score += 1
    else:
        print("Congratulations! You got all correct answers")
        is_answer_true = False