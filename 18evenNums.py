#count the number of even numbers in the lists 

nums = list(map(int , input('enter the numbers with space please : ').split()))
count = 0
for num in nums:
    if(num%2==0) : count = count + 1

print("no. of even numbers are : ",count)