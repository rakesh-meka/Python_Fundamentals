# 1. Creating tuples
numbers = (10, 20, 30, 40)
mixed = (1, "Python", 3.14, True)

print("Numbers Tuple:", numbers)
print("Mixed Tuple:", mixed)

# 2. Accessing elements (Indexing)
print("First element:", numbers[0])
print("Last element:", numbers[-1])

# 3. Slicing a tuple
print("Slice (1 to 3):", numbers[1:3])

# 4. Tuple is immutable (cannot be changed)
# numbers[0] = 100  # ❌ This will raise TypeError

# 5. Tuple methods
sample = (1, 2, 2, 3, 4, 2)
print("Count of 2:", sample.count(2))
print("Index of 3:", sample.index(3))

# 6. Looping through a tuple
print("Looping through numbers:")
for num in numbers:
    print(num)

# 7. Tuple unpacking
a, b, c, d = numbers
print("Unpacked values:", a, b, c, d)

# 8. Nested tuples
nested = ((1, 2), (3, 4), (5, 6))
print("Nested Tuple:", nested)
print("Access nested element:", nested[1][0])

# 9. Tuple as dictionary keys (use-case)
locations = {
    (12.9716, 77.5946): "Bangalore",
    (17.3850, 78.4867): "Hyderabad"
}
print("Location lookup:", locations[(12.9716, 77.5946)])

# 10. When to use tuples
print("Tuples are used when data should not be modified.")