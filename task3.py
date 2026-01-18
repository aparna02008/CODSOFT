import random
choices = ["rock", "paper", "scissor"]
user = input("Enter rock, paper or scissor: ").lower()
com = random.choice(choices)
print("User choice:", user)
print("Computer choice:", com)
if user == com:
    print("It's a tie")
elif (user == "rock" and com == "scissor") or \
     (user == "scissor" and com == "paper") or \
     (user == "paper" and com == "rock"):
    print("User wins")
elif user in choices:
    print("Computer wins")
else:
    print("Invalid input")
