'''
 Create a simple grade calculator:

90+: A, 80–89: B, 70–79: C, else:

'''

marks = int(input("enter the marks to know ur garde accodringly "))
if(marks>=90):
    print(" GRADE : A")
else:
    if(marks>=80  and marks<89):
        print(" GRADE : B")
    else:
        if(marks>=70 and marks<79):
            print("GRADE : C")
        else:
            print("GRADE : F")
