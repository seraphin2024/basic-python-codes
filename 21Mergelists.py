# Merge two lists and remove duplicates

list1 = list(map(int,input("enter the numbers with spaces : ").split()))
list2 = list(map(int,input("enter the numbers with spaces : ").split()))

list1.extend(list2)

unique = []


for  num in list1:
    if num not in unique :
        unique.append(num)

print(unique)

    