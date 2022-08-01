# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

combined_string = name1 + name2

t = combined_string.lower().count('t') 
r = combined_string.lower().count('r') 
u = combined_string.lower().count('u') 
e = combined_string.lower().count('e') 

l = combined_string.lower().count('l') 
o = combined_string.lower().count('o') 
v = combined_string.lower().count('v') 
e = combined_string.lower().count('e') 

score = (t+r+u+e)*10+(l+o+v+e)

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score >=40 and score <=50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")