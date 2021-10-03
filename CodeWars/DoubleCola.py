def numSteps(x):
    return 5*(x**2)

def who_is_next(queue, n):
    for i in range(n):
        if numSteps(i+1) > n:
            stepsToCurrentFromLastFullLoop = n - numSteps(i)
            index = int(stepsToCurrentFromLastFullLoop/loops)
            return queue[index]


queue = ["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"]

print(who_is_next(queue, 6))