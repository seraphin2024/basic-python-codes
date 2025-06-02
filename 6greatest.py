# Take three numbers and print the greatest.

a = int(input("enter the first no. "))
b = int(input("enter the second no. "))
c = int(input("enter the third no. "))

if(a>b):
  if(a>c):
     print(a," is the greatest number ")
  else:
     print(c," is the greatest .")
else:
   if(b>c):
      print(b," is the greatest .")
   else:
      print(c," is the greatest .")
   
# or we can just use the max function in python :)