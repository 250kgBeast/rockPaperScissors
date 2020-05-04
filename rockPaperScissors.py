import random

options = ['rock', 'paper', 'scissors']
computer = random.choice(options)
player = input()
while player != "!exit":
    if player == computer:
        print(f"There is a draw ({player})")
    elif player == options[options.index(computer) - 2]:
        print(f"Well done. Computer chose {computer} and failed")
    elif player == options[options.index(computer) - 1]:
        print(f"Sorry, but computer chose {computer}")
    elif player not in options:
        print("Invalid input")
    player = input()
else:
    print("Bye!")
