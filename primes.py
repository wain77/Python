primes = []
upperLimit = 10
for possiblePrime in range(2,upperLimit):
	isPrime = True
	for num in range(2, possiblePrime):
		if possiblePrime % num == 0:
			isPrime = False
			break
		
	if isPrime:
		primes.append(possiblePrime)

print(primes)
print(len(primes))