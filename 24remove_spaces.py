# Remove all spaces from a string

s = input("Enter a string: ")

ans = ""

for ch in s:
    if ch != ' ':
        ans += ch

print("String without spaces:", ans)