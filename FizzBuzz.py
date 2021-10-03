steps = 100
fizz = 5
buzz = 3

for x in range(steps + 1):
    output = ''
    if x % fizz == 0: output += "Fizz"
    if x % buzz == 0: output += "Buzz"
    if output == '': output = x
    print(output)
