# Fibonacci generator

print('Welcome to the Fibonacci sequence generator!')
print('')

loop = 'y'

while loop == 'y':
    fib = [0,1]
    limit = int(input('Please enter how many terms of the Fibonnaci sequence you would like to generate: '))
    f = 2
    while f < limit:
        fib.append(fib[f-1] + fib[f-2])
        f += 1
    print(fib)
    while True:
        loop = input('Would you like to go again? (y/n) ')
        if loop == 'y' or loop == 'n': break


print('Thanks, come again!')
