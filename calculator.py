from os import system, name

def clear():
    # Windows
    if name == 'nt':
        _ = system('cls')
    # Mac/Linux
    else:
        _ = system('clear')

def addition(num1, num2):
    return num1 + num2

def subtraction(num1, num2):
    return num1 - num2

def multiplication(num1, num2):
    return num1 * num2

def division(num1, num2):
    return num1 / num2

if __name__ == "__main__":
    again = 'y'
    operators = ['+','-','*','/']

    while again == 'y':
        clear()

        op = ''
        num1 = int(input('Please enter the first number: '))
        while op not in set(operators):
            op = input('Please choose your operator (+, -, *, /): ')
        num2 = int(input('Please enter the second number: '))

        if op == '+':
            print('Result:', addition(num1, num2))
        if op == '-':
            print('Result:', subtraction(num1, num2))
        if op == '*':
            print('Result:', multiplication(num1, num2))
        if op == '/':
            print('Result:', division(num1, num2))
        
        again = input('Perform another calculation? (y/n) ')
    
    print('Thanks! Bye!')