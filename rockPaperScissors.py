import random


x = input()
random_integer = random.randint(1, 3)
computer_choice = 0
if random_integer == 1:
    computer_choice = "rock"
elif random_integer == 2:
    computer_choice = "scissors"
else:
    computer_choice = "paper"

if x == computer_choice:
    print(f"There is a draw ({x})")
elif (x == "scissors" and computer_choice == "paper")\
        or (x == "paper" and computer_choice == "rock")\
        or (x == "rock" and computer_choice == "scissors"):
    print(f"Well done. Computer chose {computer_choice} and failed")
else:
    print(f"Sorry, but computer chose {computer_choice}")
