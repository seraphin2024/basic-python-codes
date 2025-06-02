# Take a list of numbers and print the maximum element.
maxi = -1
number = list(map(int, input("Enter numbers separated by space: ").split()))

for num in number :
    if(num>maxi): maxi = num

print("max is : ", maxi)
