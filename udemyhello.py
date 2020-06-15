# This program says hello asks for my name

print('Hello world!')

myName = input('What is your name? ') # ask for their name
print('It\'s good to meet you, ' + myName)
print('The length of your name is: ' + str(len(myName)) + ' characters.')

myAge = input('How old are you? ') # Ask how old they are
print('On your next birthday, you will be: ' + str(int(myAge) + 1) + ' years old')

myBirthday = input('When is your birthday? ')
