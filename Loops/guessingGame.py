import random
num = random.randint(1, 10)
guess = int(input("Pick a number from 1 to 10: "))
while True:
    if guess == num:
        keep_playing = input("That's it! Wanna play again? (y/n): ")
        if keep_playing == "n":
            print("K bye!")
            break
        else:
            num = random.randint(1, 10)
            guess = int(input("Pick a number between 1 and 10: "))
    if guess > num:
        guess = int(input("Too high! Try again: "))
    else:
        guess = int(input("Too low! Try again: "))
