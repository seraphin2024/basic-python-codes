
student1 = {
    "name":"Jhanavi ",
    "marks" : {
        "maths" : "A",
        "french" : "A+",
        "english" :"B"
    }    
}

student2 = {
    "name":"shikha ",
    "marks" : {
        "maths" : "A",
        "french" : "A+",
        "english" :"A"
    }    

}

student = {
    "student1" : student1,
    "student2" : student2
}

print(student["student1"]["name"])
print(student["student1"]["marks"]["english"])

student["student1"]["marks"]["english"] = "A++"
print(student["student1"]["marks"]["english"])

#looping through all the students name 
print("printing the names first : \n")
for x in student:
    print(student[x]["name"],"\n")


print("printing the marks for each student : \n")

#printing the subjects and marks of each student 
for x in student:
    print(student[x]["name"],":\n")
    
    for y in student[x]["marks"] :
        print(y ,": ",student[x]["marks"][y]," \n" )



