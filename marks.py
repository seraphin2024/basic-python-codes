# Print students with marks > 80


n = int(input("Enter number of students: "))

students = {}

for i in range(n):
    name = input("Enter name: ")
    marks = int(input("Enter marks: "))
    students[name] = marks

print("Students scoring more than 80:")


for name in students:
    if students[name] > 80:
        print(name, "->", students[name])