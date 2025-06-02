# reverse a list without using built in functions 

nums = list(map(int,input("enter the numbers with spaces ").split()))
revnums = []


for x in range(len(nums)-1,-1,-1):
    revnums.append(nums[x])

print(revnums)