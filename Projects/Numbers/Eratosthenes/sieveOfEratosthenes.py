import math

def SieveOfEratosthenes(n):
    prime = [True for i in range(n + 1)]

    p = 2

    for i in range(p): prime[i] = False

    while (p * p <= n):
        if (prime[p] == True):
            #print('p =', p, end=': ')
            for i in range(p * 2, n + 1, p):
                #print(i, end=' ')
                prime[i] = False
        p += 1
        #print('')

    for p in range(n + 1):
        if prime[p]: print(p, end=', ')
    else:
        print('')

def main():
    print('Welcome to the Sieve of Eratosthenese!')
    print('This program prints out all the prime numbers below a number set by you.')
    
    loop = True
    
    while loop:
        print('')
        n = int(input('Please enter the upper limit: '))
        print('')

        if (n > 500):
            print('Sorry,', n, 'is too big. Please choose another number')
        else:
            print('These are the prime numbers smaller than', n, end='')
            print(':')
            SieveOfEratosthenes(n)
            
            while True:
                again = input('Woud you like to go again? (y/n) ')
                if again == 'n':
                    loop = False
                    break
                elif again == 'y':
                    break

main()