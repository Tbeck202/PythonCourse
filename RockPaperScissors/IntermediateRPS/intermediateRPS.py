import random
computer_num = random.randint(1, 3)
computer = None

if computer_num == 1:
    computer = "rock"
elif computer_num == 2:
    computer = "paper"
else:
    computer = "scissors"

print("Welcome to Rock, Paper, Scissors! \n\nMake your move, bitch!")
player = input().lower()

if player:
    if player == computer:
        print("It's a tie!")
    elif player == "rock" or player == "paper" or player == "scissors":
        if (player == "rock" and computer == "scissors") or (player == "scissors" and computer == "paper") or (player == "paper" and computer == "rock"):
            print(
                f"You threw {player} and the computer threw {computer}. \nYou win!")
        else:
            print(
                f"You threw {player} and the computer threw {computer}. \nYou lose!")
    else:
        print("You ruined the game, ya ding dong!")
else:
    print("You didn't enter anything!")
