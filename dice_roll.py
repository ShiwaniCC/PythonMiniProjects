import random

count = 0
i = 1
while True:
    count = count + 1
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

    print(f"Number of times rolled so far: {count}")