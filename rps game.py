import random
def game():
    guess = int(input("Enter 1 for rock, 2 for paper, 3 for scissors: "))
    comp = random.randint(1,3)
    if guess == comp:
        print("Tie")
    elif guess == 1 and comp == 2:
        print("Computer wins")
    elif guess == 1 and comp == 3:
        print("You win")
    elif guess == 2 and comp == 1:
        print("You win")
    elif guess == 2 and comp == 3:
        print("Computer wins")
    elif guess == 3 and comp == 1:
        print("Computer wins")
    elif guess == 3 and comp == 2:
        print("You win")
    else:
        print("Invalid input")
game()
print(200)
