import random

rounds = 0
print("Welcome to Rock, Paper, Scissors!")
play_to = int(input("Let's play best out of: (enter and odd number) "))
check = play_to / 2
player_score = 0
comp_score = 0
while True:
    comp_throw_num = random.randint(1, 3)
    if (player_score or comp_score) < check:
        if comp_throw_num == 1:
            comp_throw = "rock"
        elif comp_throw_num == 2:
            comp_throw = "paper"
        else:
            comp_throw = "scissors"
        print(f"Player: {player_score} - Computer: {comp_score}")
        print('(Type "q" at any time to quit)')
        player_throw = input("What's your throw??")

        if player_throw == comp_throw:
            print(f"You both threw {player_throw}, try again!")
        elif player_throw == "rock" and comp_throw == "scissors":
            player_score += 1
            print("Rock beats scissors! Go again!")
        elif player_throw == "paper" and comp_throw == "rock":
            player_score += 1
            print("Paper beats rock! Go again!")
        elif player_throw == "scissors" and comp_throw == "paper":
            player_score += 1
            print("Scissors beats paper! Go again!")
        elif player_throw == "q":
            print("K bye!")
            break
        else:
            print(
                f"You threw {player_throw} but the computer threw {comp_throw}\nTry again!")
            comp_score += 1
    elif comp_score > check:
        print("You lose!")
        play_again = input("Wanna play again? (y/n)")
        if play_again == "n":
            print("K bye!")
            break
        elif play_again == "y":
            print("sweet, let's do this!")
            comp_score = 0
            player_score = 0
    else:
        print("You win!")
        play_again = input("Wanna play again? (y/n)")
        if play_again == "n":
            print("K bye!")
            break
        elif play_again == "y":
            print("sweet, let's do this!")
            comp_score = 0
            player_score = 0
