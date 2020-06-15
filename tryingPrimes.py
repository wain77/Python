primes = [1]
possPrime = 2
upperLimit = 100

while possPrime < upperLimit:
    #printStr = "Possible prime: {}".format(possPrime)
    #print(printStr)

    isPrime = True
    num = 2
    
    while num < possPrime:
        #printStr = "Current divisor: {}".format(num)
        #print(printStr)

        primeTest = possPrime % num
        #printStr = "Outcome of primetest: {}".format(primeTest)
        #print(printStr)

        if primeTest == 0:
            isPrime = False
            break
        else:
            num += 1

    #printStr = "Is this a prime? {}".format(isPrime)
    #print(printStr)
    
    if isPrime == True:
        primes.append(possPrime)
        
    possPrime += 1

print(primes)
print(len(primes))
