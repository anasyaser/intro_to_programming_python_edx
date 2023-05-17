"""
 solution for problems of first unit
"""
# ----------------------------------------- #
# Problem 1

s = 'azcbobobegghakl'
i = 0
for char in s:
    if char in 'aeiou':
        i += 1
print(f"Number of vowels: {i}")

# ----------------------------------------- #
# Problem 2

x = 0
for i in range(len(s) - 2):
    if s[i: i+3] == "bob":
        x += 1
print(f"Number of times bob occures is: {x}")

# ----------------------------------------- #
# Problem 3


