import math
import tkinter as tk


def bin2dec():
    loop = 'y'
    while loop == 'y':
        decNum = 0

        # Infinite loop to check if input is a binary string
        while True:
            binInput = input(
                "Please enter a binary number to convert to decimal: ")
            if set(binInput) == {'0', '1'} or set(binInput) == {'0'} or set(binInput) == {'1'}:
                break    # break out of loop if binInput is a binary string
            else:
                print(binInput, "is not a binary number")

        binList = list(binInput)                        # Cast input as a list
        for n in range(len(binList)):
            # return elements from the end of the list one-by-one, multiply by the nth power of 2 and add to result
            decNum += int(binList.pop()) * pow(2, n)

        print(binInput, "in decimal is:", decNum)

        loop = ''
        while loop not in {'y', 'n'}:
            loop = input("Do another? (y/n): ")
    return


def dec2bin():
    loop = 'y'
    while loop == 'y':
        binNum = []

        while True:                                             # Infinite loop to check input
            decInput = input(
                "Please enter a decimal number to convert to binary: ")
            try:
                decWorking = int(decInput)
                if decWorking > 0:
                    break                        # break out of loop if decInput is a positive number
                else:
                    print("Please enter a positive number")
            except ValueError:
                print("That's not a number!")

        if math.log2(decWorking) == int(math.log2(decWorking)):  # Handle perfect powers of 2
            binNum.append(1)
            binNum.extend([0] * int(math.log2(decWorking)))
        else:                                                   # Work with everything else
            while decWorking >= 1:
                binNum.insert(0, decWorking % 2)
                decWorking //= 2

        print(decInput, "in binary is:", ''.join(map(str, binNum)))

        loop = ''
        while loop not in {'y', 'n'}:
            loop = input("Do another? (y/n): ")
    return


def main():
    carryOn = 'y'

    print("")
    while carryOn == 'y':
        choice = 0
        print("Would you like to convert:\n1. FROM binary TO decimal, or\n2. FROM decimal TO binary?")
        while choice not in {'1','2'}:
            choice = input("Choose a number 1/2: ")
            if choice == '1':
                bin2dec()
            elif choice == '2':
                dec2bin()
        carryOn = ''
        while carryOn not in {'y','n'}:
            carryOn = input("Would you like to carry on? (y/n): ")


main()
