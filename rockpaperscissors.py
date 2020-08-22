from random import randint
choices = ["rock", "paper", "scissors"]
computer = choices[randint(0, 2)]
print("Welcome to the Rock,Paper,Scissors Game\n")
player = input("Your choice: ").lower()
print("Computer's Choice: "+ computer)

if player == computer:
    print("Draw")
elif player == "rock" and computer == "paper":
    print("Computer has won")
elif player == "rock" and computer == "scissors":
    print("Player has won")
elif player == "paper" and computer == "rock":
    print("Player has won")
elif player == "paper" and computer == "scissors":
    print("Computer has won")
elif player == "scissors" and computer == "rock":
    print("Computer has won")
elif player == "scissors" and computer == "paper":
    print("Player has won")
elif player == "end":
        StopIteration
