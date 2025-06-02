'''
Print a pyramid pattern using *:

*****
 ****
  ***
   **
    *

space on the left  = row no. - 1 
no of stars = row no. 

'''
row = int(input("enter the no. of rows please "))

for i in range (row,0,-1):
    for space in range (row-i):
        print(" ",end="")
    for j in range ( i , 0 ,-1):
        print("*", end="")
    print('')


        
    
