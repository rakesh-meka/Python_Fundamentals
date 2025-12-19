#Write a Python function to check whether a given number is a Perfect Number.
def is_perfect(num):
    if num<=0:
        return False
    
    total = 0
    for i in range(1, num): #A number is called perfect if the sum of its proper divisors (excluding itself) is equal to the number.
        if num % i ==0:
            total +=i
    
    if total == num:
       return True
    else:
       return False
    
# Taking input from the user
number = int(input("Enter a number: "))

# Function call and output
if is_perfect(number):
    print(number, "is a Perfect Number")
else:
    print(number, "is NOT a Perfect Number")

