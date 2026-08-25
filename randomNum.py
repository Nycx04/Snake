import random
from PIL import Image
while True:

    print("Random Number Guesser!")
    print("Select a difficulty")

    choice = int(input("Difficulty: "))

    match choice: 
        case 1:
            print("Easy (1-20)")
        case 2:
            print("Medium (1-50)")
        case 3:
            print("Hard (1-100)")

    if choice == 1:
        num = (random.randint(1, 20))
    elif choice == 2:
        num = (random.randint(1, 50))
    elif choice == 3:
        num = (random.randint(1, 100))
    else :
        print("Enter a vaid difficulty")
        break


    guess = input("Guess: ")

    if guess == num:
        print("congrats! you got it right!")
    else:
        print("Wrong answer son")