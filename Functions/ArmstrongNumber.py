def is_armstrong(num):
    temp = num
    digits = len(str(num))
    total = 0

    while temp > 0:
        digit = temp % 10
        total += digit ** digits
        temp //= 10

    return total == num


# Taking input from user
number = int(input("Enter a number: "))

# Function call
if is_armstrong(number):
    print(number, "is an Armstrong Number")
else:
    print(number, "is NOT an Armstrong Number")
