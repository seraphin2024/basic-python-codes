# Replace every vowel in a string with '*'

text = input("enterthe text : ")

res = ""

for i in range(len(text)):
    if text[i] in "aeiouAEIOU":
        res += '*'
    else:
        res += text[i]

print(res)