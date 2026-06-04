#============ PYTHON ONE-LINERS =============
from pickletools import pystring

# 1. SWAP TWO VARIABLES

a = 10
b = 20

print("\n1. Swap Variables")
print("Before:", a, b)

a, b = b, a

print("After :", a, b)

# 2. IF ELSE ONE-LINER

age = 12
print("\n2. If Else One-Liner")
print("Adult" if age >= 18 else "Minor")


# 3. LIST COMPREHENSION - SQUARES
print("\n3. Squares")
squares = [i * i for i in range(1, 6)]
print(squares)

# 4. EVEN NUMBERS
print("\n4. Even Numbers")
evens = [x for x in range(20) if x % 2 == 0]
print(evens)

# 5. REVERSE STRING
print("\n5. Reverse String")
text = "python"
print(text[::-1])

# 6. REVERSE LIST
print("\n6. Reverse List")
numbers = [1, 2, 3, 4]
print(numbers[::-1])

# STRING MANIPULATION
print("\n7. String Manipulation")

s = "hello world"

# Reverse string
reversed_str = s[::-1]
print("Reverse:", reversed_str)

# Palindrome check
is_palindrome = lambda x: x == x[::-1]
print("Palindrome:", is_palindrome("madam"))

# Count vowels
vowel_count = sum(c in "aeiouAEIOU" for c in s)
print("Vowels:", vowel_count)

# Remove vowels
no_vowels = ''.join(c for c in s if c.lower() not in 'aeiou')
print("Without vowels:", no_vowels)

# Capitalize words
capitalized = ' '.join(word.capitalize() for word in s.split())
print("Capitalized:", capitalized)

# NUMBERS & MATH
print("\n8. Numbers & Math")

from math import prod, gcd

factorial = lambda n: prod(range(1, n + 1))
print("Factorial 5:", factorial(5))

is_prime = lambda n: n > 1 and all(
    n % i for i in range(2, int(n ** 0.5) + 1)
)

print("Prime 17:", is_prime(17))

print("GCD(12,18):", gcd(12, 18))

sum_sq = sum(i * i for i in range(1, 6))
print("Sum of squares:", sum_sq)

# LOGIC & CONDITIONALS
print("\n9. Logic & Conditionals")

x = 15

result = "Yes" if x > 10 else "No"
print(result)

lst = [1, 2, 3, 4, 5]

unique = len(set(lst)) == len(lst)
print("Unique:", unique)

print("All True:", all([True, True, True]))
print("Any True:", any([False, False, True]))

# LISTS & COLLECTIONS
print("\n10. Lists & Collections")

matrix = [[1, 2], [3, 4], [5, 6]]

flat = [i for sub in matrix for i in sub]

print("Flattened:", flat)

numbers = [1, 2, 3, 4, 5, 6]

evens = [x for x in numbers if x % 2 == 0]

print("Even Numbers:", evens)

duplicates = list(
    set([x for x in [1, 2, 3, 1, 2, 4] if [1, 2, 3, 1, 2, 4].count(x) > 1])
)

print("Duplicates:", duplicates)

cleaned = [x for x in [1, None, 2, None, 3] if x is not None]

print("Removed None:", cleaned)

# DICTIONARIES
print("\n11. Dictionaries")

keys = ["name", "age"]
values = ["Salina", 22]

d = dict(zip(keys, values))

print(d)

swapped = {v: k for k, v in d.items()}

print("Swapped:", swapped)

# COLLECTIONS MODULE
print("\n12. Counter")

from collections import Counter

data = [1, 2, 2, 3, 3, 3]

counts = Counter(data)

print(counts)

# MATRIX OPERATIONS
print("\n13. Matrix Transpose")

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

transposed = list(zip(*matrix))

print(transposed)

# UTILITIES
print("\n14. Utilities")

filename = "program.py"

ext = filename.split(".")[-1]

print("Extension:", ext)

binary = "1010"

decimal = int(binary, 2)

print("Binary to Decimal:", decimal)

words = ["apple", "banana", "watermelon"]

max_len = max(map(len, words))

print("Longest word length:", max_len)

# LAMBDA + MAP + FILTER
print("\n15. Lambda, Map, Filter")

nums = [1, 2, 3, 4, 5]

squares = list(map(lambda x: x * x, nums))

print("Squares:", squares)

numbers = [-3, -1, 2, 5, -8]

positives = list(filter(lambda x: x >= 0, numbers))

print("Positives:", positives)


# DATE & TIME
print("\n17. Current Date & Time")

from datetime import datetime

print(datetime.now())

# TUPLE UNPACKING
print("\n18. Tuple Unpacking")

a, b, c = (1, 2, 3)

print(a, b, c)

# SECOND LARGEST NUMBER
print("\n19. Second Largest")

lst = [10, 20, 30, 40, 50]

second_largest = sorted(set(lst))[-2]

print(second_largest)

# REPEAT STRING
print("\n20. Repeat String")

repeated = "hello " * 5

print(repeated)
