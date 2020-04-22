# Collatz conjecture

print('Welcome to the Collatz generator!')
print('')
print("Pick a number, and I will either: divide it by 2 if it's even; or: multiply by 3 and add 1 if it's odd; and we'll see how long it takes to get to 1!")

again = 'y'

while again == 'y':
    num = int(input('Pick a number: '))
    step = 0
    biggest = 0
    peakStep = 0

    while num != 1:             # Stop when we get to 1
        if num > biggest: 
            biggest = num       # Keep a record of the biggest number
            peakStep = step     # and which step it occurred on

        step += 1               # increment step here in case the biggest number is the input

        if num % 2 == 0:        
            num = int(num / 2)  # if num is even divide by 2
        else:                   
            num = (3 * num) + 1   # if num is odd multiply by 3 and add 1

        print('Step ' + str(step) + ': ' + str(num)) # Show progress

    # Display results
    print('You got to 1 in ' + str(step) + ' steps, with the number peaking at ' + str(biggest) + ' on step ' + str(peakStep))

    while True: # intentional infinite loop for input checking
        again = input('Would you like to go again? (y/n): ')
        if again == 'y' or again == 'n': break

print('Thanks for playing!')
