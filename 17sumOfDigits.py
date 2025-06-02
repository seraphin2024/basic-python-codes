# give the sum of digits :

def sum_digits(n):
    sum = 0 

    while(n>0):
        a =  n%10 
        n = int(n/10 )
        sum = sum + a 
    return sum 


number = int(input("enter any number : "))
print("sum of the digits of that number is : ", sum_digits(number))

    