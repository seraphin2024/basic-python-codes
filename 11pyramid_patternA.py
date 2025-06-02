'''
Print a pyramid pattern using *:

*
**
***
****

'''

limit = int(input("enter the limit for rows  "))
for i in range (1,limit+1):
  for j in range (1,i+1):
     print("*",end="")
  print('')