# wap to check whether  a number is prime or not 
def checkPrime(a):
    count = 0
    for i in range (1, a+1):
        if(a%i== 0):
          count = count + 1
    
    if(count>2) : return False
    else : return True 


    

number = int(input("enter the number : "))
print(checkPrime(number))
