# Calories Burned
# Amanda M

keepGoing = "y"

def main():
    minutes1 = int(input("Enter quantity of minutes: "))
    CALORIES = 3.9
    if minutes1 > 10 and minutes1 < 30:
        burnED = CALORIES * minutes1
        print(f"You have burned {burnED} calories in {minutes1} minutes.") 
    if minutes1 > 31:
         print("Variable not within limit. Please input minutes.")
         quit()

while keepGoing == "y":
    keepGoing = input("Do you want to record more minutes? Enter y for yes, n for no. ")
    if keepGoing == "y":
        main()
    elif keepGoing == "n":
        project = input("Would you like to see the projected calories burned in 10 more minutes? Enter Y for yes, N for no.")
        if project == "Y":
            CALORIES = 3.9
            minutes1 = int(input("Enter previous quantity of minutes: "))
            minutes = minutes1 + 10
            burnED = CALORIES * minutes
            print("Your projected calories burned are", burnED)
        else:
            print("Have a nice day!")
            quit()
