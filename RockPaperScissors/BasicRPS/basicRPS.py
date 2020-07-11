print("Welcome to Rock, Paper, Scissors! \n\nThrow something, Player One!")
player_one = input()
if not player_one:
    print("You ruined the game!")
else:
    print("Now you throw something, Player Two!")
player_two = input()
if player_two:
    if (player_one == "rock" and player_two == "scissors") or (player_one == "scissors" and player_two == "paper") or (player_one == "paper" and player_two == "rock"):
        print("Player one wins!")
    elif player_one == player_two:
        print("Y'all tied!")
    else:
        print("Player two wins!")
else:
    print("You ruined the game!")
