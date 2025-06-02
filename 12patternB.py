'''
Print a pyramid pattern using *:

****
***
**
*

'''

row = int(input("enter the no. of rows: "))

for i in range (row , 0 , -1 ):
    for j in range (i, 0 , -1):
        print("*" , end="")
    print('')
