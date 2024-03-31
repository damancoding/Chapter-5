# Amanda M
# 3/29/2024
# Algorithm 4: Design a loop that asks the user to enter a number. The loop should iterate 10 times and keep a running total of the numbers entered.
counter = 1
num = int(input("Enter a number: "))
def label():
    counter = 1
    for i in range(10):
        print(f"This is your number, {num}, printed {counter} times.")
        counter = counter + 1

label()
