# chapter 5 5.1 program on repetition
# Amanda M
# 2/7/2024

#sales_and_commission
keepGoing = "Y" 
def commiss():
    sales = float(input("Enter the amount of sales. "))
    COMMISSION_RATE = 0.10
    commission = (sales * COMMISSION_RATE)
    print("The commission is $", commission)




while keepGoing == "Y":
    keepGoing = input("Do you want to calculate another commission? Enter Y for yes, n for no. ")
    if keepGoing == "Y":
        commiss()
    else:
        print("Have a nice day!")        

    


