score = int(input("Enter your score: "))

def Grades(): 
    if score >= 90 : 
        print("your grade is A")
    elif score <= 89 and score >= 80 :
        print("Your grade is B")
    elif score <= 79 and score >= 70 :
        print("Your grade is C")
    elif score <= 69 and score >= 60 :
        print("You are a failure")





Grades()
