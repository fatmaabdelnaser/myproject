#****************************************************************************************************************
# File: CS112_A1_T2_3_20230281
# Purpose:A subtract a square game in python.
#        The players subtract a non-zero square number from a specific number of coins(picked by users or randomly).
#        The player who removes the last coin wins
# Author: Fatma Abd Elnaser Abd Elasis Marei
# ID: 20230281
#****************************************************************************************************************

#Function if the user select random pick
def random():
    #import a random number of coins and display it
    import random
    random_coins_number = int(random.randint(10, 1000))
    print(f"number of coins = {random_coins_number}")
    #assign empty list to fill it
    square_list = []
    for i in range(1, (int(random_coins_number**0.5) + 1)):
        square_list.append(int(i ** 2))
    while True:
        while True:
            #set number and validate the input
            Num = input(f"player 1 please enter squard number between 1 & {random_coins_number} : ")
            if not all(char in "1234567890" for char in str(Num)):
                print(f"Invalid number , please enter a squard number between 1 & {random_coins_number} : ")
            else:
                Num = int(Num)
                if Num in square_list and Num != 0:
                    if Num > random_coins_number:
                        print(f"Invalid number , please enter a squard number between 1 & {random_coins_number} : ")
                    else:
                        if random_coins_number == Num:
                            print("player 1 is the winner ")
                            exit()
                        else:
                            random_coins_number -= Num
                            print(f"now we have {random_coins_number}")
                            break
                else:
                    print(f"invalid number , please enter a squard number between 1 & {random_coins_number} : ")
                    continue

        while True:
            # set number and  validate the input
            Num = input(f"player 2 please enter squard number between 1 & {random_coins_number} : ")
            if not all(char in "1234567890" for char in str(Num)):
                print(f"Invalid number , please enter a squard number between 1 & {random_coins_number} : ")
            else:
                Num = int(Num)
                if Num in square_list and Num != 0:
                    if Num > random_coins_number:
                        print(f"Invalid number , please enter a squard number between 1 & {random_coins_number} : ")
                    else:
                        if random_coins_number == Num:
                            print("player 2 is the winner ")
                            exit()
                        else:
                            random_coins_number -= Num
                            print(f"now we have {random_coins_number}")
                            break
                else:
                    print(f"invalid number , please enter a squard number between 1 & {random_coins_number} : ")
                    continue
#Function if the user select a constant pick
def constant():
    #set coins_number and (validate and display the input)
    while True:
        coins_number = input("Please enter the coins numbers you want : ")
        if not all(char in "1234567890" for char in str(coins_number)):
            print(f"Invalid number , please enter a valid number of coins")
        else:
            coins_number = int(coins_number)
            break
    print(f"number of coins = {coins_number}")
    # assign empty list to fill it
    square_list = []
    for i in range(1, (int(coins_number**0.5)+1)):
        square_list.append(int(i ** 2))
    while True:
        while True:
            # set number and  validate the input
            Num = input(f"player 1 please enter sruard number between 1 & {coins_number} : ")
            if not all(char in "1234567890" for char in str(Num)):
                print(f"Invalid number , please enter a squard number between 1 & {coins_number} : ")
            else:
                Num = int(Num)
                if Num in square_list and Num != 0:
                    if Num > coins_number:
                        print(f"Invalid number , please enter a squard number between 1 & {coins_number} : ")
                    else:
                        if coins_number == Num:
                            print("player 1 is the winner ")
                            exit()
                        else:
                            coins_number -= Num
                            print(f"now we have {coins_number}")
                            break
                else:
                    print(f"invalid number , please enter a squard number between 1 & {coins_number} : ")
                    continue
        while True:
            # set number and  validate the input
            Num = input(f"player 2 please enter sruard number between 1 & {coins_number} : ")
            if not all(char in "1234567890" for char in str(Num)):
                print(f"Invalid number , please enter a squard number between 1 & {coins_number} : ")
            else:
                Num = int(Num)
                if Num in square_list and Num != 0:
                    if Num > coins_number:
                        print(f"Invalid number , please enter a squard number between 1 & {coins_number} : ")
                    else:
                        if coins_number == Num:
                            print("player 2 is the winner ")
                            exit()
                        else:
                            coins_number -= Num
                            print(f"now we have {coins_number}")
                            break
                else:
                    print(f"invalid number , please enter a squard number between 1 & {coins_number} : ")
                    continue
#Welcome message and the menu of the choices
def choose():
    print("* Welcome to our program *")
    print("choose the type of coins numbers you want")
    print("A)Random coins number")
    print("B)Constant coins number")
    print()
#Game playing
while True:
    choose()
    s = str(input("enter your choose : "))
    if s == "A":
        random()
        break
    elif s == "B":
        constant()
        break
    else:
        print("invalid choice , please enter a valid choice")
        print()
