__author__ = 'SamWainwright'

if __name__ == "__main__":
    num = int(input('Please enter a whole number: '))

    print(f'The divisors of {num} (not including 1 and {num}) are: {[div for div in list(range(2,num)) if not num % div]}')