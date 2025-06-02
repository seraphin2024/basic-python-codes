# Check if a string is a palindrome

s = input("enter the string : ")
ans = True
i = 0
j = len(s)-1

while(j>=i):
    if(s[i]!=s[j]): 
        ans =  False 
        break
    i = i+1
    j = j-1


print(ans)
    


