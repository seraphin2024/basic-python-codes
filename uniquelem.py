# Print unique elements using set

nums = list(map(int, input("Enter numbers: ").split()))

unique = set()

for num in nums:
    unique.add(num)



print("Unique elements:", unique)