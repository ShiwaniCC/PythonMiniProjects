import random

while True:
    c = input("Do you want to Roll(Y/N)? ").upper()

    if c == "Y":
        num1 = random.randint(1, 6)
        num2 = random.randint(1, 6)
        print(f'({num1} , {num2})')
    elif c == "N":
        print("Thanks for playing!!")
        break
    else:
        print("Invalid Input! Please enter 'Y' or 'N'.")
