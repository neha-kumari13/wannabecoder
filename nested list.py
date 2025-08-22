students = []   # empty list to store students

for i in range(1, 6):   # loop for 5 students
    name = input("Enter student name: ").upper()   # capital letters
    
    # take 5 subject marks
    m1 = int(input("Enter mark 1: "))
    m2 = int(input("Enter mark 2: "))
    m3 = int(input("Enter mark 3: "))
    m4 = int(input("Enter mark 4: "))
    m5 = int(input("Enter mark 5: "))

    total = m1 + m2 + m3 + m4 + m5
    percentage = (total / 500) * 100
    
    students.append([i, name, percentage])   # add student details to list

print("\n=== STUDENT PERCENTAGE LIST ===")
print("S.No   Name        Percentage")

for s in students:
    print(s[0], "   ", s[1], "   ", str(round(s[2], 2)) + "%")
