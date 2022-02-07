# tuple = collection which is ordered and unchangable 
# used to group together related data

student = ("Bro", 21, "male")

count = student.count("Bro")
index = student.index(21)
print(count)

for s in student:
    print(s)

if "Bro" in student:
    print("Bro is here")

if "Bros" in student:
    print("Bro is not here")