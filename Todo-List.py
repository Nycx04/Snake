
while True:
    print(" \n \nTo-Do List")

    list = [
    "1. Play warframe",
    "2. Play arknights",
    "3. Eat",
    "4. Go to the gym",
    "5. Study"
]

    print("Menu\n 1. Add task\n 2. View Task\n 3. Remove task\n 4. Exit ")
    option = int(input(" \n"))

    if option == 1:
        newtask = input("Enter new task: ")
        list.append(newtask)
    elif option == 2:
        print("\n" .join (list))
    elif option == 3:
        removetask = input("which task to remove?: ")
        list.remove(removetask)
    else:
        break