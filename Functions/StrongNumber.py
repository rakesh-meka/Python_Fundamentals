#Write a Python program using functions to check whether a given number is a Strong Number.

# Function to calculate factorial of a digit
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

# Function to check Strong Number
def is_strong_number(num):
    temp = num
    total = 0
    
#A Strong Number is a number where the sum of factorials of its digits is equal to the number itself.

    while temp > 0:
        digit = temp % 10
        total += factorial(digit)
        temp //= 10

    return total == num

# Taking input from user
number = int(input("Enter a number: "))

# Function call
if is_strong_number(number):
    print(number, "is a Strong Number")
else:
    print(number, "is NOT a Strong Number")
