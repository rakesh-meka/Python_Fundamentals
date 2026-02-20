#1. Reverse string

s = input("Enter the string:")
result = s[::-1]
print(result)

#2. check  if string is palindrome 

s = input("Enter the String:")

if s == s[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

#3. Removes spaces from a string
s = input("Enter the string:")
result=s.replace(" ", "")
print(result)

#4. count vowels and consonants

s = input("Enter the String:")

vowels = "aeiouAEIOU"

v_count = 0
c_count = 0

for i in s:
    if i in vowels:
        v_count+=1
    else:
        c_count+=1

print("Vowels:" , v_count)
print("Consonants: ", c_count)

#5. convert upper case and lower case 	nd vice versa


s = input("Enter the string:")

result = ""

for i in s:
    if i.isupper():
        result+=i.lower()
    elif i.islower():
        result+=i.upper()
    
print("After Converting String:", result)

#6.Find length of string without using len()

s = input("Enter the string:")

count =  0

for i in s:
    count+=1

print(count)

#7. Remove duplicate characters

s1 = input("Enter the string:")

result=""

for i in s1:
    if i not in result:
        result+=i

print(result)    

#8. Check if two strings are Anagrams

s1 = input("Enter the string:")
s2 = input("Enter the string:")

if sorted(s1) == sorted(s2):
    print("Anagrams")
else:
    print("Not Anagrams")

#9. count words in strings

s = input("Enter the string:")

a= s.split()

result = len(a)

print("count of words", result)

#10. reverse each word in string 

s = input("Enter the string:")

words = s.split()

result= " ".join(word[::-1]for word in words)

print(result)
