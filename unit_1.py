"""
Problems Solution of Unit 1:
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

s = 'azcbobobegghakl'

longest = ""
comp = ""

for idx, char in enumerate(s):
    comp += char
    for i in range(idx + 1, len(s)):
        if (s[i] < comp[-1]):
            break
        elif (s[i] >= comp[-1]):
            comp += s[i]
    if len(comp) > len(longest):
        longest = comp
    comp = ""
    
print(f"Longest substring in alphabtical order is: {longest}")
