import datetime

def getInput(ageToTurn):
    now = datetime.datetime.now()
    name = input('Would you mind telling me your name? ')
    age = float(input('And how old you are today? '))
    age += float(input('And how many months has it been since your last birthday? '))/12
    return {
        "name": name,
        "targetYear": str(ageToTurn - round(age) + now.year)
    }

if __name__ == "__main__":
    targetAge = 100
    data = getInput(targetAge)
    output =  f'Hello, {data["name"]}! You will turn {targetAge} in {data["targetYear"]}.'
    repeat = int(input('Please tell me how many times I should print the outcome: '))
    for x in range(repeat):
        print(output)