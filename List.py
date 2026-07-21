List = []
while True:
 print("=====To Do List=====")

 print("1. Add Task")
 print("2. Remove Task")
 print("3. View Task")
 print("4. Exit")


 choice = int(input("Choose: "))

 if choice == 1 : 
  add = input("Enter the task to add: ")
  List.append(add)
 elif choice == 2 :
  remove = input("Which task to delete?: ")
  List.remove(remove)
 elif choice == 3 :
  print(f"{List}")
 elif choice == 4 :
  break
