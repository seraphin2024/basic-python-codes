'''
 reverse the sentence like this :
 " my home " -> home my 
   i knew it -> it knew i

'''
sentence = input("enter the string : ")
str1 = sentence .split()
str2 = str1[::-1]
revstr = ' '.join(str2)
print(revstr)


