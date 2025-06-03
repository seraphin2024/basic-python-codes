
dict1 = {
   "Akshita" : "90%",
   "anshu"   : "45%",
   "tinshu"   : "89%",
   "tannu"   : "89.8%"

}

dict1["ranju"] = "98%"

dict1.update({'anshu': '77%'})

for x in dict1 :
    print(x ,":", dict1[x], "\n") 


if "Jhanavi" in dict1:
    print(dict1.get("jhanavi"))


