import random

print("\033[1m--- Play Rock, Paper and Scissors! ---\033[0m")

while True:
    my_choice = int(input("What do you choose? Type \033[1m0\033[0m for Rock, \033[1m1\033[0m for Paper or \033[1m2\033[0m for "
                      "Scissors. "))
    if my_choice >= 0 and my_choice <= 2:
        break
    else:
        print("Chose between 0 and 2!")
        continue

computer_choice = random.randint(0, 2)

list = ["Rock", "Paper", "Scissors"]

print(f"You choose {list[my_choice]}")
print(f"Computer choose {list[computer_choice]}")

if my_choice == 0 and computer_choice == 0:
    print("A tie!")
elif my_choice == 1 and computer_choice == 1:
    print("A tie!")
elif my_choice == 2 and computer_choice == 2:
    print("A tie!")
elif my_choice == 0 and computer_choice == 1:
    print("You lose!")
elif my_choice == 0 and computer_choice == 2:
    print("You win!")
elif my_choice == 1 and computer_choice == 0:
    print("You win!")
elif my_choice == 1 and computer_choice == 2:
    print("You lose!")
elif my_choice == 2 and computer_choice == 0:
    print("You lose!")
else:
    print("You win!")