def checkEven(number):
    if not number % 2:
        returnVal = 'even'
        if not number % 4:
            returnVal += ' and divisible by 4'
    else:
        returnVal = 'odd'
    return returnVal

def checkDivisibility(num, check):
    isDiv = ''
    if num % check:
        isDiv += ' not'
    return isDiv

if __name__ == "__main__":
    print("We're checking whether the number you're entering is odd or even")
    oddEvenNum = int(input('Please enter a number: '))
    print(f'{oddEvenNum} is {checkEven(oddEvenNum)}')

    print("Now we're checking whether one number is divisible by another")
    firstNum = int(input('Please enter the numerator: '))
    secondNum = int(input('Please enter the divisor: '))

    print(f'{firstNum} is{checkDivisibility(firstNum, secondNum)} divisible by {secondNum}')


